import gzip, bisect, csv, os, sys
from collections import defaultdict
import numpy as np

repeat_union=sys.argv[1]
soft_gff=sys.argv[2]
unmask_gff=sys.argv[3]
braker_gff=sys.argv[4]
outdir=sys.argv[5]
os.makedirs(outdir,exist_ok=True)

# repeat index
R={}
with gzip.open(repeat_union,'rt') as fh:
    cur=None; starts=[]; ends=[]
    for line in fh:
        seq,s,e=line.rstrip().split('\t'); s=int(s); e=int(e)
        if seq!=cur:
            if cur is not None: R[cur]=(starts,ends)
            cur=seq; starts=[]; ends=[]
        starts.append(s); ends.append(e)
    if cur is not None: R[cur]=(starts,ends)

def rep_overlap(seq,s,e):
    dat=R.get(seq)
    if not dat:return 0
    starts,ends=dat; i=bisect.bisect_left(ends,s); tot=0
    while i<len(starts) and starts[i]<=e:
        a=max(s,starts[i]); b=min(e,ends[i])
        if a<=b: tot+=b-a+1
        i+=1
    return tot

def attrs(s):
    d={}
    for x in s.strip().strip(';').split(';'):
        if '=' in x:
            k,v=x.split('=',1); d[k]=v
    return d

def parse_aug(path):
    genes={}; txgene={}; cds=defaultdict(list)
    with gzip.open(path,'rt',errors='replace') as fh:
        for line in fh:
            if not line or line[0]=='#':continue
            p=line.rstrip('\n').split('\t')
            if len(p)!=9:continue
            seq,src,typ,s,e,score,strand,phase,att=p; s=int(s); e=int(e); a=attrs(att)
            if typ=='gene': genes[a['ID']]={'seq':seq,'s':s,'e':e,'strand':strand}
            elif typ in ('transcript','mRNA'): txgene[a['ID']]=a.get('Parent')
            elif typ=='CDS':
                parent=a.get('Parent')
                if parent: cds[parent].append((s,e))
    for tid,gid in txgene.items():
        if gid in genes: genes[gid]['cds']=cds.get(tid,[])
    return genes

def parse_braker_genes(path):
    genes={}
    with gzip.open(path,'rt',errors='replace') as fh:
        for line in fh:
            if not line or line[0]=='#':continue
            p=line.rstrip('\n').split('\t')
            if len(p)!=9 or p[2]!='gene':continue
            a=attrs(p[8]); genes[a['ID']]={'seq':p[0],'s':int(p[3]),'e':int(p[4]),'strand':p[6]}
    return genes

def build_gene_index(genes):
    d=defaultdict(list)
    for gid,g in genes.items(): d[(g['seq'],g['strand'])].append((g['s'],g['e'],gid))
    out={}
    for k,v in d.items():
        v.sort(); out[k]=( [x[0] for x in v], v )
    return out

def overlaps(index,seq,strand,s,e):
    dat=index.get((seq,strand));
    if not dat:return []
    starts,v=dat
    i=bisect.bisect_right(starts,e)
    hits=[]
    # backwards until starts too low isn't enough because intervals can be long; scan all prior? optimize with max end unavailable.
    # Gene numbers per scaffold small enough; use local full list query.
    for a,b,gid in v[:i]:
        if b>=s:hits.append(gid)
    return hits

soft=parse_aug(soft_gff); unmask=parse_aug(unmask_gff); br=parse_braker_genes(braker_gff)
soft_idx=build_gene_index(soft); br_idx=build_gene_index(br)

def add_metrics(genes, which):
    rows=[]
    for gid,g in genes.items():
        L=g['e']-g['s']+1; rb=rep_overlap(g['seq'],g['s'],g['e'])
        cb=cr=0
        for s,e in g.get('cds',[]):
            cb+=e-s+1; cr+=rep_overlap(g['seq'],s,e)
        rows.append({'set':which,'gene_id':gid,'seqid':g['seq'],'start':g['s'],'end':g['e'],'strand':g['strand'],'gene_span_bp':L,
                     'gene_repeat_bp':rb,'gene_repeat_fraction':rb/L,'cds_bp':cb,'cds_repeat_bp':cr,'cds_repeat_fraction':cr/cb if cb else np.nan,
                     'overlaps_softmasked_same_strand':bool(overlaps(soft_idx,g['seq'],g['strand'],g['s'],g['e'])) if which=='unmasked' else np.nan,
                     'overlaps_BRAKER_same_strand':bool(overlaps(br_idx,g['seq'],g['strand'],g['s'],g['e']))})
    return rows
rows=add_metrics(soft,'softmasked')+add_metrics(unmask,'unmasked')
with gzip.open(os.path.join(outdir,'augustus_repeat_gene_detail.tsv.gz'),'wt',newline='') as oh:
    w=csv.DictWriter(oh,fieldnames=rows[0].keys(),delimiter='\t'); w.writeheader(); w.writerows(rows)

# summaries by set and categories
import pandas as pd
df=pd.DataFrame(rows)
summ=[]
for name,sub in [('softmasked_all',df[df['set']=='softmasked']),('unmasked_all',df[df['set']=='unmasked']),
                 ('unmasked_overlaps_softmasked',df[(df['set']=='unmasked')&(df.overlaps_softmasked_same_strand==True)]),
                 ('unmasked_no_softmasked_overlap',df[(df['set']=='unmasked')&(df.overlaps_softmasked_same_strand==False)]),
                 ('unmasked_overlaps_BRAKER',df[(df['set']=='unmasked')&(df.overlaps_BRAKER_same_strand==True)]),
                 ('unmasked_no_BRAKER_overlap',df[(df['set']=='unmasked')&(df.overlaps_BRAKER_same_strand==False)]),
                 ('softmasked_overlaps_BRAKER',df[(df['set']=='softmasked')&(df.overlaps_BRAKER_same_strand==True)]),
                 ('softmasked_no_BRAKER_overlap',df[(df['set']=='softmasked')&(df.overlaps_BRAKER_same_strand==False)])]:
    if len(sub)==0:continue
    summ.append({'category':name,'n_genes':len(sub),'median_gene_span_bp':sub.gene_span_bp.median(),'median_gene_repeat_fraction':sub.gene_repeat_fraction.median(),
                 'mean_gene_repeat_fraction':sub.gene_repeat_fraction.mean(),'pct_gene_span_repeat_ge50':100*(sub.gene_repeat_fraction>=0.5).mean(),
                 'median_CDS_repeat_fraction':sub.cds_repeat_fraction.median(),'mean_CDS_repeat_fraction':sub.cds_repeat_fraction.mean(),
                 'pct_CDS_repeat_ge50':100*(sub.cds_repeat_fraction>=0.5).mean(),
                 'pct_overlaps_BRAKER_same_strand':100*sub.overlaps_BRAKER_same_strand.astype(float).mean()})
pd.DataFrame(summ).to_csv(os.path.join(outdir,'augustus_repeat_summary.tsv'),sep='\t',index=False)
print(pd.DataFrame(summ).to_string(index=False))
