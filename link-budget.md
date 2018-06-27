# Link Budget

## 2.1. Main formulas

Main formulas are performed in 

\(link\)

Let us provide some parameters summary:

1. **Initial point:** carrier frequency, distance ;
2. **Equipment dependent parameters \(ajustable\)**: transmitted power , receiver bandwidth ;
3. **Reference data:** antenna gains  ****and ****, sum of antenna losses and sky noise , noise figure .

## 2.2. Considered equipment

In fact, we use common example of ground station such as IC-910H \[13\] or ISIS ground station \[14\] however we can estimate some parameter of transceivers of real space communication systems. Fortunately, a lot of this information is open and avail- able on official sites available \[15\], \[16\],\[17\] \(table 2.1\).

These parameters can be used for calculation of up-link link budget.

For down-link estimation real example of CubeSat transceivers such as NanoCom AX100 \[26\] may be used. Additionally, as an example of CubeSat UHF/VHF antenna omnidirectional NanoCom ANT430 can be considered \[26\].

![Fig. 2.1: NanoCom AX100 by GomSpace company.](.gitbook/assets/antenna1.png)

![Fig. 2.2: NanoCom ANT430 by GomSpace company.](.gitbook/assets/transceiver.png)

For lager possible bandwidth 2.4GHz range also should be considered. For this range patch-antenna NanoCom ANT2000 and S-band transceiver NanoCom SR2000 are available \[26\].

![Fig. 2.3: NanoCom SR2000 by GomSpace company.](.gitbook/assets/transceiver2.png)

![Fig. 2.4: ANT2000 by GomSpace company.](.gitbook/assets/antenna2.png)



To sum up, main parameters for link budget calculation are maintained in table 2.4.

## 2.3. Additional losses

Additional loses due to scattering in atmosphere can be compute by \[9\]. Attenuations due to hydrometeors and other additional loses can be evaluated by \[11\]. Fortunately, for ranges smaller than 10 GHz the losses are smaller than 1 dB.

![Fig. 2.5:  Specific attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[9\].](.gitbook/assets/atten1.png)

![](https://github.com/kirlf/cubesats/tree/4904a8c7c26549dc8a1a08a45237d264e5cc9806/assets/atten1.png)

![Fig.  2.6:  Zenith attenuation due to atmospheric gases, calculated at 1 GHz intervals, including line centres \[9\].](.gitbook/assets/atten2.png)

## 2.4 Results

Results are performed in tables 2.2-2.4 in the following pdf-file:

[Click here ](https://yadi.sk/i/SuZLOYhV3Qoy6o)

![](https://github.com/kirlf/cubesats/tree/4904a8c7c26549dc8a1a08a45237d264e5cc9806/assets/8.png) Distance between satellite and ground station was fixed in value that is equal to height of the orbit \(_h_\). More precise calculation of the distances in dependance of elevation angles \(_phi_\) can be provided according to \[8\]:

$$
d = \sqrt{(R_E+h)^2-R^2cos^2\phi} - R_Esin\phi \qquad (1.1)
$$

 where _RE_ is the Earth radius.

![Fig. 2.7. Distance between CubeSat and ground station in dependance of elevation angles \(h = 750 km\).](.gitbook/assets/distance.png)



![Fig. 2.8: Distances between CubeSat and ground station in dependance of elevation angles.](.gitbook/assets/distance2.png)

  


![Fig. 2.9: Pathloss in dependance of elevation angles \(h = 750 km\).](.gitbook/assets/pathloss.png)

## 2.5 Possible doppler shifts 

 Possible doppler shifts can be estimated by well-known formula:

$$
f_D = f\frac{v}{c}cos\phi
$$

 where _f_ is the carrier frequency, _c_ is the speed of the electromagnetic wave, _v_ is the circular velosity of the satellite and _ϕ_ is the elevation angle.

 Assume that we consider environment without any influence of the atmosphere. Then circular velosity can be calculated via the classical way:

$$
v = \sqrt{G\frac{M}{R}}
$$

 where _G=6.67×\(10^−11\)_ m3×kg−1×s−2 is the Gravity constant, _M=6×10^24_ kg is the Earth mass and _R=RE+h_ is the orbit radius \(Earth radius plus orbit heigh\).

![Figure 2.10. Cercular velosity of LEO satellites in dependance of the orbit heigh.](.gitbook/assets/velosity.png)

  
Then Doppler shifts can be obtained.

![Figure 2.11. Possible Doppler shifts in dependance of the elevation angle \(h = 750 km\). ](.gitbook/assets/doppler.png)

As we see in the Figure 2.6 Doppler shifts for 2.4 GHz may be significant and therefore mitigation of the time selective fading techniques should be included in the final CubeSat configuration.

