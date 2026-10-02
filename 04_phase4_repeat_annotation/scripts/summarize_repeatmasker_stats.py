#!/usr/bin/env python3
import argparse, re, pathlib, pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("summaries", nargs="+")
ap.add_argument("--out", required=True)
args = ap.parse_args()

rows = []
for fn in args.summaries:
    text = pathlib.Path(fn).read_text()
    total = int(re.search(r"total length:\s+([0-9]+) bp", text).group(1))
    nonn = int(re.search(r"total length:\s+[0-9]+ bp\s+\(([0-9]+) bp excl N/X-runs\)", text).group(1))
    m = re.search(r"bases masked:\s+([0-9]+) bp \(\s*([0-9.]+) %\)", text)
    masked, pct = int(m.group(1)), float(m.group(2))
    rows.append({
        "file": pathlib.Path(fn).name,
        "total_bp": total,
        "nonN_bp": nonn,
        "masked_bp": masked,
        "masked_pct_nonN": pct,
        "masked_pct_total": 100 * masked / total,
        "nonrepeat_nonN_bp": nonn - masked,
    })

pd.DataFrame(rows).to_csv(args.out, sep="\t", index=False)
