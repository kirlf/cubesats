# Multiple access (in progress)

Short overview of the multiple access schemes of the LEO communication systems are provided in table 1:

#### Table 1 Multiple access schemes of different LEO communication systems

| Name of the system | Application | Multiple access scheme|
| :--- | :--- | :--- |
| [Iridium](https://www.researchgate.net/publication/3622510_Overview_of_IRIDIUM_satellite_network) | Voice  | FDMA / TDMA |
| [GLOBALSTAR](https://ieeexplore.ieee.org/document/224612/) | Voice, Data transmission |  Elements of CDMA, Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA) technology, combining with satellite Multiple Beam Antenna (MU) technology |
| [Teledesic](https://www.researchgate.net/publication/4672931_Architecture_of_the_TELEDESIC_satellite_system) | Data transmission | FDMA / asynchronous TDMA (ATDMA) / SDMA|
| [Orbcom ](https://www.ctu.cz/sites/default/files/cs/download/oznamene_typy_rozhrani/orbcomm-rozhrani_02_06_2010.pdf) | Data transmission | TDMA |
| [Messenger (Гонец)](http://lib.tssonline.ru/articles2/sputnik/mnogofunktsionalnaya-sistema-personalnoy-sputnikovoy-svyazi-gonets-d1m-sostoyanie-i-perspektivy-razvitiya.-multifunctional-system-for-personal-satellite-communication-gonets-d1m-current-state-and-prospects) | Data transmission | TDMA |
| [CDMA communication system performance for a constellation of CubeSats around the Moon \(IEEE paper\)](https://ieeexplore.ieee.org/document/7500710/) | Data transmission | CDMA |


Moreover, comparison of the W-CDMA and OFDM/TDMA is done in [\[1\]](https://www.researchgate.net/profile/P_Takis_Mathiopoulos/publication/3344159_A_comparison_study_of_the_uplink_performance_of_W-CDMA_and_OFDM_for_mobile_multimedia_communications_via_LEO_satellites/links/545a3ab80cf2bccc49132882.pdf). OFDM is also proposed in [\[2\]](https://pdfs.semanticscholar.org/49b2/a7f59ddc76f20b5abb5dcff7d29b9faa9641.pdf).

Interesting and comprehensive survey of the multiple access schemes for satellites is provided in ["Multiple Access Techniques: FDMA, TDMA & CDMA"](http://www.atlantarf.com/Downloads.php) presentation from Atlanta RF. For example, disadvantages of the CDMA technology are discribed:

>**CDMA Disadvantages**:
>
>1. ***CDMA is an interference-limited system***: As the number of users increases, the overall quality of service decreases since RF signals from undesired Users appear as higher (additive) noise levels at the receiver.
>
>2. ***Self-jamming***: Arises when the spreading sequences of different users are not exactly orthogonal; hence, in the despreading of a particular PN code, non-zero contributions to the receiver decision statistic for a desired user arise from the transmissions of other users in the system.
>
>3. ***Near and Far effect***: The near-far effect occurs at a CDMA receiver if an undesired user transmits a high detected RF power, as compared to the desired user, usually because of distance, shadowing and multipath fading. To combat the near-far effect, power control is implemented at a central control (e.g: the base station) by rapidly sampling the radio signal strength indicator levels of each (mobile) User, and then sending a power change command (to increase/decrease their transmitted RF power) over the forward radio link. In other words, the nearby transmitters are assigned a lower transmit power level than the far away transmitters.
>
>**Result**: Extra hardware complexity to implement power adjustment (Open-loop method or Closed-loop method).

This indirectly explains why [CDMA is not so popular](https://www.quora.com/How-does-CDMA-operate-on-satellite-communication) in the real communication systems.

## References

\[1\] Papathanassiou, A., Salkintzis, A. K., & Mathiopoulos, P. T. (2001). A comparison study of the uplink performance of W-CDMA and OFDM for mobile multimedia communications via LEO satellites. IEEE Personal Communications, 8(3), 35-43.

\[2\] Na, Z., Guan, Q., Fu, C., Cui, Y., & Guo, Q. (2013). Channel model and throughput analysis for LEO OFDM satellite communication system. International Journal of Future Generation Communication and Networking, 6(6), 109-122.
