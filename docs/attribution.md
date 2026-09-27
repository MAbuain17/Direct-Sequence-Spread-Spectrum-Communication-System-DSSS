# Circuit reference and implementation

The circuit is based on André Kesteloot, N4ICK, “Experimenting With Direct-Sequence Spread Spectrum,” *QEX*, December 1986, pp. 5–9, published by ARRL. The [complete issue](QEX_1986_12.pdf) is included for reference; the article begins on printed page 5.

Mohamed Abuain completed the university implementation individually: Multisim circuit simulation, breadboard assembly, waveform and spectrum measurements, and the [laboratory report](original-report.pdf). The report acknowledges supervision by Prof. Tammam Benmusa.

## Circuit adaptations

The QEX circuit compares seven-bit words with XOR/OR/NAND gates. The university report and schematic use a 74HC688 comparator and a laboratory function generator for the 4 MHz reference.

The hardware files include Multisim projects, an LTspice demodulator schematic and a KiCad placement study. The Python and MATLAB models implement the PN recurrence and extend the experiments to BER, interference, acquisition and receiver impairments. See the [implementation overview](implementation-matrix.md) for feature coverage.

## References

- [QEX source metadata](qex-source.json)
- [Technical corrections to the report](errata.md)
- [TI SN74LS164](https://www.ti.com/product/SN74LS164): shift-register specifications
- [TI SN74HC688](https://www.ti.com/product/SN74HC688): comparator specifications
