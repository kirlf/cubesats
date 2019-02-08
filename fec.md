# Modulation and coding \(FEC\)

## 4.1. Technical survey

The main features of existing equipment are shown in table 3.1

#### Table 3.1 Modulation and FEC of real cubesat S-band, X-band and Ka-band transceivers (some of examples are provided by [ Wong, Y. F., Kegege, O., Schaire, S. H., Bussey, G., Altunc, S., Zhang, Y., & Chitra, P. (2016). An optimum space-to-ground communication concept for CubeSat platform utilizing NASA space network and near earth network.](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160007683.pdf))

| Title | Modulation | FEC |
| :--- | :--- | :--- |
| [ NanoCom SR2000](https://gomspace.com/UserFiles/Subsystems/datasheet/gs-ds-nanocom-sr2000-10.pdf) | Filtered QPSK \( Square root raised cosine filter, 𝛼 = 0.2\) | Concatenated coding: convolutional code plus Reed-Solomon \[C\(7, ½\) and RS \(255, 223\), interleaving depth 𝐿 = 8\] |
| [ISIS TXS High Data Rate S-Band Transmitter](https://www.cubesatshop.com/product/isis-txs-s-band-transmitter/) | OQPSK \( Pulse shaping: Square Root Raised Cosine, Roll-off 0.5, 0.35\) | Concatenated Reed Solomon and Convolutional coding \[C\(7, ½\) and RS \(255, 223\)\] |
| [ISIS TXS High Data Rate S-Band Transmitter](https://www.cubesatshop.com/product/isis-txs-s-band-transmitter/) | DQPSK | TURBO code, rate =0.489 |
| [S Band Transceiver for Small Satellites \( IQ wireless GmbH\)](http://www.iq-wireless.com/images/pdf/SLINK-Datasheet.pdf) | BPSK/QPSK/8PSK/QAM16 | Convolutional code, r=0.5 / 0.75 |
| [Full-duplex Low-power S-band Transceiver \(Nano Avionics\)](https://n-avionics.com/cubesat-components/communication-systems/cubesat-s-band-transceiver/) | GMSK modulation \(BT=0.35\) | Configurable Reed-Solomon and convolutional coding forward error correction |
| [CDMA communication system performance for a constellation of CubeSats around the Moon \(IEEE paper\)](https://ieeexplore.ieee.org/document/7500710/) | filtered offset QPSK with phase modulation \(a CCSDS standard\) \(OQPSK/PM\) | LDPC r=0.5 |
| [CUBESAT S-BAND TRANSMITTER (EnduroSat)](https://www.endurosat.com/products/cubesat-s-band-transmitter/) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| [CUBESAT X-BAND TRANSMITTER (EnduroSat)](https://www.endurosat.com/products/cubesat-x-band-transmitter/#scroll-to ) | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| Innoflight SCR-100 | BPSK, QPSK, OQPSK, GMSK, FM/PCM | Conv. and R/S |
|Tethers Unlimited SWIFT-SLX|BPSK| - |
| L3 Cadet S-Band Tx (CXS-1000) | BPSK, QPSK, SOQPSK, SGLS M/FSK | - |
| Nimitz Radio Sband Tx/UHF Rx | Uplink FSK, GFSK; Downlink BPSK | - |
| Quasonix nanoTX | PCM/FM, SOQPSKTG, Multi-h CPM, BPSK, QPSK, OQPSK, UQPSK | - |
| MHX-2420 | FSK | - |
| LASP/GSFC Xband Radio | BPSK/OQPSK |  R/S and Conv.|
| Syrlinks/X-band Transmitter | BPSK/OQPSK |  R/S and Conv |
| Marshall X-band Tx | BPSK/OQPSK | LDPC 7/8 |
| Tethers Unlimited SWIFT-XTS | {8,16A,32A}PSK | - |
| JPL /Iris Transponder | BPSK bit sync | - |
| Canopus Systems | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| Ames Ka-band Tx | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| Tethers Unlimited | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |
| SWIFT-KTX | {Q,8,16A,32A}PSK | LDPC Concatenated with BCH |

We can make the following summary analyzing the considered matherials:

1. *S-band* includes both some of the "old" modulation schemes such as **PCM/FM**, **FSK** and **GMSK** and some of the modern schemes such as **M-APSK** (depends on a vendor's design mostly);

2. The most popular class of the modulation schemes are **M-PSK** (BPSK, QPSK, OQPSK) for both *S-* and *X-bands*.

3. Only DVB-S2/S2X standard (**{Q,8,16A,32A}PSK**) is presented for the *Ka-band*;

4. The following options are used for the Forward Error Correction (mostly): **Reed-Solomon** codes concatenated with **convolutional** codes and **LDPC** (concatenated with **BCH** in DVB-S2/S2X) codes.

<img alt="ModStat1" src="https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/Modulations.png" width="600"/>
<img alt="ModStat2" src="https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/Modulations2.png" width="600"/>

> *Fig. 3.1. The diagrams of the modulation schemes usage*.

## 4.2. Small suggestions about modulation schemes

###  Why M-PSK replaced M-FSK?

Higher order frequency modulation schemes are not usually used in satellite communications due to their relatively low spectral efficiency and difficulties with coherent detection.

**Tab. 3.2. Spectral efficient values \(bit/s/Hz\) for different modulation orders \[1\].** 

| **Modulation scheme / Modulation order** | 2 | 4 | 8 | 16 | 32 | 64 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| M-PSK | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 |
| M-FSK | 1 | 1 | 0.75 | 0.5 | 0.3125 | 0.1875 |

### Why BPSK is the one of the popular solutions?
 
Although QPSK has two twice as larger throughput \(2 bits per symbol\) and the same BER \(Bit-error ratio\) performance in AWGN \(Additive White Gaussian Noise\) channel, but, practically, BPSK is more robust due to its simplicity.

### Why OQPSK is used more than QPSK?

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

### Why GMSK was replaced in modern solutions?

GMSK was a good solution for the satellite communications \[3\] for a long time due to its promissing spectral parameters (fig. 3.4).

![PSD-MSSK](https://upload.wikimedia.org/wikipedia/commons/b/b2/PSD_MSK_PSK.png)
![PSD-GMSK](https://upload.wikimedia.org/wikipedia/commons/5/5e/GMSK_PSD.png)

> *Fig. 3.4. Power-spectral densities of the BPSK, QPSK, MSK, GMSK.*

In other hand, MSK waveform can also be designed as OQPSK (i.e. in [I/Q manner](https://www.researchgate.net/publication/306035050\_A\_Notebook\_on\_Wireless\_Communication\_Systems/figures)) with the sinusoidal pulse shaping \[5, 6\].

> **NOTE**:
> * Pulse Shaped OQPSK \(SOQPSK\) can be represented as continuous phase modulation \(CPM\) [\[4\]](https://pdfs.semanticscholar.org/f025/2fa31444fad6a5090527d73f87352137c9b8.pdf).
> * Minimum shift keying \(MSK\) is the partial case of the Continuous Phase Frequency Shift keying \(CPFSK\) and therefore of the CPM.

Moreover, theoretically, the spectral parameters of the SOQPSK can be optimized as well as in GMSK case with a good selection of the filter for the pulse shaping.  

However, it should be taken into account that MSK \(GMSK\) is the [partial case of the 2-FSK](https://www.quora.com/How-many-bits-per-symbol-are-transmitted-in-MSK). OQPSK is the [quadrature modulation](http://www.rfwireless-world.com/Terminology/QPSK-vs-OQPSK-vs-pi-4QPSK.html) scheme and has the same throughput as QPSK or 4-QAM.

### Why M-QAM schemes are not presented above?

M-QAM was replaced by the M-APSK in space communication due to (cited by the [Standard + Customized APSK Schemes For Satellite Transmission By Donald Vanderweit, Agilent Technologies, Inc.](http://www.satmagazine.com/story.php?number=1051727556)):

> Like QAM, APSK gives more bits per symbol than QPSK, allowing more data to be sent in the same bandwidth. But unlike QAM, the states are configured in rings, with the intent that symbol points in a given ring will react the same way to compression. This has two positive effects. The first is that compression of the signal tends to have less of an effect on the spacing between states (sometimes referred to as the “Euclidean distance”), and so the states are easier to distinguish from each other during demodulation.
>
> \[...\]
>
> The second advantage of APSK is that it lends itself to pre-distortion. By varying the space between rings before transmission, it is possible to pre-distort the signal in a way that counteracts the effects of transmission distortion and thereby gets a better output. In static pre-distortion, the spacing between rings is set and fixed. In dynamic pre-distortion, the signal received from the satellite is monitored and measured, and the results are fed back to the pre-distortion circuitry for adjustment. Because of the presence of Automatic Level Control (ALC) circuitry in the transmitter and the relatively stable operation of the satellite amplifier, static pre-distortion can give good results over long periods of time.
>
> Peak to Average Power Ratio (PAPR): Another consideration is Peak-to-Average Power Ratio (PAPR). This metric gives the ratio of the highest power the amplifier will be expected to send to the average power. This ratio is important to designers because the amount of data that can be sent is proportional to the average power, but the size of the amplifier needed for a given format depends on the peak power. The ideal PAPR would be 1:1, and this is in fact the ratio for QPSK. All of the points in the constellation are the same distance from the origin, and therefore require the same power to transmit. For more complicated schemes, APSK has an advantage over QAM: the 32-APSK scheme shown above has a PAPR of approx. 1.57, compared to 1.7 for 32-QAM. By adjusting the spacing between rings and other factors, a designer can reach a balance between lower PAPR and better resistance to distortion.


## 4.3. Channel coding \(FEC\)

As we can see from table 3.1 very popular option of the FEC is [RSC \(Reed-Solomon convolutional\) concatenated codes](https://github.com/kirlf/CSP/blob/master/FEC/Conv%20codes%20idea%20extensions.md). This relates, probably, to the deep-space communication standartd. However, since 2000-s modern error correction schemes are used more widely in space communications.

![Codes Used by NASA Missions \[10\]](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%2814%29.png)

>*Fig. 3.5. Codes Used by NASA Missions \[10\]*

### Turbo codes vs. LDPC

**LDPC disadvanges** \(cited by [\[10\]](https://ieeexplore.ieee.org/document/4383367/)\):

> Turbo codes were the first of the modern iteratively decoded codes to become practical. LDPC codes followed and have proven very versatile, but they have not replaced turbo codes, or even the traditional block and convolutional codes. LDPC codes are decoded on a parity check matrix, and this matrix grows larger as the code rate is decreased, making low-rate LDPC decoders more complex. In contrast, turbo codes are decoded on trellises, with one trellis section per information bit, corresponding to several code symbols. Hence turbo codes remain superior to LDPC codes at low rates. Iterative decoding, of either turbo or LDPC codes, remains complex relative to either Viterbi decoding of convolutional codes or to algebraic decoding techniques for Reed–Solomon and other block codes. When decoding complexity is constrained, as it is in highdata- rate applications, the traditional codes remain unbeaten. It is unknown if there are fundamental reasons why these different niches require different coding solutions. It is quite possible that good LDPC codes based on generator matrices will be found, and that low complexity LDPC decoding algorithms will be discovered. If so, perhaps LDPC codes will eventually solve all coding problems.

In other hand,  BER performance of the Turbo codes are influenced by low weight codes  limitation \[7 , p.614\]. This phenomenon indirectly means that for decreasing of the BER in fixed SNR only decreasing of the code rate \(and hence of the net bit rate\) can be used.

LDPC codes have no limitations of minimum distance \(cited by \[7, p. 653\]\):

> LDPC codes have excellent distance properties. Gallager showed that for random LDPC codes, the minimum distance dmin between codewords increases with N \[code word length\] when column and row weights are held fixed \[ 112, p. 51\], that is, as they become increasingly sparse. Sequences of LDPC codes as N -&gt; inf have been proved to reach channel capacity \[217\].

That indirectly means that LDPC codes may be more efficient on relatively large code rates \(e.g. 3/4, 5/6, 7/8\) than Turbo codes.

In the [following reference](https://www.nt.tuwien.ac.at/wp-content/uploads/2016/10/DC2-16_Ch7_LDPC.pdf) comparison formulated as:

> LDPC codes have certain advantages over turbo codes: 
>
> • They tend to have a better block error performance, and a better performance on bursty channels. 
>
> • They are more amenable to high rates, and in fact can be designed for almost any rate and blocklength. \(In contrast, the rate of turbo codes is usually adjusted by means of a puncturing scheme, which necessitates an additional design step.\) 
>
> • Their error floor tends to occur at a lower BER. 
>
> • The encoder and decoder do not require interleavers. 
>
> • A single LDPC code can be universally good for a collection of channels. 
>
> • There exist iterative LDPC decoding algorithms that are easy to implement, have moderate complexity \(which scales linearly with the blocklength\), and are parallelizable in hardware. In particular, LDPC decoding using the belief propagation \(sum-product\) algorithm tends to be less complex than turbo decoding using the BCJR algorithm. 
>
> • LDPC decoders inherently check if a codeword satisfying the check equations has been found, and otherwise declare a decoding failure. \(In contrast, turbo decoders usually need to perform additional operations to compute a stopping criterion, and even then it is not clear if the decoding result corresponds to a codeword satisfying the check equations.\) 
>
> LDPC codes also have certain disadvantages relative to turbo codes: 
>
> • In general, the encoding complexity is higher than for turbo codes. \(However, there are special LDPC code constructions with low encoding complexity.\) 
>
> • Iterative LDPC decoding typically requires many more iterations than iterative turbo decoding, which may lead to a higher latency. \(The complexity per iteration is much lower, though.\)

The interesting research about LDPC-BCH codes is done in \[11\].

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

\[11\] Chen, P. H., Weng, J. J., Wang, C. H., & Chen, P. N. (2013). BCH code selection and iterative decoding for BCH and LDPC concatenated coding system. IEEE Communications Letters, 17(5), 980-983.
