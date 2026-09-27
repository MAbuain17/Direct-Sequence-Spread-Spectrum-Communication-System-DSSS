# Hardware implementation

An individual university project by Mohamed Abuain, based on André Kesteloot's [QEX circuit](../docs/QEX_1986_12.pdf), December 1986, pp. 5–9.

![Breadboard assembly](../assets/lab-20.jpg)

The transmitter and receiver use PN generators, XOR spreading, square-carrier BPSK, comparator-driven code acquisition, a latch and clock switch, and an LM/MC1496 balanced demodulator. The laboratory setup uses a shared reference and a wired connection between transmitter and receiver.

## Circuit files

| File | Description |
|---|---|
| [DSSS_MAbuain.ms14](original/DSSS_MAbuain.ms14) | Main Multisim 14 project |
| [GOLD1.ms14](original/GOLD1.ms14) | Additional Multisim project |
| [MC1496_split_Gilbert_Cell_Test.asc](original/MC1496_split_Gilbert_Cell_Test.asc) | LTspice balanced-demodulator test schematic |
| `original/dsss.kicad_*` | KiCad component placement study; routing is pending |
| [Laboratory report](../docs/original-report.pdf) | Circuit description, measurements and discussion |

The [PCB review](audit/pcb-review.md) records connectivity counts and the next design steps. [Technical notes](../docs/errata.md) clarify the report's rate and bandwidth calculations.

## Laboratory captures

| Capture | Description |
|---|---|
| [Lab setup](../assets/lab-15.jpg) | Breadboard connected to test equipment |
| [Board close-up](../assets/lab-20.jpg) | Component placement and wiring |
| [Logic waveforms](../assets/lab-11.jpg) | Oscilloscope capture of digital signals |
| [Spectrum](../assets/lab-14.jpg) | Spectrum-analyzer capture |
| [Recovered signal](../assets/lab-01.jpg) | Demodulated waveform |

The report provides the context for these captures. Numerical BER and channel studies are documented in [simulation results](../docs/results.md).
