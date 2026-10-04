#!/usr/bin/env python3

import sys
import gzip
from collections import defaultdict

inp = sys.argv[1]
out = sys.argv[2]

def opener(path, mode="rt"):
    if path.endswith(".gz"):
        return gzip.open(path, mode)
    return open(path, mode)

intervals = defaultdict(list)

with opener(inp) as fh:
    for line in fh:
        if not line.strip() or line.startswith("#"):
            continue

        p = line.rstrip().split("\t")

        if len(p) < 5:
            continue

        seqid = p[0]
        start = int(p[3])
        end = int(p[4])

        intervals[seqid].append((start, end))


with gzip.open(out, "wt") as oh:

    for seqid in sorted(intervals):

        vals = sorted(intervals[seqid])

        current_start, current_end = vals[0]

        for start, end in vals[1:]:

            # merge overlapping or directly adjacent intervals
            if start <= current_end + 1:
                current_end = max(current_end, end)

            else:
                oh.write(
                    f"{seqid}\t{current_start}\t{current_end}\n"
                )

                current_start, current_end = start, end

        oh.write(
            f"{seqid}\t{current_start}\t{current_end}\n"
        )