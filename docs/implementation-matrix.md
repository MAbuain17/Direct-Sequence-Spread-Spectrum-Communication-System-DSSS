# Implementation overview

| Capability | Hardware implementation | Python | MATLAB / Octave |
|---|---|---|---|
| 4 MHz reference / 2 MHz carrier | Report and lab waveforms | Ideal 2 MHz square-carrier trace | Same ideal trace |
| Seven-stage XNOR PN | Report sequence and scope observations | Exact recurrence; automated tests | Same recurrence; golden tests |
| Continuous PN across data intervals | Circuit design | Hardware mode | Hardware mode |
| XOR spreading and square-carrier modulation | Report and Multisim screenshots | Ideal logic model | Ideal logic model |
| Comparator / clock-switch acquisition | Reported code alignment; no measured time | Not gate-level simulated | Not gate-level simulated |
| LM/MC1496 analogue demodulator | Circuit and recovered-waveform evidence | Ideal despreading only | Ideal despreading only |
| 2 kHz test / Morse input | Report | Logic patterns; no physical Morse key | Logic patterns |
| Random data, framed text, CRC32 | Software study | Implemented | Implemented |
| PCM audio samples | Software study | Implemented | Implemented |
| BER versus Eb/N0 | Software study | Executed | Executed |
| Tone, chirp and burst interference | Software study | Executed | Executed |
| Joint preamble delay/CFO estimation | Software study | Executed | Executed |
| Multipath / ideal known-channel combining | Software study | Executed | Executed |
| Rayleigh fading / perfect CSI | Software study | Executed | Executed |
| Quantization, timing, IQ, phase impairments | Software study | Executed | Executed |
| RRC shaping and matched filtering | Software study | Executed | Executed |
| Two-user near-far study | Software study | Executed | Executed |
| Repetition-code energy check | Software study | Executed | Executed |
| Routed PCB, ERC, DRC, board bring-up | Not completed | Not applicable | Not applicable |

The MATLAB implementation is tested in GNU Octave and native MathWorks MATLAB. Hardware captures are linked from the [hardware page](../hardware/README.md); numerical experiments are described in [simulation results](results.md).
