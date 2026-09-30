# Failed Guo reassembly attempt

This directory preserves provenance for an attempted independent Flye reconstruction of the Guo sequencing dataset.

## Status

The Guo Flye remake did **not** produce a usable completed assembly and is not carried forward as a genome representation in downstream RE-SAPRIA analyses.

The failure is retained in the repository because RE-SAPRIA is intended to document relevant analytical decisions and unsuccessful major branches rather than silently remove them from the project history.

## Interpretation

The failed run should not be interpreted as evidence that the Guo genome is intrinsically unassemblable. A failed workflow can reflect computational-resource limits, dataset scale, run configuration, scheduler/backend behavior, or other technical factors.

Accordingly:

- no biological conclusion is drawn from this failure;
- no incomplete Guo reassembly is used in comparative analyses;
- the published Guo assembly remains the Guo structural representation used downstream.

## Why Phase 2 was renamed

The original plan included independent reassembly of both Cai and Guo. Cai reassembly succeeded and produced the Flye–HyPo representation, whereas the Guo remake did not yield a usable assembly.

Phase 2 therefore became focused on **mapping independent Cai reads to Guo**, quantifying support and divergence, and generating the Cai-fixed-on-Guo pseudogenome rather than forcing symmetry between the two reconstruction branches.
