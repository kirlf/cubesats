# 6. Margin for shadowing

According to \[5\] the most appropriate channel model for LEO satellites is the mixture of the Rician and lognormal idependent fading processes. Although shadowing \(lognormal part\) is negligible on elevation angles larger than 60 degrees \(and smaller than 120 degree\) \[5\], we suppose that it is not exessive to add to our link budget calculations calculation of marging for shadowing.

According to log-distance path loss model \[27-28\] shadowing process influences link budget due to it makes a contribution to losses \(logorithmic scale\):


$$
P_r = P_t - L - \chi \qquad (6.1)
$$


where $$P_r$$ is the received power, $$P_t$$ is the transmitt power, $$L$$ is the total losses that were considered in chapter 2 and $$\chi$$ is the lognormal distributed random value.

For more or less precise estimation of link budget let us use following formula:


$$
\hat{P_r} = P_t - L - E\{\chi\} \qquad (6.2)
$$


where $$E\{*\}$$ denotes expectation.

According to \[5\] we have two generalized cases: ligth shadowing \( $$\mu$$ = 0.13 and $$\sigma$$ = 1.0\) and strong shadowing \( $$\mu$$ = −1.08 and $$\sigma$$ = 2.5\), where $$\mu $$ denotes the Log mean of and $$\sigma$$ denotes Log standard deviation.

Using modeling in MATLAB, obtain $$\chi$$ equals to about 9 dB for strong  shadowing and about 2 dB for light shadowing.

