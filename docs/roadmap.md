# Maintenance and research roadmap

Version 0.1 includes the communications models, laboratory files and automated tests. Python, GNU Octave and native MATLAB first passed their published GitHub Actions workflows on 21 September 2026. Native MATLAB reruns on relevant MATLAB/vector changes and remains manually dispatchable.

| Priority | Work item | Definition of done |
|---|---|---|
| P0 | Rerun original Multisim model | Export current netlist, operating points and labelled waveforms; reconcile report and as-built component list |
| P1 | Hardware-equivalent acquisition model | Explicit doubled-clock phase search, latch behaviour, initial phases and timing assumptions; compare with lab capture |
| P1 | Complete PCB schematic | Verified pin map, logic margins, bias and power circuits; clean ERC |
| P1 | New routed PCB | Reviewed layout, zero unrouted connections, clean DRC, fabrication review; physical validation remains a later gate |
| P2 | Off-grid acquisition / tracking | CFO estimator refinement, false-alarm-controlled detection, fractional timing and sample-clock recovery |
| P2 | Realistic fading | Correlated Rayleigh/Rician channel with stated Doppler, channel estimation and imperfect-CSI receiver |
| P2 | Stronger FEC | Convolutional/LDPC or another justified code with equal energy, rate and bandwidth comparisons |
| P2 | Multiuser receiver | Asynchronous users, power control, matched-filter versus decorrelating/MMSE detection |
| P3 | SDR bridge | File-based I/Q exchange and loopback; RF use only after front-end and local operating constraints are established |

Each extension should specify its channel assumptions, comparison baseline and acceptance tests.

## Contribution workflow

Use focused branches and descriptive commits. Record instrument settings and raw samples with new measurements. When changing numerical code, run the unit suite and relevant experiments, then review the generated CSVs and figures.

Planned tasks are listed in [issue-backlog.json](issue-backlog.json). GitHub Actions runs the validation suite on code changes.
