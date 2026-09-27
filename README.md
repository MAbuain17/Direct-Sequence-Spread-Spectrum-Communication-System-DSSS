# DSSS Lab

**A 2 MHz hardware demonstration, extended into a reproducible Python and MATLAB communications laboratory.**

[![Validate DSSS models](https://github.com/MAbuain17/dsss-lab/actions/workflows/validate.yml/badge.svg)](https://github.com/MAbuain17/dsss-lab/actions/workflows/validate.yml)
[![Native MATLAB validation](https://github.com/MAbuain17/dsss-lab/actions/workflows/matlab.yml/badge.svg)](https://github.com/MAbuain17/dsss-lab/actions/workflows/matlab.yml)

I built and tested a direct-sequence spread-spectrum (DSSS) link as an individual university project, following André Kesteloot's design in *QEX*, December 1986. This repository brings together my Multisim files, laboratory photographs, original report, and a new software study of the link's behaviour under noise, interference and receiver impairments.

![DSSS hardware in the university laboratory](assets/lab-15.jpg)

The hardware work covers PN generation, XOR spreading and square-carrier BPSK, code alignment, and analogue data recovery. The Python and MATLAB models cover framed text, PCM samples, BER, acquisition, pulse shaping and channel impairments.

## Start here

| Goal | Open |
|---|---|
| Understand the signal chain and assumptions | [Methodology](docs/methodology.md) |
| Explore BER, interference and acquisition results | [Simulation results](docs/results.md) |
| Run the project on Windows | [Getting started](docs/getting-started.md) |
| Explore the circuit and laboratory measurements | [Hardware](hardware/README.md) |
| Check the original report's corrections | [Technical errata](docs/errata.md) |
| Understand the source design and my contribution | [Attribution](docs/attribution.md) |
| Read the circuit's source article | [QEX, December 1986, pp. 5–9](docs/QEX_1986_12.pdf) |
| Compare hardware and software features | [Implementation overview](docs/implementation-matrix.md) |

## Run Python

From the repository root, using Python 3.10 or later:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python examples/burst_link.py
python -m dsss_lab.experiments
python examples/pulse_shaping.py
```

For a smaller run, add `--quick` to the experiment command. CSV files, figures and environment metadata are written to `results/`. Running without installing is also possible with `PYTHONPATH=src` on Linux/macOS; see the Windows guide for PowerShell.

## Run MATLAB

No Communications Toolbox is required. From the repository root:

```matlab
addpath('matlab');
test_dsss;
run_experiments('results/matlab', 12000);
advanced_demo('results/matlab');
```

MATLAB shares deterministic test vectors with Python. Random-number streams differ, so Monte Carlo results should agree statistically, not bit-for-bit. **Python, GNU Octave and native MATLAB pass the published GitHub Actions validation workflows.** Native MATLAB runs automatically when its implementation, shared vectors or workflow changes and remains manually dispatchable.

## What the software explores

| Area | Implemented experiments |
|---|---|
| Data | Random bits, constants, alternating patterns, bursts, UTF-8 text, 8-bit PCM, CRC32 frames |
| Spreading | Exact hardware XNOR recurrence, code phase, autocorrelation, configurable spreading length, two-user Gold-family interference |
| Channels | AWGN; in-band and out-of-band tones; swept interference; burst noise; multipath; symbol-independent Rayleigh fading |
| Receiver | Coherent despreading, known-preamble delay/CFO acquisition, burst phase correction, known-channel matched combining |
| Front end | Carrier offset, phase offset/noise, fractional timing error, ADC clipping/quantization, IQ imbalance, RRC pulse shaping |
| Measurements | BER with Wilson intervals, frame CRC failure rate, acquisition success, raw decision EVM, Welch PSD and 99% occupied bandwidth |
| Coding | Soft repetition decoding with equal information-bit energy as a normalization check |

## BER and interference

![DSSS and BPSK BER against theory](results/figures/awgn.png)

At equal information-bit energy, DSSS and ordinary coherent BPSK have the same theoretical BER in AWGN. Spreading's interference behaviour depends on the interferer's spectrum and the receiver. The experiments include cases where DSSS helps and cases where the narrower unspread receiver performs better.

![Interference comparison](results/figures/interference.png)

The simulation uses 60,000 bits per AWGN point and 30,000 bits per interference point. Source CSVs include error counts and confidence intervals; seeds and model settings are documented in [methodology](docs/methodology.md).

## Credits

Hardware implementation and laboratory report: **Mohamed Abuain**, supervised by Prof. Tammam Benmusa.

Circuit reference: André Kesteloot, N4ICK, “Experimenting With Direct-Sequence Spread Spectrum,” *QEX*, December 1986, pp. 5–9. [Read the issue](docs/QEX_1986_12.pdf) or see the [design notes](docs/attribution.md).

[Software licence](LICENSE.md) · [Changelog](CHANGELOG.md) · [Roadmap](docs/roadmap.md)
