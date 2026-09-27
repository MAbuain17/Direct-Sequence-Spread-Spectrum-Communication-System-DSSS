# Laboratory implementation

The original 2 MHz university bench project by Mohamed Abuain. The new [configurable Rev A board](configurable/README.md) adds a programmable signal chain and I/Q interfaces.

![Breadboard assembly](../assets/lab-20.jpg)

The transmitter and receiver use PN generators, XOR spreading, square-carrier BPSK, comparator-driven code acquisition, a latch and clock switch, and an LM/MC1496 balanced demodulator. The laboratory setup uses a shared reference and a wired connection between transmitter and receiver.

## Circuit files

| File | Description |
|---|---|
| [DSSS_MAbuain.ms14](original/DSSS_MAbuain.ms14) | Main Multisim 14 project |
| [GOLD1.ms14](original/GOLD1.ms14) | Additional Multisim project |
| [MC1496_split_Gilbert_Cell_Test.asc](original/MC1496_split_Gilbert_Cell_Test.asc) | LTspice balanced-demodulator test schematic |
| `original/dsss.kicad_*` | Original KiCad layout concept |
| [Laboratory report](../docs/original-report.pdf) | Circuit description, measurements and discussion |

The [Rev A PCB package](configurable/README.md) contains the programmable baseband design, routed board and renders. [Engineering notes](../docs/errata.md) explain the original clock and spreading conventions.

## Laboratory captures

| Capture | Description |
|---|---|
| [Lab setup](../assets/lab-15.jpg) | Breadboard connected to test equipment |
| [Board close-up](../assets/lab-20.jpg) | Component placement and wiring |
| [Logic waveforms](../assets/lab-11.jpg) | Oscilloscope capture of digital signals |
| [Spectrum](../assets/lab-14.jpg) | Spectrum-analyzer capture |
| [Recovered signal](../assets/lab-01.jpg) | Demodulated waveform |

The report provides the context for these captures. Numerical BER and channel studies are documented in [simulation results](../docs/results.md).
