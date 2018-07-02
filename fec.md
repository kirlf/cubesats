# Modulation and coding \(FEC\)

## Thechnical survey

The main features of existing equipment are shown in table 3.1

#### Table 3.1 Modulation and FEC of real cubesat S-band transceivers

| Title | Modulation | FEC |
| --- | --- | --- | --- | --- | --- | --- |
| [ NanoCom SR2000](https://gomspace.com/UserFiles/Subsystems/datasheet/gs-ds-nanocom-sr2000-10.pdf) | Filtered QPSK \( Square root raised cosine filter, 𝛼 = 0.2\) | Concatenated coding: convolutional code plus Reed-Solomon \[C\(7, ½\) and RS \(255, 223\), interleaving depth 𝐿 = 8\] |
| [ISIS TXS High Data Rate S-Band Transmitter](https://www.cubesatshop.com/product/isis-txs-s-band-transmitter/) | OQPSK \( Pulse shaping: Square Root Raised Cosine, Roll-off 0.5, 0.35\) | Concatenated Reed Solomon and Convolutional coding \[C\(7, ½\) and RS \(255, 223\)\] |
| [ISIS TXS High Data Rate S-Band Transmitter](https://www.cubesatshop.com/product/isis-txs-s-band-transmitter/) | DQPSK | TURBO code, rate =0.489 |
| [S Band Transceiver for Small Satellites \( IQ wireless GmbH\)](http://www.iq-wireless.com/images/pdf/SLINK-Datasheet.pdf) | BPSK/QPSK/8PSK/QAM16 | Convolutional code, r=0.5 / 0.75 |
| [Full-duplex Low-power S-band Transceiver \(Nano Avionics\)](https://n-avionics.com/cubesat-components/communication-systems/cubesat-s-band-transceiver/) | GMSK modulation \(BT=0.35\) | Configurable Reed-Solomon and convolutional coding forward error correction |
| [CDMA communication system performance for a constellation of CubeSats around the Moon \(IEEE paper\)](https://ieeexplore.ieee.org/document/7500710/) | filtered offset QPSK with phase modulation \(a CCSDS standard\) \(OQPSK/PM\) | LDPC r=0.5 |

## Modulation

### Why QPSK is preferable in comparison with BPSK?

### QPSK vs. OQPSK

### QPSK vs. MSK

| Modulation | QPSK | MSK |
| --- | --- | --- |
| Energy gain |  |  |
| Spectral efficiency | 1 | 0.667 |

### MSK vs. GMSK

### Shaped OQPSK vs. conventional OQPSK

### Shaped OQPS vs. MSK/GMSK

## Channel coding \(FEC\)

As we can see from table 3.1 very popular option of the FEC is RSC \(Reed-Solomon convolutional\) concatenated codes. It relates to deep-space communication standartd \(fig. 3.1\) that allows to achieve sufficiently high BER performance \(fig. 3.2\).

![ Fig. 3.1. Deep-space concatenated coding system. \[1, p. 433\]](.gitbook/assets/rsc.png)



![Fig. 3.2. Typical performance curves for concatenated and unconcatenated coding systems for the space channel \(AWGN\) \[2, p.27\]](.gitbook/assets/rsc-2.png)

  
Very interesting research can be found also in [\[3\]](https://publik.tuwien.ac.at/files/publik_262129.pdf)  where capabilities of Turbo convolutional , LDPC  and Polar codes are considered. 

Morover, according to[ \[4\]](https://ieeexplore.ieee.org/document/7095355/), in general,  Turbo codes have the similar computational complexity with RSC codes.



## References

\[1\] Moon Todd, K. Error correction coding: mathematical methods and algorithms. 2005 by John Wiley & Sons. ISBN 0-471-64800-0.

\[2\] J. Hagenauer, E. Offer, and L. Papke, Reed Solomon Codes and Their Applications. New York IEEE Press, 1994

\[3\] Tahir, Bashar, Stefan Schwarz, and Markus Rupp. "BER comparison between Convolutional, Turbo, LDPC, and Polar codes." Telecommunications \(ICT\), 2017 24th International Conference on. IEEE, 2017.

\[4\] Balaji, Pavithra,u et al. "Evaluaton of decoding trade-ofs of concatenated RSconvolutonal codes and turbo codes via trellis." Signal Pricessing andIntegrated Netwirks \(SPIN\), 2015 2nd Internatinal Cinference in. IEEE, 2015

