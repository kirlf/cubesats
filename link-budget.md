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

\(see [pdf-file](https://yadi.sk/i/SuZLOYhV3Qoy6o)\)

#### **Tab. 2.1:Transmitter parameters of different ground stations.**

| System | Stationary station | Mobile station |
| :--- | :--- | :--- |
|  | Transmit power\(in Watts\) | Transmit power\(in Watts\) |
| IC-910H | 5 - 100 | - |
| ISIS Ground Station | 5 - 100 |  |
| Iridium | - | 0.6 |
| Globalstar | 3 | 0.6 |
| Messenger | 8 - 12 | - |
|  |  |  |
|  | Antenna gains \(in dBi\) | Antenna gains \(in dBi\) |
| IC-910H \(connected to Uda-Yagi\) | 12.8 - 15 | - |
| ISIS Ground Station \(connected to dish antenna\) | up to 35 | - |
| Iridium | - | 0 - 7 |
| Globalstar | up to 17 | 0 - 7 |
| Messenger | up to 17 | - |

#### **Tab. 2.2: Equivalent Isotropically Radiated Power for different ranges \(total additional losses are 5 dB\).**

| Power\(in Watts\) | Range\(in MHz\) | Type of Antenna | Antenna gains          \(in dBi\) | EIRP                           \(in dBm\) |
| :--- | :--- | :--- | :--- | :--- |
| **Uplink** |  |  |  |  |
| 5 |  |  |  | 49.49 |
| 10 | 144 | Uda-Yagi | 12.5 | 52.5 |
| 15 |  |  |  | 54.3 |
| 5 |  |  |  | 54.99 |
| 10 | 2400 | Uda-Yagi | 18 | 58 |
| 15 |  |  |  | 59.76 |
| 5 |  |  |  | 71.99 |
| 10 | 2400 | Dish antenna | 35 | 75 |
| 15 |  |  |  | 76.76 |
| **Downlink** |  |  |  |  |
| 0.5 |  |  |  | 28.5 |
| 1 | 433 | GomSpace ANT430 | 1.5 | 31.5 |
| 2 |  |  |  | 34.5 |
| 0.5 |  |  |  | 34.3 |
| 1 | 2400 | GomSpace ANT2000 | 7.3 | 37.3 |
| 2 |  |  |  | 40.3 |

#### **Tab. 2.3: Noise power and Path loss \(d = 750km \).**

| Range\(in MHz\) | BandwidthB\(in MHz\) | Noise temperature\(in K\) | Noise powerN\(in dBm\) | Path Loss\(in dB\) |
| :--- | :--- | :--- | :--- | :--- |
| **Uplink** |  |  |  |  |
| 144 | 0.5                                                             | 234 | -117.5                       | -133.1 |
|  | 1 |  | -114.45 |  |
|  | 2 |  | -111.4 |  |
| 2400 | 3 | 240 | -109.57    | -157.5 |
|  | 6 |  | -106.56 |  |
|  | 10 |  | -104.34 |  |
| **Downlink** |  |  |  |  |
| 433 | 0.5   | 1000 | -111.15  | -142.7 |
|  | 1 |  | -108.1 |  |
|  | 2 |  | -105.1 |  |
| 2400 | 3 | 1000 | -103.37   | -157.5 |
|  | 6 |  | -100.36 |  |
|  | 10 |  | -98.15 |  |

**Tab. 2.4: Expected Signal-to-Noise ratios**

| Range \(in MHZ\) | Receiver bandwidth \(in MHz\) | Uplink |  | Downlink |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Power   \(in watts\) | SNR \(in dB\) | Power \(in Watts\) | SNR \(in dB\) |
| 144 /433 | 0.5 | 5 | 30.3 | 0.5 | 6.97 |
| antenna gains: |  | 10 | 33.3 | 1 | 9.98 |
| 12.5 \(ground\) |  | 15 | 35.1 | 2 | 13 |
| 1.5 dBi \(CubeSat\) | 1 | 5 | 27.3 | 0.5 | 3.96 |
|  |  | 10 | 30.3 | 1 | 6.97 |
|  |  | 15 | 32.1 | 2 | 9.98 |
|  | 2 | 5 | 24.3 | 0.5 | 0.95 |
|  |  | 10 | 27.3 | 1 | 3.96 |
|  |  | 15 | 29.1 | 2 | 6.97 |
| 2400 | 3 | 5 | 9.3 | 0.5 | -6.88 |
| antenna gains: |  | 10 | 12.3 | 1 | -3.87 |
| 18 dBi \(ground\) |  | 15 | 14.1 | 2 | -0.86 |
| 7.3 dBi \(CubeSat\) | 6 | 5 | 6.3 | 0.5 | -9.89 |
|  |  | 10 | 9.3 | 1 | -6.88 |
|  |  | 15 | 11.1 | 2 | -3.87 |
|  | 10 | 5 | 4.1 | 0.5 | -12.1 |
|  |  | 10 | 7.1 | 1 | -9.1 |
|  |  | 15 | 8.9 | 2 | -6.09 |
| 2400 | 3 | 5 | 26.3 | 0.5 | 10.1 |
| antenna gains: |  | 10 | 29.3 | 1 | 13.1 |
| 36 dBi \(ground\) |  | 15 | 31.3 | 2 | 16.1 |
| 7.3 dBi \(CubeSat\) | 6 | 5 | 23.3 | 0.5 | 7.1 |
|  |  | 10 | 26.3 | 1 | 10.1 |
|  |  | 15 | 28.3 | 2 | 13.1 |
|  | 10 | 5 | 21.1 | 0.5 | 4.88 |
|  |  | 10 | 24.1 | 1 | 7.8 |
|  |  | 15 | 25.9 | 2 | 10.9 |

![](https://github.com/kirlf/cubesats/tree/4904a8c7c26549dc8a1a08a45237d264e5cc9806/assets/8.png)

## 2.5 Possible doppler shifts 

![Figure 2.6. Possible Doppler shifts in dependance of the elevation angle.](.gitbook/assets/doppler.png)

As we see in the Figure 2.6 Doppler shifts for 2.4 GHz may be significant and therefore mitigation of the time selective fading techniques should be included in the final CubeSat configuration.

