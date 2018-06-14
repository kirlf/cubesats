## 6. Transmission \(gross\) bit rate estimation

Theretical description of modulation scheme selection was provided by us in \[30\]. For **M-PSK** and **M-QAM** modulation schemes following formulas \[31 - 32\] can be used for estimation of **gross bit rate** $$R_b$$:


$$
\eta = \frac{R_b}{B_{null-to-null}} = \frac{log_2 M}{2}  \qquad(2.7)
$$



$$
B_{null-to-null} = \frac{2f_b}{log_2 M} \qquad(2.8)
$$



$$
R_b = \frac{B_{null-to-null}log_2 M}{2} = f_b = \frac{1}{T_b} \qquad(2.9)
$$


where $$\eta$$ is the** spectral effitiency** \(bits/seconds/Herz\) $$M$$ is the modulation order and $$B_{null-to-null} $$ is the **null-to-null bandwidth **\(Herz\)**, **$$f_b$$ is the **3dB bandwidth **\(Herz\)** **and $$T_b$$ is the **bit duration **\(seconds\)**. **Gross bit rate can be estimated throug the **baud rate **$$R_s$$** ** \(number of changes of modulation parameter\(-s\) per second\) also:


$$
R_b = R_slog_2 M \qquad(2.10)
$$


For **MSK** spectral efficiency is equal to \[33\]:


$$
\eta = \frac{R_b}{B_{null-to-null}} = \frac{R_b}{1.5f_b} = 0.667 \quad [bits/second/Hz] \qquad (2.11)
$$


Therefore gross bit rate can be estimated via:


$$
R_b = 1.0005f_b \approx f_b = \frac{1}{T_b} \qquad (2.12)
$$


