# Maintenance and research roadmap

Version 0.1 includes the communications models, laboratory files and automated tests. Python, GNU Octave and native MATLAB first passed their published GitHub Actions workflows on 21 September 2026. Native MATLAB reruns on relevant MATLAB/vector changes and remains manually dispatchable.

| Priority | Work item | Milestone |
|---|---|---|
| P0 | Rev A firmware | USB command parser, configuration validation, shared PN/mapping vectors, timer/DMA DAC streaming |
| P0 | Rev A electrical review | Clock, USB, regulator thermals, analogue range and sampling requirements checked against selected parts |
| P1 | Board bring-up | Power rails, SWD, USB enumeration, DAC test tones and ADC captures |
| P1 | Configurable payload and PN | User bits/text/patterns, LFSR taps/seed/phase and uploaded codes |
| P1 | Modulation profiles | BPSK, QPSK, OOK and 2-FSK captures against known sample vectors |
| P2 | Loopback receiver | Correlation, code-phase estimation, timing alignment, CRC and BER comparison |
| P2 | CDMA model extensions | Asynchronous symbol arrivals, multipath channel estimation and measured near–far captures |
| P2 | RF expansion | SPI-controlled conversion/attenuation module after validating baseband interfaces |

Each extension should specify its channel assumptions, comparison baseline and acceptance tests.

## Contribution workflow

Use focused branches and descriptive commits. Record instrument settings and raw samples with new measurements. When changing numerical code, run the unit suite and relevant experiments, then review the generated CSVs and figures.

Planned tasks are listed in [issue-backlog.json](issue-backlog.json). GitHub Actions runs the validation suite on code changes.
