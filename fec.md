## Table of contents

### Surveys
1. [Statistical channel model survey](https://github.com/kirlf/cubesats/blob/master/statistical_model.md)
2. Modulation and coding \(FEC\) survey

### Tutorials (Python)
1. [Sat-to-Ground (and vice versa) link budget calculation](https://nbviewer.jupyter.org/github/kirlf/cubesats/blob/master/LinkBudget/LB.ipynb)
2. [Intersatellite Link budget calculation (wireless optical)](https://nbviewer.jupyter.org/github/kirlf/cubesats/blob/master/Optical-ISL-LB.ipynb)

# Survey of modulation and coding schemes for application in CubeSat systems (afterwords)

**Table 1. Modulation and FEC of real cubesat S-band, X-band and Ka-band transceivers**

| Title | Modulation | FEC |
| :--- | :--- | :--- |
| [ISIS TXS High Data Rate S-Band Transmitter](https://www.cubesatshop.com/product/isis-txs-s-band-transmitter/) | [BPSK](https://en.wikipedia.org/wiki/Phase-shift_keying#Binary_phase-shift_keying_(BPSK)), [OQPSK](https://en.wikipedia.org/wiki/Phase-shift_keying#Offset_QPSK_(OQPSK)) \([Pulse shaping](https://en.wikipedia.org/wiki/Pulse_shaping): Square [Root Raised Cosine](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20120008631.pdf), Roll-off 0.5, 0.35\) | [Concatenated coding](http://www.scholarpedia.org/article/Concatenated_codes#RS60): [Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction#Space_transmission) and [Convolutional coding](https://en.wikipedia.org/wiki/Convolutional_code): RS (255, 223) and CC (constrain length = 7, code rate = 1/2)|
| [ NanoCom SR2000](https://gomspace.com/UserFiles/Subsystems/datasheet/gs-ds-nanocom-sr2000-230.pdf) | Filtered [QPSK](https://en.wikipedia.org/wiki/Phase-shift_keying#Quadrature_phase-shift_keying_(QPSK)) (Square root raised cosine filter, 𝛼 = 0.2) |  Convolutional code (7, 1/2) + Reed-Solomon code (255, 223), interleaving depth 𝐿 = 8 |
| [SWIFT Radios](https://www.tethers.com/swift-radios/)|B/Q/OQ/8-PSK, [16-APSK](https://en.wikipedia.org/wiki/Amplitude_and_phase-shift_keying), PM/CPM, [SGLS-Ternary](https://www.researchgate.net/publication/3816361_Impact_of_baseband_filtering_on_the_SGLS_waveform)| Reed-Solomon + convolutional codes, BCH, LDPC|
| [Full-duplex Low-power S-band Transceiver \(Nano Avionics\)](https://n-avionics.com/cubesat-components/communication-systems/cubesat-s-band-transceiver/) | [GMSK](https://en.wikipedia.org/wiki/Minimum-shift_keying#Gaussian_minimum-shift_keying) \(BT=0.35\) | Configurable Reed-Solomon and convolutional coding forward error correction |
| [Innoflight SCR-100 (S-Band)](https://www.innoflight.com/product-overview/scrs/scr-100/)| **Tx**: BPSK, QPSK, OQPSK; **Rx**: FSK/GMSK, FM/PCM | Conv. and R/S |
| [Iris V2.1 CubeSat Deep Space Transponder](https://www.jpl.nasa.gov/cubesat/pdf/Brochure_IrisV2.1_201611-URS_Approved_CL16-5469.pdf) | [PM](https://en.wikipedia.org/wiki/Phase_modulation)/PSK/[NRZ](https://en.wikipedia.org/wiki/Non-return-to-zero) | Convolutional (7, 1/2); [Manchester, Bi-Phase, and bypass (NRZ)](http://ww1.microchip.com/downloads/en/AppNotes/Atmel-9164-Manchester-Coding-Basics_Application-Note.pdf); Reed Solomon (255,223); [Turbo](http://www.scholarpedia.org/article/Turbo_code) (1/2, 1/3, 1/6) block size 8920 bits |
| [CDMA communication system performance for a constellation of CubeSats around the Moon \(IEEE paper\)](https://ieeexplore.ieee.org/document/7500710/) | filtered OQPSK with phase modulation \(a [CCSDS](https://en.wikipedia.org/wiki/Consultative_Committee_for_Space_Data_Systems) standard\) \(OQPSK/PM\) | LDPC r=0.5 |
| [Quasonix nanoTX](https://www.quasonix.com/products/transmitters/nanotx-transmitters/) | [PCM](https://en.wikipedia.org/wiki/Pulse-code_modulation)/[FM](https://en.wikipedia.org/wiki/Frequency_modulation) (legacy), SOQPSK-TG, [Multi-h CPM](https://www.quasonix.com/files/artm-tier-ii-waveform-itc-paper.pdf) | LDPC |
| [CXS-1000 (S-Band)](https://www2.l3t.com/trf/pdf/datasheets/ML642_CXS1000.pdf) | **Tx**: [LPM (linear-period modulation)](https://yadi.sk/i/8GVJhJAkk_xWMA) 1.024 MHz s/c, [ranging](https://deepspace.jpl.nasa.gov/dsndocs/810-005/203/203C.pdf), BPSK, QPSK, OQPSK, UQPSK, user defined; **Rx**: BPSK, SGLS, [USB/STDN](https://yadi.sk/i/DW9PvZsf2f45MQ), ranging, [TDRSS](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20180003065.pdf) | - |
| [S Band Transceiver for Small Satellites \( IQ wireless GmbH\)](https://www.iq-spacecom.com/images/downloads/SLINK-PHY-datasheet.pdf) | **Uplink**: BPSK; **Downlink**: QPSK | -|
| [CUBESAT S-BAND TRANSMITTER (EnduroSat)](https://www.endurosat.com/products/cubesat-s-band-transmitter/) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| [CUBESAT X-BAND TRANSMITTER (EnduroSat)](https://www.endurosat.com/products/cubesat-x-band-transmitter/#scroll-to ) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| [Syrlinks EWC27 X-band Transmitter](https://www.syrlinks.com/en/space/nano-satellite/x-band-transmitter-ewc27) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| [Canopus Systems, Ames Ka-band Tx, Tethers Unlimited](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160010584.pdf) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |

We can make the following summary analyzing the considered matherials:

1. The most popular class of the modulation schemes are **M-PSK** (BPSK, QPSK, OQPSK). 

2. One of the popular options of FEC is RSC \(Reed-Solomon convolutional\) concatenated codes. This relates to the [deep-space communication standartd](https://ipnpr.jpl.nasa.gov/progress_report/42-63/63H.PDF).

3. DVB-S2/S2X standard (**{Q,8,16A,32A}PSK** and **LDPC + BCH codes**) is also popular solution.

4. Some vendors provide also "legacy" types such as **PCM/FM**, **FSK** and **GMSK**.


### Why is BPSK one of the popular solutions?
 
Although QPSK has two twice as larger throughput \(2 bits per symbol\) and the same BER \(Bit-error ratio\) performance in AWGN \(Additive White Gaussian Noise\) channel, but, practically, BPSK is more robust due to its simplicity.
