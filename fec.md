# Modulation and coding \(FEC\)

## 4.1. Technical survey

The main features of existing equipment are shown in table 3.1

#### Table 3.1 Modulation and FEC of real cubesat S-band, X-band and Ka-band transceivers (some of examples are provided by [\[0\]](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160007683.pdf).)

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

![ModStat1](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/Modulations.png)
![ModStat2](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/Modulations1.png)

### M-PSK vs. M-FSK

Frequency modulation schemes is not usually used in satellite communications due to their relatively low spectral efficiency and difficulties with coherent detection.

**Tab. 3.2. Spectral efficient values \(bit/s/Hz\) for different modulation orders \[1\].** 

| **Modulation scheme / Modulation order** | 2 | 4 | 8 | 16 | 32 | 64 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| M-PSK | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 |
| M-FSK | 1 | 1 | 0.75 | 0.5 | 0.3125 | 0.1875 |

### QPSK vs. BPSK

The same BER \(Bit-error ratio\) performance in AWGN \(Additive White Gaussian Noise\) channel.
QPSK has two twice as larger throughput \(2 bits per symbol\).

| **Modulation** | **BPSK** | **QPSK** |
| :--- | :--- | :--- |
| Spectral efficiency | 0.5 | 1 |

Practically, BPSK is more robust due to its simplicity.

### QPSK vs. OQPSK

One solution to avoid π radians phase jumps (zero crossings), is to use Offset QPSK \(OQPSK\).

![ Signal constellations of the conventional QPSK and OQPSK.](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%2812%29.png)

>*Signal constellations of the conventional QPSK and OQPSK*
  
The sequence in the Q-branch is delayed by T/2, where T is channel symbol duration \(by 1 bit duration\). With this operation 180 degrees phase jumps are avoided and hence deep distortions in envelope will not occur.

The same theoretical BER performance. 

![BER](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%284%29.png)

### Shaped OQPSK vs. conventional OQPSK

Pulse shaping motivation \(cited by  [Root Raised Cosine Filters & Pulse Shaping in Communication Systems](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20120008631.pdf)\)

> This presentation briefly discusses application of the Root Raised Cosine \(RRC\) pulse shaping in the space telecommunication. Use of the RRC filtering \(i.e., pulse shaping\) is adopted in commercial communications, such as cellular technology, and used extensively. However, its use in space communication is still relatively new. This will possibly change as the crowding of the frequency spectrum used in the space communication becomes a problem. The two conflicting requirements in telecommunication are the demand for high data rates per channel \(or user\) and need for more channels, i.e., more users. Theoretically as the channel bandwidth is increased to provide higher data rates the number of channels allocated in a fixed spectrum must be reduced. Tackling these two conflicting requirements at the same time led to the development of the RRC filters. More channels with wider bandwidth might be tightly packed in the frequency spectrum achieving the desired goals. A link model with the RRC filters has been developed and simulated. Using 90% power Bandwidth \(BW\) measurement definition showed that the RRC filtering might improve spectrum efficiency by more than 75%. Furthermore using the matching RRC filters both in the transmitter and receiver provides the improved Bit Error Rate \(BER\) performance.

Impulse response of the filter:

![By Krishnavedala - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=15390555](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%2810%29.png)

>[*By Krishnavedala - Own work, CC BY-SA 3.0*](https://commons.wikimedia.org/w/index.php?curid=15390555)

With decreasing of the roll-off  factor $ \beta$ we have more compact frequency response \(more efficient usage of the spectrum\):    


![By Krishnavedala - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=15390895](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%283%29.png)

>[*By Krishnavedala - Own work, CC BY-SA 3.0*](https://commons.wikimedia.org/w/index.php?curid=15390895)
  
However, beta = 0 is the ideal case with difficulties of implementation in reality. Theoretically, decreasing of the roll-off factor increases ISI \(intersymbol interference\), however, in practice, it could be negligible.

Comparison of the different waveforms in terms of spectral efficiency and BER performance is done in [\[3\]](https://ieeexplore.ieee.org/document/904973/).

### Shaped OQPS vs. MSK/GMSK

Pulse Shaped OQPSK \(SOQPSK\) can be represented as continuous phase modulation \(CPM\) [\[4\]](https://pdfs.semanticscholar.org/f025/2fa31444fad6a5090527d73f87352137c9b8.pdf).

Minimum shift keying \(MSK\) is the partial case of the Continuous Phase Frequency Shift keying \(CPFSK\) and therefore of the CPM. MSK waveform can also be designed as OQPSK with the sinusoidal pulse shaping \[5, 6\]. 

![https://www.researchgate.net/publication/306035050\_A\_Notebook\_on\_Wireless\_Communication\_Systems/figures](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%2813%29.png)

>*https://www.researchgate.net/publication/306035050\_A\_Notebook\_on\_Wireless\_Communication\_Systems/figures*

However, it should be taken into account that MSK \(GMSK\) is the [partial case of the 2-FSK](https://www.quora.com/How-many-bits-per-symbol-are-transmitted-in-MSK). OQPSK is the quadrature modulation scheme and has the same throughput as QPSK or 4-QAM.

![http://www.rfwireless-world.com/Terminology/QPSK-vs-OQPSK-vs-pi-4QPSK.html](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%289%29.png)

>*http://www.rfwireless-world.com/Terminology/QPSK-vs-OQPSK-vs-pi-4QPSK.html*

## 4.3. Channel coding \(FEC\)

As we can see from table 3.1 very popular option of the FEC is [RSC \(Reed-Solomon convolutional\) concatenated codes](https://github.com/kirlf/CSP/blob/master/FEC/Conv%20codes%20idea%20extensions.md). This relates, probably, to the deep-space communication standartd. However, since 2000-s modern error correction schemes are used more widely in space communications.

![Codes Used by NASA Missions \[10\]](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%2814%29.png)

>*Codes Used by NASA Missions \[10\]*

### Turbo codes vs. LDPC

**LDPC disadvanges** \(cited by [\[10\]](https://ieeexplore.ieee.org/document/4383367/)\):

> Turbo codes were the first of the modern iteratively decoded codes to become practical. LDPC codes followed and have proven very versatile, but they have not replaced turbo codes, or even the traditional block and convolutional codes. LDPC codes are decoded on a parity check matrix, and this matrix grows larger as the code rate is decreased, making low-rate LDPC decoders more complex. In contrast, turbo codes are decoded on trellises, with one trellis section per information bit, corresponding to several code symbols. Hence turbo codes remain superior to LDPC codes at low rates. Iterative decoding, of either turbo or LDPC codes, remains complex relative to either Viterbi decoding of convolutional codes or to algebraic decoding techniques for Reed–Solomon and other block codes. When decoding complexity is constrained, as it is in highdata- rate applications, the traditional codes remain unbeaten. It is unknown if there are fundamental reasons why these different niches require different coding solutions. It is quite possible that good LDPC codes based on generator matrices will be found, and that low complexity LDPC decoding algorithms will be discovered. If so, perhaps LDPC codes will eventually solve all coding problems.

**Turbo codes disadvantages** \(cited by wikipedia article\)

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

# 4.4. MIMO / MISO / SIMO cases

Another way to improve reliability is using of space-time coding schemes such as Alamouti [12, 13]. 
In this case system model can be discribed as following figure:

<img src="https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/Cooperativeeng.png" alt="mimo" width="700" height="500">

*System model for the cooperative MIMO (channel unknown for the transmitter) case \[11\].*

Estimation of the capabilities of this scheme including cojunction with channel coding is done in [[11]]().

Additionally, reliability can be improved using combining schemes such as MRC (Maximum Ratio Combining) for the SIMO and channel known for the transmitter MISO system cases [[14]](https://www.researchgate.net/publication/272726183_BER_performance_comparison_of_MIMO_system_with_STBC_and_MRC_over_different_fading_channels). 

Theoretically, if the channel known for the transmitter and MIMO configuration is available, [DET (Dominant eigenmode transmission)]() as more powerful technique is also possible.

# 4.5. Multiple access

Short overview of the multiple access schemes of the LEO communication systems are provided in table 4.2:

#### Table 4.2 Multiple access schemes of different LEO communication systems

| Name of the system | Application | Multiple access scheme|
| :--- | :--- | :--- |
| [Iridium](https://www.researchgate.net/publication/3622510_Overview_of_IRIDIUM_satellite_network) | Voice  | FDMA / TDMA |
| [GLOBALSTAR](https://ieeexplore.ieee.org/document/224612/) | Voice, Data transmission |  Elements of CDMA, Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA) technology, combining with satellite Multiple Beam Antenna (MU) technology |
| [Teledesic](https://www.researchgate.net/publication/4672931_Architecture_of_the_TELEDESIC_satellite_system) | Data transmission | FDMA / asynchronous TDMA (ATDMA) / SDMA|
| [Orbcom ](https://www.ctu.cz/sites/default/files/cs/download/oznamene_typy_rozhrani/orbcomm-rozhrani_02_06_2010.pdf) | Data transmission | TDMA |
| [Messenger (Гонец)](http://lib.tssonline.ru/articles2/sputnik/mnogofunktsionalnaya-sistema-personalnoy-sputnikovoy-svyazi-gonets-d1m-sostoyanie-i-perspektivy-razvitiya.-multifunctional-system-for-personal-satellite-communication-gonets-d1m-current-state-and-prospects) | Data transmission | TDMA |
| [CDMA communication system performance for a constellation of CubeSats around the Moon \(IEEE paper\)](https://ieeexplore.ieee.org/document/7500710/) | Data transmission | CDMA |


Moreover, comparison of the W-CDMA and OFDM/TDMA is done in [[15]](https://www.researchgate.net/profile/P_Takis_Mathiopoulos/publication/3344159_A_comparison_study_of_the_uplink_performance_of_W-CDMA_and_OFDM_for_mobile_multimedia_communications_via_LEO_satellites/links/545a3ab80cf2bccc49132882.pdf).

Interesting and comprehensive survey of the multiple access schemes for satellites is provided in ["Multiple Access Techniques: FDMA, TDMA & CDMA"](http://www.atlantarf.com/Downloads.php) presentation from Atlanta RF. For example, disadvantages of the CDMA technology are discribed:

>CDMA Disadvantages:

>1.CDMA is an interference-limited system: As the number of users increases, the overall quality of service decreases since RF signals from undesired Users appear as higher (additive) noise levels at the receiver.

>2.Self-jamming: Arises when the spreading sequences of different users are not exactly orthogonal; hence, in the despreading of a particular PN code, non-zero contributions to the receiver decision statistic for a desired user arise from the transmissions of other users in the system.

>3.Near and Far effect: The near-far effect occurs at a CDMA receiver if an undesired user transmits a high detected RF power, as compared to the desired user, usually because of distance, shadowing and multipath fading. To combat the near-far effect, power control is implemented at a central control (e.g: the base station) by rapidly sampling the radio signal strength indicator levels of each (mobile) User, and then sending a power change command (to increase/decrease their transmitted RF power) over the forward radio link. In other words, the nearby transmitters are assigned a lower transmit power level than the far away transmitters.

>Result: Extra hardware complexity to implement power adjustment (Open-loop method or Closed-loop method).

This indirectly explains why [CDMA is not so popular](https://www.quora.com/How-does-CDMA-operate-on-satellite-communication) in the real communication systems.

## References

\[0\] Wong, Y. F., Kegege, O., Schaire, S. H., Bussey, G., Altunc, S., Zhang, Y., & Chitra, P. (2016). An optimum space-to-ground communication concept for CubeSat platform utilizing NASA space network and near earth network.

\[1\]  Haykin S. Communication systems. – John Wiley & Sons, 2008. - p. 368, 402 

\[2\] Rice, M., Oliphant, T., & Mcintire, W. \(2007\). Estimation techniques for GMSK using linear detectors in satellite communications. IEEE Transactions on Aerospace and Electronic Systems, 43\(4\).

\[3\]  Hill, Terrance J. "A non-proprietary, constant envelope, variant of shaped offset QPSK \(SOQPSK\) for improved spectral containment and detection efficiency." MILCOM 2000. 21st Century Military Communications Conference Proceedings. Vol. 1. IEEE, 2000.

\[4\]  Li, Lifang, and M. K. Simon. "Performance of coded offset quadrature phase-shift keying \(OQPSK\) and MIL-STD shaped OQPSK \(SOQPSK\) with iterative decoding." Interplanetary Network Prog. Rep. 42 \(2004\).

\[5\] Proakis J. G. Digital communications. 1995 //McGraw-Hill, New York. – p. 126-128

\[6\] Anderson J. B., Aulin T., Sundberg C. E. Digital phase modulation. – Springer Science & Business Media, 2013. – p.49-50

\[7\] Moon Todd, K. Error correction coding: mathematical methods and algorithms. 2005 by John Wiley & Sons. ISBN 0-471-64800-0.

\[8\] J. Hagenauer, E. Offer, and L. Papke, Reed Solomon Codes and Their Applications. New York IEEE Press, 1994

\[9\] Tahir, Bashar, Stefan Schwarz, and Markus Rupp. "BER comparison between Convolutional, Turbo, LDPC, and Polar codes." Telecommunications \(ICT\), 2017 24th International Conference on. IEEE, 2017.

\[10\]  Andrews, Kenneth S., et al. "The development of turbo and LDPC codes for deep-space applications." Proceedings of the IEEE 95.11 \(2007\): 2142-2156.

\[11\] Gibalina, Z. S., Fadeev, V. A., Korsukova, K. A., Hennhöfer, M., & Haardt, M. (2018, July). Estimation of capabilities of cooperative CubeSat systems based on Alamouti transmission scheme. In 2018Systems of Signal Synchronization, Generating and Processing in Telecommunications (SYNCHROINFO) (pp. 1-6). IEEE.

\[12\] Arapoglou, P. D., Liolis, K., Bertinelli, M., Panagopoulos, A., Cottis, P., & De Gaudenzi, R. (2011). MIMO over satellite: A review. IEEE communications surveys & tutorials, 13(1), 27-51.

\[13\] Kyröläinen, J., Hulkkonen, A., Ylitalo, J., Byman, A., Shankar, B., Arapoglou, P. D., & Grotz, J. (2014). Applicability of MIMO to satellite communications. International Journal of Satellite Communications and Networking, 32(4), 343-357.

\[14\] Tiwari, K., & Saini, D. S. (2014, December). BER performance comparison of MIMO system with STBC and MRC over different fading channels. In High Performance Computing and Applications (ICHPCA), 2014 International Conference on (pp. 1-6). IEEE.

\[15\] Papathanassiou, A., Salkintzis, A. K., & Mathiopoulos, P. T. (2001). A comparison study of the uplink performance of W-CDMA and OFDM for mobile multimedia communications via LEO satellites. IEEE Personal Communications, 8(3), 35-43.
