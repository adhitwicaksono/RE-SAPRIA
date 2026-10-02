import gzip, sys, bisect, csv, math, statistics, os
from collections import defaultdict
import numpy as np
from scipy.stats import spearmanr

label=sys.argv[1]; repeat_union=sys.argv[2]; gff=sys.argv[3]; outprefix=sys.argv[4]

# Load merged repeat intervals per scaffold.
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

def overlap_bp(seq,s,e):
    dat=R.get(seq)
    if not dat: return 0
    starts, ends=dat
    i=bisect.bisect_left(ends,s)
    total=0; n=len(starts)
    while i<n and starts[i]<=e:
        a=max(s,starts[i]); b=min(e,ends[i])
        if a<=b: total += b-a+1
        i+=1
    return total

def attrs(s):
    d={}
    for part in s.strip().strip(';').split(';'):
        if '=' in part:
            k,v=part.split('=',1); d[k]=v
    return d

# Parse annotation.
genes={}; tx={}; gene_txs=defaultdict(list)
with gzip.open(gff,'rt',errors='replace') as fh:
    for line in fh:
        if not line or line[0]=='#': continue
        p=line.rstrip('\n').split('\t')
        if len(p)!=9: continue
        seq,src,typ,s,e,score,strand,phase,att=p; s=int(s); e=int(e); a=attrs(att)
        if typ=='gene':
            gid=a.get('ID');
            if gid: genes[gid]=(seq,s,e,strand)
        elif typ in ('mRNA','transcript'):
            tid=a.get('ID'); gid=a.get('Parent')
            if tid:
                tx[tid]={'gene':gid,'seq':seq,'s':s,'e':e,'strand':strand,'cds':[],'introns':[],'start':False,'stop':False}
                gene_txs[gid].append(tid)
        elif typ in ('CDS','intron','start_codon','stop_codon'):
            parent=a.get('Parent')
            if not parent: continue
            # Parent may theoretically be comma separated.
            for tid in parent.split(','):
                if tid not in tx: continue
                if typ=='CDS': tx[tid]['cds'].append((s,e))
                elif typ=='intron': tx[tid]['introns'].append((s,e))
                elif typ=='start_codon': tx[tid]['start']=True
                elif typ=='stop_codon': tx[tid]['stop']=True

# Choose representative longest-CDS transcript per gene.
reps={}
for gid,tids in gene_txs.items():
    valid=[t for t in tids if t in tx]
    if not valid: continue
    def key(tid):
        t=tx[tid]; cdsbp=sum(e-s+1 for s,e in t['cds']); span=t['e']-t['s']+1
        return (cdsbp,span,tid)
    reps[gid]=max(valid,key=key)

intron_rows=[]; gene_rows=[]
for gid,tid in reps.items():
    t=tx[tid]; seq=t['seq']; gs,ge=(genes.get(gid,(seq,t['s'],t['e'],t['strand']))[1:3])
    gene_len=ge-gs+1; gene_rep=overlap_bp(seq,gs,ge)
    cds_bp=cds_rep=0
    for s,e in t['cds']:
        L=e-s+1; cds_bp+=L; cds_rep+=overlap_bp(seq,s,e)
    intr_bp=intr_rep=0; longest=0; longest_rf=np.nan
    for idx,(s,e) in enumerate(t['introns'],1):
        L=e-s+1; rb=overlap_bp(seq,s,e); rf=rb/L
        intr_bp+=L; intr_rep+=rb
        if L>longest: longest=L; longest_rf=rf
        intron_rows.append((label,gid,tid,seq,idx,s,e,L,rb,rf))
    gene_rows.append((label,gid,tid,seq,gs,ge,gene_len,gene_rep,gene_rep/gene_len if gene_len else np.nan,
                      cds_bp,cds_rep,cds_rep/cds_bp if cds_bp else np.nan,
                      intr_bp,intr_rep,intr_rep/intr_bp if intr_bp else np.nan,
                      len(t['introns']),longest,longest_rf,int(t['start'] and t['stop'])))

# Output details.
os.makedirs(os.path.dirname(outprefix),exist_ok=True)
with gzip.open(outprefix+'.introns.tsv.gz','wt',newline='') as oh:
    w=csv.writer(oh,delimiter='\t'); w.writerow(['representation','gene_id','transcript_id','seqid','intron_index','start','end','length_bp','repeat_bp','repeat_fraction'])
    w.writerows(intron_rows)
with gzip.open(outprefix+'.genes.tsv.gz','wt',newline='') as oh:
    w=csv.writer(oh,delimiter='\t'); w.writerow(['representation','gene_id','transcript_id','seqid','start','end','gene_span_bp','gene_repeat_bp','gene_repeat_fraction','cds_bp','cds_repeat_bp','cds_repeat_fraction','intron_bp','intron_repeat_bp','intron_repeat_fraction','intron_count','longest_intron_bp','longest_intron_repeat_fraction','complete_start_stop_proxy'])
    w.writerows(gene_rows)

# Summary.
lengths=np.array([r[7] for r in intron_rows],dtype=float); rfr=np.array([r[9] for r in intron_rows],dtype=float); rbp=np.array([r[8] for r in intron_rows],dtype=float)
rho,p=spearmanr(lengths,rfr) if len(lengths)>1 else (np.nan,np.nan)
gene_arr=np.array([r[8] for r in gene_rows],dtype=float)
cds_bp=sum(r[9] for r in gene_rows); cds_rep=sum(r[10] for r in gene_rows)
intr_bp=sum(r[12] for r in gene_rows); intr_rep=sum(r[13] for r in gene_rows)
summary={
'label':label,'genes':len(gene_rows),'rep_introns':len(intron_rows),'median_intron_bp':float(np.median(lengths)) if len(lengths) else np.nan,
'max_intron_bp':int(np.max(lengths)) if len(lengths) else 0,'total_intron_bp':int(intr_bp),'intron_repeat_bp':int(intr_rep),'weighted_intron_repeat_pct':100*intr_rep/intr_bp if intr_bp else np.nan,
'spearman_length_repeat_fraction_rho':rho,'spearman_p':p,'median_intron_repeat_fraction':float(np.median(rfr)) if len(rfr) else np.nan,
'weighted_CDS_repeat_pct':100*cds_rep/cds_bp if cds_bp else np.nan,'median_gene_span_repeat_pct':100*float(np.median(gene_arr)) if len(gene_arr) else np.nan,
'complete_start_stop_proxy_pct':100*np.mean([r[-1] for r in gene_rows]) if gene_rows else np.nan
}
with open(outprefix+'.summary.tsv','w',newline='') as oh:
    w=csv.DictWriter(oh,fieldnames=summary.keys(),delimiter='\t'); w.writeheader(); w.writerow(summary)

# Size bins. Use half-open conceptual bins: <1k,1-5k,5-10k,10-50k,50-100k,>=100k.
bins=[('lt1kb',0,1000),('1to5kb',1000,5000),('5to10kb',5000,10000),('10to50kb',10000,50000),('50to100kb',50000,100000),('ge100kb',100000,float('inf'))]
with open(outprefix+'.bins.tsv','w',newline='') as oh:
    fn=['representation','bin','n_introns','pct_introns','intron_bp','pct_intron_bp','repeat_bp','weighted_repeat_pct','median_repeat_fraction']
    w=csv.DictWriter(oh,fieldnames=fn,delimiter='\t'); w.writeheader()
    totaln=len(lengths); totalbp=lengths.sum()
    for name,lo,hi in bins:
        mask=(lengths>=lo)&(lengths<hi)
        n=int(mask.sum()); bp=float(lengths[mask].sum()); rep=float(rbp[mask].sum())
        w.writerow({'representation':label,'bin':name,'n_introns':n,'pct_introns':100*n/totaln if totaln else 0,'intron_bp':int(bp),'pct_intron_bp':100*bp/totalbp if totalbp else 0,'repeat_bp':int(rep),'weighted_repeat_pct':100*rep/bp if bp else np.nan,'median_repeat_fraction':float(np.median(rfr[mask])) if n else np.nan})
print(summary)
