# 2. Link Budget calculation

## 2.1. Main formulas

Before we start considering even different types of modulation it is extremely valuable to know what SNR values can be expected on the receiver side. In fact, we can calculate the SNR as:


$$
 \frac S N = \frac {PtGtGrLLadd} {kTnoiseBnoise}  \qquad(2.1)
$$


Where **S** is the received power,  **N** is the total termal noise power \(relates to noise spectral density $$N_0 = kT_{noise}$$  and double-sided white noise variance $$\sigma^2 = N_0/2$$\),  _Pt_ is the transmitted power, **Gt** and** Gr** are antenna gains on transmitter and receiver sides respectively,** **_**L**_ is path losses,** Ladd **_is additional losses \(margin\),_ **k** _is  Boltzmann constant, _**Tnoise** is equivalent noise temperature and **Bnoise** is noise bandwidth. Assume that all of losses in RF \(fiders, cabels etc.\) part are annihilated by related gains.

Path losses can be estimated by Friis formula:


$$
 L = 20 lg \frac {λ}{4πd}  \qquad (2.2)
$$


where **λ \(**relates to the carrier frequency** **$$f_0 = c / \lambda$$\) is wave length and **d** is distance between satellite and ground station. According to \[12\] noise bandwidth **Bnoise** can be estimated roughly as _1.1B_ where  **B** is receiver bandwidth.

Equivalent noise temperature is not the physical temperature of an antenna. It is equal to the temperature of a resistor, which would have the same thermal noise power in the given frequency band. This parameter can be represented as:


$$
 Tnoise = Ta + Te \qquad (2.3)
$$


where _**Ta**_ is sum of antenna losses and sky noise and _**Te**_ is the receiver noise temperature. Additionally, receiver noise temperature can be calculated by following formula:


$$
 Te = T_0(Fsys − 1) \qquad (2.4)
$$


where **T0** is equal to 290K and **Fsys** is noise factor which can be estimated by noise figure \(**NF**\) of receive antenna:


$$
 Fsys = 10^{NF/10} \qquad (2.5)
$$


Let us provide some parameters summary:

1. **Initial point:** carrier frequency$$f_0$$, distance $$d$$;
2. **Equipment dependent parameters \(ajustable\)**: transmitted power $$P_t$$, receiver bandwidth$$B$$ ;
3. **Reference data: **antenna gains $$G_t$$** **and** **$$G_r$$, sum of antenna losses and sky noise $$T_a$$, noise figure $$NF$$.

## 2.2. Considered equipment

In fact, we use common example of ground station such as IC-910H \[13\] or ISIS ground station \[14\] however we can estimate some parameter of transceivers of real space communication systems. Fortunately, a lot of this information is open and avail- able on official sites available \[15\], \[16\],\[17\] \(table 2.1\).

These parameters can be used for calculation of up-link link budget.

For down-link estimation real example of CubeSat transceivers such as NanoCom AX100 \[26\] may be used. Additionally, as an example of CubeSat UHF/VHF antenna omnidirectional NanoCom ANT430 can be considered \[26\].

![](/assets/transceiver.png)

_Fig. 2.1: NanoCom AX100 by GomSpace company._

![](/assets/antenna1.png)

_Fig. 2.2: NanoCom ANT430 by GomSpace company._

For lager possible bandwidth 2.4GHz range also should be considered. For this range patch-antenna NanoCom ANT2000 and S-band transceiver NanoCom SR2000 are available \[26\].

![](/assets/transceiver2.png)

_Fig. 2.3: NanoCom SR2000 by GomSpace company._

![](/assets/antenna2.png)

_Fig. 2.4: ANT2000 by GomSpace company._

To sum up, main parameters for link budget calculation are maintained in table 2.4.

## 2.3. Additional losses

Additional loses due to scattering in atmosphere can be compute by \[9\]. Attenuations due to hydrometeors and other additional loses can be evaluated by \[11\]. Fortunately, for ranges smaller than 10 GHz the losses are smaller than 1 dB.

![](/assets/atten1.png)_Fig. 2.5: _ Specific attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[9\].

![](/assets/atten2.png)_Fig. 2.5: _  Zenith attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[9\].

