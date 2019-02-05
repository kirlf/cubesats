# 2. Statistical channel model


According to [\[1\]](https://www.csie.ntu.edu.tw/~b92b02053/printing/summer/Materials/channel%20model/CHN_A%20statistical%20model%20for%20land%20mobile%20satellite%20channels%20and%20itsapplication%20to%20nongeostationary.pdf) the most appropriate channel model for LEO satellites is the mixture of the Rician and lognormal independent fading processes with two ultimate conditions: light shadowing and strong shadowing \(tab.2.1\). Moreover, shadowing \(lognormal part\) is negligible on elevation angles larger than 60 degrees \(and smaller than 120 degree\) \(fig. 2.1\) [\[1\]](https://www.csie.ntu.edu.tw/~b92b02053/printing/summer/Materials/channel%20model/CHN_A%20statistical%20model%20for%20land%20mobile%20satellite%20channels%20and%20itsapplication%20to%20nongeostationary.pdf).

<img src="https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/image%20(6).png" alt="params" width="600" />

>*Fig. 2.1. Model parameters, sigma, mu and K as a function of the elevation angle, a, in a mal tree-shadowed environment. \[1\]*

 Table 2.1. Statistical characteristics of the LEO channel

| Parameter | Light shadowing | Strong shadowing |
| :--- | :--- | :--- |
|  Rician factor \(linear scale\) | 4.0 | 0.6 |
|  Lognormal mean \(linear scale\) | 0.13 | -1.08 |
|  Lognormal variance \(linear scale\) | 1.0 | 2.5 |


> **NOTE**: 
>
>Possibly, it makes scense to model [Rician flat fading channel](https://nbviewer.jupyter.org/gist/kirlf/4328eb389b3ddc9a0c350eaed468f870) to estimate BER performance primaraly.

Corazza-Vatalaro model (the mixture of the Rician fast fading channel and Log-normal slow fading channel) should be considered for more precise considerationc (fig. 2.2).

![Figure 2.2.  Circuit implementation of the C&V model with Jakes multipath Doppler shaping..](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/cvm.png)
*Figure 2.2.  Circuit implementation of the C&V model with Jakes multipath Doppler shaping.\[2\]*

> Our suggestion is that implementation of this model in MatLab or Python is good student project. This allows to learn more about Doppler spread, Doppler shifts, Log-normal fading, Rate conversion and Interpolation.

Interesting research can be obtained in [\[3\]](https://www.db-thueringen.de/receive/dbt_mods_00026568), where both single-state and multi-state models are considered. 

<img alt="Markov" src="https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/SatMarkov.png" width="600"/>

> Figure 2.3. Semi-Markov model for two satellites \[3\].

## References

\[1\] Giovanni E. Corazza and Francesco Vatalaro, A Statistical Model for Land Mobile Satellite Channels and Its Application to Nongeostationary Orbit Systems, Transac- tions on Vehicular Technology, vol. 43, no. 3. August 1994 


\[2\] Fontan, F. P., Mayo, A., Marote, D., Prieto‐Cerdeira, R., Mariño, P., Machado, F., & Riera, N. (2008). Review of generative models for the narrowband land mobile satellite propagation channel. International Journal of Satellite Communications and Networking, 26(4), 291-316.

\[3\] [Arndt, D. (2015). On Channel Modelling for Land Mobile Satellite Reception (Doctoral dissertation).](https://www.db-thueringen.de/receive/dbt_mods_00026568)
