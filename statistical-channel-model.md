# 5. Simplified statistical channel model

## 5.1. Multiplicative distortions

It makes scense to model Rician flat fading channel to estimate primaraly BER performance. Rician process $$r$$ can be estimated based on described in \[34\] channel model  with simplification to **SISO** \(single input single output\) case:


$$
H = \sqrt{\frac{K}{K+1}}H_{LoS} + \sqrt{\frac{1}{K+1}}H_{NLoS} => r = \sqrt{\frac{K}{K+1}}+  \sqrt{\frac{1}{2(K+1)}}(G_1 + jG_2) \qquad (5.1)
$$


where $$H$$ is the channel matrix, $$K$$ is the Rician factor, Line-of-Sight component  $$H_{LoS} = e^{j2\pi 0 d cos(\theta_r)}e^{j2\pi 0 d cos(\theta_t)} = 1$$ \($$d $$ is the antenna spacing, $$\theta_r $$ is the Direction of Departure, $$\theta_t  $$ is the Direction of Arrival\) and Non-Line-of-Sight component $$H_{NLoS} $$, actually, is the Rayleigh fading process.

**Note 1:**  See "Scripts" for another approach of modeling \(verified for QPSK and 4-QAM\).

**Note 2:** Described in \[30\] approach also works with equalization \(verified for QPSK and 4-QAM\).

## 5.2. Additive noise

For modeling of additive noise Additive White Gaussian Noise \(AWGN\) model was selected.

To model AWGN channel first of all actual power of modeled signal should be measured \[29\]:


$$
E_s=\frac{1}{L}\sum_{k=1}^L|x_k|^2 \qquad (5.2)
$$


where $$x_k$$ is complex symbol and $$L$$ is the length of signal \(block or frame\).

Noise spectral density for different modulation schemes with modulation order $$M$$ can be computed by following formula:


$$
E_b/N_0 = \frac{E_s}{N_0log_2M} => N_0=\frac{E_s}{(E_b/N_0) log_2M } \qquad (5.3)
$$


where $$E_b/N_0 = 10^{(Eb/ N_0)_{dB}/10}$$  is the **energy per bit to noise power spectral density ratio** in linear scale.

AWGN can be modeled via following formula:


$$
\sqrt{\frac{N_0}{2}}(G_1+jG_2) \qquad (5.4)
$$


where $$G_1 $$ and $$G_2$$ are the independent Gaussian processes.

## 5.3. Model verification

For verification of the proposal model we model random binary message \(length of the message equals to 100000 bits\), modulate it by pi/4-QPSK Gray mapping rule, multiply elementwise with fading process, add white gaussian noise, equalize by Zero-Forcing method, demodulate and calculate BER. The number of trials is equal to 10000.

![](/assets/proof_complex.png)

Figure 5.1. Bit error ratio performance of described ways of the modeling.

As we can see  in figure 5.1 BER performance of the proposal approaches completely matched with theoretical \(**berfading\(\) function in MatLab**\) results.

## 5.3. Ergodic capacity limits

Ergodic capacity for our simplified channel model can be estimated cause of flat nature of considered fading process. For this we use  following formula:


$$
C_{erg} = E\{\frac{1}{2}log_2 (1 + |r|^2 \frac{S}{N})\} \quad [bits / transmission] \qquad (5.5)
$$


where $$\frac{S}{N}$$ is the Signal to Noise Ration in linear scale.

Avereged ergodic capacity is provided just for illustration:


$$
C
_{erg}^{'} = E\{\frac{1}{2}log_2 (1 + E\{|r|^2\} \frac{S}{N})\} \quad [bits / transmission] \qquad (5.6)
$$


For AWGN channel capasity can be described via the Shannon theorem:


$$
C = \frac{1}{2}log_2 (1 + \frac{S}{N}) \quad [bits / transmission] \qquad (5.7)
$$


![](/assets/capacity.png)

Figure 5.2. Ergodic capacity in dependance of some set of SNRs.

To estimate capasity in bits per channel use we can use following formula \[31\]:


$$
C = \frac{1}{2} log_2 (1 + \frac{S}{2W\frac{N_0}{2}}) = \frac{1}{2} log_2 (1 + \frac{S}{W N_0})  \quad [bits \quad / \quad channel \quad use] \qquad(5.8)
$$


where $$W$$ is the channel bandwidth.

To estimate capasity in bits second \(more common\) $$C$$ in \(5.8\) should be multiplied by symbol rate $$R_s = 2W $$ \(by Kotelnikov / Nyquist\):


$$
C = W log_2 (1 + \frac{S}{W N_0}) \quad [bits/s] \qquad(5.9)
$$


Final values depend on channel bandwidth selection.

