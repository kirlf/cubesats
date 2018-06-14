# Statistical channel model

## 5.1. Multiplicative distortions

It makes scense to model Rician flat fading channel to estimate primaraly BER performance. Rician process  can be estimated based on described in \[34\] channel model with simplification to **SISO** \(single input single output\) case:

where  is the channel matrix,  is the Rician factor, Line-of-Sight component  \( is the antenna spacing,  is the Direction of Departure,  is the Direction of Arrival\) and Non-Line-of-Sight component , actually, is the Rayleigh fading process.

**Note 1:** See "Scripts" for another approach of modeling \(verified for QPSK and 4-QAM\).

**Note 2:** Described in \[30\] approach also works with equalization \(verified for QPSK and 4-QAM\).

## 5.2. Additive noise

For modeling of additive noise Additive White Gaussian Noise \(AWGN\) model was selected.

To model AWGN channel first of all actual power of modeled signal should be measured \[29\]:

where  is complex symbol and  is the length of signal \(block or frame\).

Noise spectral density for different modulation schemes with modulation order  can be computed by following formula:

where  is the **energy per bit to noise power spectral density ratio** in linear scale.

AWGN can be modeled via following formula:

where  and  are the independent Gaussian processes.

## 5.3. Model verification

For verification of the proposal model we model random binary message \(length of the message equals to 100000 bits\), modulate it by pi/4-QPSK Gray mapping rule, multiply elementwise with fading process, add white gaussian noise, equalize by Zero-Forcing method, demodulate and calculate BER. The number of trials is equal to 10000.

![](https://github.com/kirlf/cubesats/tree/4904a8c7c26549dc8a1a08a45237d264e5cc9806/assets/proof_complex.png)

Figure 5.1. Bit error ratio performance of described ways of the modeling.

As we can see in figure 5.1 BER performance of the proposal approaches completely matched with theoretical \(**berfading\(\) function in MatLab**\) results.

## 5.3. Ergodic capacity limits

Ergodic capacity for our simplified channel model can be estimated cause of flat nature of considered fading process. For this we use following formula:

where  is the Signal to Noise Ration in linear scale.

Avereged ergodic capacity is provided just for illustration:

For AWGN channel capasity can be described via the Shannon theorem:

![](https://github.com/kirlf/cubesats/tree/4904a8c7c26549dc8a1a08a45237d264e5cc9806/assets/capacity.png)

Figure 5.2. Ergodic capacity in dependance of some set of SNRs.

To estimate capasity in bits per channel use we can use following formula \[31\]:

where  is the channel bandwidth.

To estimate capasity in bits second \(more common\)  in \(5.8\) should be multiplied by symbol rate  \(by Kotelnikov / Nyquist\):

Final values depend on channel bandwidth selection.

