## Table of contents

### Tutorials (Python)
1. [Sat-to-Ground (and vice versa) link budget calculation](https://nbviewer.jupyter.org/github/kirlf/cubesats/blob/master/LinkBudget/LB.ipynb)
2. [Intersatellite Link budget calculation (wireless optical)](https://nbviewer.jupyter.org/github/kirlf/cubesats/blob/master/Optical-ISL-LB.ipynb)

### Surveys
1. [Statistical channel model survey](https://github.com/kirlf/cubesats/blob/master/statistical_model.md)
2. Modulation and coding \(FEC\) survey

# Survey of modulation and coding schemes for application in CubeSat systems (afterwords)

## 3.1. Technical survey

The main features of existing equipment are shown in table 3.1

#### Table 3.1 Modulation and FEC of real cubesat S-band, X-band and Ka-band transceivers (some of examples are provided by [ Wong, Y. F., Kegege, O., Schaire, S. H., Bussey, G., Altunc, S., Zhang, Y., & Chitra, P. (2016). An optimum space-to-ground communication concept for CubeSat platform utilizing NASA space network and near earth network.](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160007683.pdf))

| Title | Modulation | FEC |
| :--- | :--- | :--- |
| [ISIS TXS High Data Rate S-Band Transmitter](https://www.cubesatshop.com/product/isis-txs-s-band-transmitter/) | BPSK, [OQPSK](https://en.wikipedia.org/wiki/Phase-shift_keying#Offset_QPSK_(OQPSK)) \([Pulse shaping](https://en.wikipedia.org/wiki/Pulse_shaping): Square [Root Raised Cosine](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20120008631.pdf), Roll-off 0.5, 0.35\) | [Concatenated coding](http://www.scholarpedia.org/article/Concatenated_codes#RS60): [Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction#Space_transmission) and [Convolutional coding](https://en.wikipedia.org/wiki/Convolutional_code): RS (255, 223) and CC (constrain length = 7, code rate = 1/2)|
| [ NanoCom SR2000](https://gomspace.com/UserFiles/Subsystems/datasheet/gs-ds-nanocom-sr2000-230.pdf) | Filtered QPSK (Square root raised cosine filter, 𝛼 = 0.2) |  Convolutional code (7, 1/2) + Reed-Solomon code (255, 223), interleaving depth 𝐿 = 8 |
| [CDMA communication system performance for a constellation of CubeSats around the Moon \(IEEE paper\)](https://ieeexplore.ieee.org/document/7500710/) | filtered OQPSK with phase modulation \(a [CCSDS](https://en.wikipedia.org/wiki/Consultative_Committee_for_Space_Data_Systems) standard\) \(OQPSK/PM\) | LDPC r=0.5 |
| [S Band Transceiver for Small Satellites \( IQ wireless GmbH\)](https://www.iq-spacecom.com/images/downloads/SLINK-PHY-datasheet.pdf) | **Uplink**: BPSK; **Downlink**: QPSK | -|
| [Full-duplex Low-power S-band Transceiver \(Nano Avionics\)](https://n-avionics.com/cubesat-components/communication-systems/cubesat-s-band-transceiver/) | GMSK modulation \(BT=0.35\) | Configurable Reed-Solomon and convolutional coding forward error correction |
| [CUBESAT S-BAND TRANSMITTER (EnduroSat)](https://www.endurosat.com/products/cubesat-s-band-transmitter/) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| [CUBESAT X-BAND TRANSMITTER (EnduroSat)](https://www.endurosat.com/products/cubesat-x-band-transmitter/#scroll-to ) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| [Quasonix nanoTX](https://www.quasonix.com/products/transmitters/nanotx-transmitters/) | PCM/FM (legacy), SOQPSK-TG, [Multi-h CPM](https://www.quasonix.com/files/artm-tier-ii-waveform-itc-paper.pdf) | LDPC |
| [Innoflight SCR-100](https://www.innoflight.com/product-overview/scrs/scr-100/) (S-Band) | **Tx**: BPSK, QPSK, OQPSK; **Rx**: FSK/GMSK, FM/PCM | Conv. and R/S |
| [SWIFT Radios](https://www.tethers.com/swift-radios/)|B/Q/OQ/8-PSK, 16-APSK, PM/CPM, [SGLS-Ternary](https://www.researchgate.net/publication/3816361_Impact_of_baseband_filtering_on_the_SGLS_waveform)| Reed-Solomon + convolutional codes, BCH, LDPC|
| [CXS-1000 (S-Band)](https://www2.l3t.com/trf/pdf/datasheets/ML642_CXS1000.pdf) | **Tx**: [LPM (linear-period modulation)](https://yadi.sk/i/8GVJhJAkk_xWMA) 1.024 MHz s/c, [ranging](https://deepspace.jpl.nasa.gov/dsndocs/810-005/203/203C.pdf), BPSK, QPSK, OQPSK, UQPSK, user defined; **Rx**: BPSK, SGLS, [USB/STDN](https://yadi.sk/i/DW9PvZsf2f45MQ), ranging, [TDRSS](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20180003065.pdf) | - |
| [Syrlinks EWC27 X-band Transmitter](https://www.syrlinks.com/en/space/nano-satellite/x-band-transmitter-ewc27) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| Tethers Unlimited SWIFT-XTS | {8,16A,32A}PSK | - |
| JPL /Iris Transponder | BPSK bit sync | - |
| Canopus Systems | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| Ames Ka-band Tx | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| Tethers Unlimited | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| SWIFT-KTX | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |

We can make the following summary analyzing the considered matherials:

1. *S-band* includes both some of the "old" modulation schemes such as **PCM/FM**, **FSK** and **GMSK** and some of the modern schemes such as **M-APSK** (depends on a vendor's design mostly);

2. The most popular class of the modulation schemes are **M-PSK** (BPSK, QPSK, OQPSK) for both *S-* and *X-bands*.

3. One of the popular options of FEC is RSC \(Reed-Solomon convolutional\) concatenated codes. This relates to the [deep-space communication standartd](https://ipnpr.jpl.nasa.gov/progress_report/42-63/63H.PDF).

4. Only DVB-S2/S2X standard (**{Q,8,16A,32A}PSK**) is presented for the *Ka-band*;


## 3.2. Small suggestions about modulation schemes


### Why is BPSK one of the popular solutions?
 
Although QPSK has two twice as larger throughput \(2 bits per symbol\) and the same BER \(Bit-error ratio\) performance in AWGN \(Additive White Gaussian Noise\) channel, but, practically, BPSK is more robust due to its simplicity.

### Why is OQPSK used more than QPSK?

QPSK has possible phase jumps (zero crossings). When the signal is low-pass filtered (as is typical in a transmitter), these phase-shifts result in large amplitude fluctuations. One solution to avoid π radians phase jumps, is to use Offset QPSK \(OQPSK\).

![ Signal constellations of the conventional QPSK and OQPSK.](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%2812%29.png)

>*Fig. 3.2. Signal constellations of the conventional QPSK and OQPSK*
  
The sequence in the Q-branch is delayed by T/2, where T is channel symbol duration \(by 1 bit duration\). With this operation 180 degrees phase jumps are avoided and hence deep distortions in envelope will not occur.

OQPS and QPSK have the same theoretical BER performance. 

![BER](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%284%29.png)

> *Fig. 3.3. Bit error ratio curves in Rician flat fading channel.*

Moreover, [pulse shaping](https://en.wikipedia.org/wiki/Pulse_shaping) procedure is frequently applied. 

> Pulse shaping motivation provided in [Root Raised Cosine Filters & Pulse Shaping in Communication Systems.](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20120008631.pdf)

Comparison of the different waveforms in terms of spectral efficiency and BER performance is done in [\[2\]](https://ieeexplore.ieee.org/document/904973/).

### Why are M-QAM schemes not presented above?

M-QAM was replaced by the M-APSK in space communication (fig. 3.5).

![apsk](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/APSK_advantages.png)

> *Fig. 3.5. The main advantages of APSK in comparison with QAM (prepared according to ["Standard + Customized APSK Schemes For Satellite Transmission" By Donald Vanderweit, Agilent Technologies, Inc.](http://www.satmagazine.com/story.php?number=1051727556))*


## 3.3. Channel coding \(FEC\)

Very popular option of the FEC is [RSC \(Reed-Solomon convolutional\) concatenated codes](http://www.scholarpedia.org/article/Concatenated_codes#RS60). This relates to the [deep-space communication standartd](https://ipnpr.jpl.nasa.gov/progress_report/42-63/63H.PDF) (see also [Reed–Solomon error correction: Space transmission](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction#Space_transmission)).

However, since 2000-s modern error correction schemes such as [Turbo codes](http://www.scholarpedia.org/article/Turbo_code) and LDPC codes are used more widely in space communications \[10\].

Moreover the LDPC codes are the part of the DVB-S2/S2X standards (fig. 3.8)\[12\].

![](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/dvb_new.PNG)

> Fig. 3.7. The block schemes of DVB-S and DVB-S2/SX2.
 
There are a lot of [comparison issues](https://www.nt.tuwien.ac.at/wp-content/uploads/2016/10/DC2-16_Ch7_LDPC.pdf) of the Turbo codes and LDPC in the literature \[7, p. 614, 653\]\, [\[10\]](https://ieeexplore.ieee.org/document/4383367/), \[11\].

Briefly, the main tradeoff can be formulated as following:
* Turbo codes are the mest choice for the lower code rate (e.g. 1/6, 1/3, 1/2);
* LDPC codes are appropriate solution for the higher code rates (e.g. 3/4, 5/6, 7/8).

Additionally, LDPC does not require interleaving and puncturing procedures.


## References

\[1\]  Haykin S. Communication systems. – John Wiley & Sons, 2008. - p. 368, 402 

\[2\]  Hill, Terrance J. "A non-proprietary, constant envelope, variant of shaped offset QPSK \(SOQPSK\) for improved spectral containment and detection efficiency." MILCOM 2000. 21st Century Military Communications Conference Proceedings. Vol. 1. IEEE, 2000.

\[3\] Rice, M., Oliphant, T., & Mcintire, W. \(2007\). Estimation techniques for GMSK using linear detectors in satellite communications. IEEE Transactions on Aerospace and Electronic Systems, 43\(4\).

\[4\]  Li, Lifang, and M. K. Simon. "Performance of coded offset quadrature phase-shift keying \(OQPSK\) and MIL-STD shaped OQPSK \(SOQPSK\) with iterative decoding." Interplanetary Network Prog. Rep. 42 \(2004\).

\[5\] Proakis J. G. Digital communications. 1995 //McGraw-Hill, New York. – p. 126-128

\[6\] Anderson J. B., Aulin T., Sundberg C. E. Digital phase modulation. – Springer Science & Business Media, 2013. – p.49-50

\[7\] Moon Todd, K. Error correction coding: mathematical methods and algorithms. 2005 by John Wiley & Sons. ISBN 0-471-64800-0.

\[8\] J. Hagenauer, E. Offer, and L. Papke, Reed Solomon Codes and Their Applications. New York IEEE Press, 1994

\[9\] Tahir, Bashar, Stefan Schwarz, and Markus Rupp. "BER comparison between Convolutional, Turbo, LDPC, and Polar codes." Telecommunications \(ICT\), 2017 24th International Conference on. IEEE, 2017.

\[10\]  Andrews, Kenneth S., et al. "The development of turbo and LDPC codes for deep-space applications." Proceedings of the IEEE 95.11 \(2007\): 2142-2156.

\[11\] Hassan, A. E. S., Dessouky, M., Elazm, A. A., & Shokair, M. (2012). Evaluation of complexity versus performance for turbo code and LDPC under different code rates. In Proc. SPACOMM 2012: The fourth international conference on advances in satellite and space communication (pp. 93-98).

\[12\] Chen, P. H., Weng, J. J., Wang, C. H., & Chen, P. N. (2013). BCH code selection and iterative decoding for BCH and LDPC concatenated coding system. IEEE Communications Letters, 17(5), 980-983.
