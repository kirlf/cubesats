## 7. Transmission \(gross\) bit rate estimation

Theretical description of modulation scheme selection was provided by us in \[30\]. For **M-PSK** and **M-QAM** modulation schemes following formulas \[31 - 32\] can be used for estimation of **gross bit rate** $$R_b$$:


$$
\eta = \frac{R_b}{B_{null}} = \frac{log_2 M}{2}  \qquad(7.1)
$$



$$
B_{null} = \frac{2f_b}{log_2 M} \qquad(7.2)
$$



$$
R_b = \frac{B_{null}log_2 M}{2} = f_b = \frac{1}{T_{b}} \qquad(7.3)
$$


where $$\eta$$ is the** spectral effitiency** \(bits/seconds/Herz\) $$M$$ is the modulation order and $$B_{null} $$ is the **null-to-null bandwidth **\(Herz\)**, **$$f_b$$ is the **3dB bandwidth **\(Herz\)** **and $$T_b$$ is the **bit duration **\(seconds\)**. **Gross bit rate can be estimated throug the **baud rate \(symbol rate\) **$$R_s$$** ** \(number of changes of modulation parameter\(-s\) per second\) also:


$$
R_b = R_slog_2 M \qquad(7.4)
$$


For **MSK** spectral efficiency is equal to \[33\]:


$$
\eta = \frac{R_b}{B_{null}} = \frac{R_b}{1.5f_b} = 0.667 \quad [bits/second/Hz] \qquad (7.5)
$$


Therefore gross bit rate can be estimated via:


$$
R_b = 1.0005f_b \approx f_b = \frac{1}{T_b} \qquad (7.6)
$$
Note that symbol rate will depend on **channel bandwith** and therefore bit duration will be different for MSK and M-PSK \(and for diferent M-s\), i.e $$T_b = T_s / log_2 M$$.

