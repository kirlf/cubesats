# 1. Link Budget

[1.1. Main formulas](https://github.com/kirlf/cubesats/blob/master/LinkBudget/LBformulas.ipynb)

[1.2. Additional losses](https://github.com/kirlf/cubesats/blob/master/LinkBudget/AddLoss.ipynb)

**1.3. Parameters summary**

Let us provide some parameters summary:

1. **Initial point:** carrier frequency,  hight of the orbit;
2. **Equipment dependent parameters \(adjustable\)**: transmitted power , receiver bandwidth ;
3. **Reference data:** antenna gains and losses, feeder gains and losses , noise temperature,  additional losses.

[1.4. Sat-to-Ground distance](https://github.com/kirlf/cubesats/blob/master/LinkBudget/SatDist.ipynb)

[1.5. Visibility time](https://github.com/kirlf/cubesats/blob/master/LinkBudget/VisTime.ipynb)

**1.6. Considered equipment**

In fact, we use informstion about common example of ground station such as IC-910H [\[3\] ](http://sicom.ru/catalog/radiostancii/lyubitelskie/bazovye/icom-ic-9100.html)or ISIS ground station[ \[4\] ](https://www.cubesatshop.com/product/full-ground-station-kit-vhfuhfs-band/)however we can estimate some parameter of mobile stations of real space communication systems also. Fortunately, a lot of this information is open and available on official sites [\[5\]](https://www.iridium.com%20), [\[6\],](https://www.globalstar.com) [\[7\]](http://www.gonets.ru/rus/%20).

These parameters can be used for calculation of up-link link budget.

For down-link estimation real example of CubeSat transceivers such as NanoCom AX100 [\[8\]](https://gomspace.com/Shop/subsystems/communication/nanocom-ant2000.aspx) \(fig. 2.10\) may be used. Additionally, as an example of CubeSat UHF/VHF antenna omnidirectional NanoCom ANT430 \(fig. 2.9\) can be considered [\[9\]](https://gomspace.com/Shop/subsystems/communication/nanocom-ant430.aspx).

![Fig. 2.5: NanoCom AX100 by GomSpace company.](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/antenna1.png)
*Fig. 2.9. NanoCom AX100 by GomSpace company.*

![Fig. 2.6: NanoCom ANT430 by GomSpace company.](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/transceiver.png)
*Fig. 2.10. NanoCom ANT430 by GomSpace company.*

For larger possible bandwidth 2.4GHz range also should be considered. For this range patch-antenna NanoCom ANT2000 and S-band transceiver NanoCom SR2000 are available[ \[10\]](https://gomspace.com/Shop/subsystems/communication/nanocom-sr2000.aspx) \(fig. 2.11\). For low speed transmission \(for example, for signaling\) UHF/VHF NanoCom ANT430 [\[11\]](https://gomspace.com/Shop/subsystems/communication/nanocom-ax100.aspx) \(fig. 2.12\) can be used.

![Fig. 2.7: NanoCom SR2000 by GomSpace company.](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/transceiver2.png)
*Fig. 2.11. NanoCom SR2000 by GomSpace company.*

![Fig. 2.8: ANT2000 by GomSpace company.](https://raw.githubusercontent.com/kirlf/cubesats/master/.gitbook/assets/antenna2.png)
*Fig. 2.12. ANT2000 by GomSpace company.*

