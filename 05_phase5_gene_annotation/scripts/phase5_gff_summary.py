#!/usr/bin/env python3
"""
Summarize BRAKER3/AUGUSTUS GFF3 outputs for RE-SAPRIA Phase 5.

The script intentionally uses only the Python standard library plus pandas/numpy
for summary output. It does not require genome FASTA files.

Representative transcript rule:
    longest total CDS length per gene; transcript span and ID break ties.

The "complete ORF proxy" is structural only:
    a transcript has both an explicit start_codon and stop_codon feature.
It is not a functional validation.
"""
import argparse, gzip
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
import pandas as pd

def attrs(s):
    d = {}
    for part in s.strip().strip(";").split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            d[k] = v
    return d

def parse_gff(path):
    counts = Counter()
    genes, txs = {}, {}
    gene_txs = defaultdict(list)
    seqids = set()
    with gzip.open(path, "rt", errors="replace") as fh:
        for line in fh:
            if not line.strip() or line.startswith("#"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) != 9:
                raise ValueError(f"Malformed GFF3 line: {line[:120]!r}")
            seqid, source, ftype, start, end, score, strand, phase, attr = p
            start, end = int(start), int(end)
            a = attrs(attr)
            counts[ftype] += 1
            seqids.add(seqid)
            if ftype == "gene":
                genes[a["ID"]] = dict(seqid=seqid, start=start, end=end,
                                      strand=strand, span=end-start+1)
            elif ftype in ("mRNA", "transcript"):
                tid = a["ID"]
                txs[tid] = dict(gene=a.get("Parent"), start=start, end=end,
                                span=end-start+1, cds_bp=0, cds_n=0,
                                intron_bp=0, intron_n=0,
                                start_codon=False, stop_codon=False)
                gene_txs[a.get("Parent")].append(tid)
            elif ftype in ("CDS", "intron", "start_codon", "stop_codon"):
                parent = a.get("Parent")
                if parent not in txs:
                    continue
                L = end-start+1
                if ftype == "CDS":
                    txs[parent]["cds_bp"] += L
                    txs[parent]["cds_n"] += 1
                elif ftype == "intron":
                    txs[parent]["intron_bp"] += L
                    txs[parent]["intron_n"] += 1
                elif ftype == "start_codon":
                    txs[parent]["start_codon"] = True
                elif ftype == "stop_codon":
                    txs[parent]["stop_codon"] = True
    return counts, genes, txs, gene_txs, seqids

def reps(txs, gene_txs):
    out = {}
    for gene, tids in gene_txs.items():
        if not tids:
            continue
        out[gene] = max(tids, key=lambda t: (txs[t]["cds_bp"], txs[t]["span"], t))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True)
    ap.add_argument("--gff", required=True)
    ap.add_argument("--assembly-span", required=True, type=int)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    counts, genes, txs, gene_txs, seqids = parse_gff(args.gff)
    r = reps(txs, gene_txs)
    rep_txs = [txs[t] for t in r.values()]
    tx_complete = [t["start_codon"] and t["stop_codon"] for t in txs.values()]
    rep_complete = [t["start_codon"] and t["stop_codon"] for t in rep_txs]

    row = {
        "representation": args.label,
        "assembly_span_bp": args.assembly_span,
        "genes": len(genes),
        "transcripts": len(txs),
        "CDS_features": counts["CDS"],
        "exon_features": counts["exon"],
        "intron_features": counts["intron"],
        "gene_density_per_Mb": len(genes)/(args.assembly_span/1e6),
        "gene_span_median": np.median([g["span"] for g in genes.values()]),
        "gene_span_p95": np.quantile([g["span"] for g in genes.values()], 0.95),
        "gene_span_max": max(g["span"] for g in genes.values()),
        "complete_orf_proxy_pct": 100*np.mean(tx_complete),
        "rep_complete_orf_proxy_pct": 100*np.mean(rep_complete),
        "seqids_with_features": len(seqids),
    }
    pd.DataFrame([row]).to_csv(args.out, sep="\t", index=False)

if __name__ == "__main__":
    main()
