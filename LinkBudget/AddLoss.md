## 1.2. Additional losses

According to \[1, p.88-96\] additional losses include:

* loss due to refraction and inaccuracy of antenna pointing \(Antenna Beam Loss\);
* phase effects in the atmosphere;
* loss due to inconsistency of polarization of antennas;
* attenuations due to hydrometeors.

### 1.2.1. Loss due to refraction and inaccuracy of antenna pointing 

Depends on characteristics of the certain antenna:

$$
L_b = 10log_{10}(1+ (2\theta/\theta_{0.5})^2) \qquad (1.7)
$$

where $ \theta$ is the beamwidth and $\theta_{0.5}$ is the halfpowered beamwidth \(fig. 1.2.1\).

![Fig. 2.1 Antenna gain pattern  \[2\]](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%288%29.png)
*Fig. 1.2.1. Antenna gain pattern [2]*

According to [\[2\]](http://www.atlantarf.com/Downloads.php) total antenna losses for large cassegrain antennas are equal to 1.65 dB.

### 1.2.2. Phase effects in the atmosphere

Influence data rate, due to receiver bandwidth should be desirably selected according to table 1.2.1 \[1, p. 91\] to avoid phase distortions.

Table 1.2.1. Maximum receiver bandwidths for different ranges.

| Carrier frequency, GHz | 0.5 | 1 | 5 | 10 |
| :--- | :--- | :--- | :--- | :--- |
| Receiver bandwidth \(B\), MHz | 10 | 25 | 270 | 750 |

Additionaly, to avoid Faradey effect for ranges less than 10 GHz only circular polarization should be used \[1, p. 91\].

### 1.2.3. Loss due to inconsistency of polarization of antennas

Can be estimated by figure 1.2.2 \($e_1$ and $e_2$ are coefficients of elipticity\).



![Fig. 2.2. Dependence of losses due to inconsistency of the polarizations of the transmitting and receiving antennas from the polarity elepticity. \[1, p. 93\]](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20%287%29.png)
*Fig. 1.2.2. Dependence of losses due to inconsistency of the polarizations of the transmitting and receiving antennas from the polarity elepticity. \[1, p. 93\]*

In general, this parameter is kind of reference data, e.g. in the link budget calculation for [NanoCom AX100](https://gomspace.com/UserFiles/Subsystems/datasheet/gs-ds-nanocom-ax100-33.pdf) polarization losses are equal to 3 dB \(and athmospheric losses are 2.1 dB,  ionospheric losses are 0.4 dB\).

### 1.2.4. Attenuations due to hydrometeors and other additional losses

Can be evaluated by [\[3\]](https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.676-11-201609-I!!PDF-E.pdf). Fortunately, for ranges smaller than 10 GHz the losses are smaller than 1 dB \(fig. 1.2.3 and 1.2.4\).

![Fig. 2.3:  Specific attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[10\].](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/atten1.png)
*Fig. 1.2.3.  Specific attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[10\].*

![Fig.  2.4:  Zenith attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[3\].](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/atten2.png)
*Fig.  1.2.4.  Zenith attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[3\].*

##  References

\[1\] L. Kantor, Satellite communication and broadcasting. Directory,Radio and communication,1988, 

\[2\] [Antennas - An Overview](http://www.atlantarf.com/Downloads.php)  \(date of the application is 09.07.2018\)

\[3\] [Attenuation by atmospheric gases, ITU 2016](https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.676-11-201609-I!!PDF-E.pdf) \(date of the application is 27.06.2017\)
