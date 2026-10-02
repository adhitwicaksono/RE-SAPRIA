import gzip, sys, os, time
from pathlib import Path

inp=Path(sys.argv[1]); out=Path(sys.argv[2])
start=time.time(); rec=0; merged=0; bp=0; seqs=set()
cur_seq=None; cur_s=cur_e=None
with gzip.open(inp,'rt',errors='replace') as fh, gzip.open(out,'wt') as oh:
    for line in fh:
        if not line or line[0]=='#': continue
        p=line.rstrip('\n').split('\t')
        if len(p)<5: continue
        seq=p[0]; s=int(p[3]); e=int(p[4])
        rec+=1
        if cur_seq is None:
            cur_seq=seq; cur_s=s; cur_e=e; seqs.add(seq); continue
        if seq==cur_seq and s <= cur_e+1:
            if e>cur_e: cur_e=e
        else:
            oh.write(f'{cur_seq}\t{cur_s}\t{cur_e}\n'); merged+=1; bp+=cur_e-cur_s+1
            cur_seq=seq; cur_s=s; cur_e=e; seqs.add(seq)
    if cur_seq is not None:
        oh.write(f'{cur_seq}\t{cur_s}\t{cur_e}\n'); merged+=1; bp+=cur_e-cur_s+1
print(f'{inp.name}\trecords={rec}\tmerged={merged}\tbp={bp}\tseqs={len(seqs)}\tsec={time.time()-start:.1f}')
