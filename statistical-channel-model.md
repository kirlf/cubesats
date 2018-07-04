# Statistical channel model

## 3.1. Model

It makes scense to model Rician flat fading channel to estimate primaraly BER performance. Rician process  can be estimated based on described in [\[1\]](https://pdfs.semanticscholar.org/0fdd/65ed5a4e90f2ee44a1a0a8caa3f7021ce9f9.pdf) channel model with simplification to **SISO.** Common formula:

$$
\mathbf{H} = \sqrt{\frac{K}{K+1}}\mathbf{H_{LoS}} + \sqrt{\frac{1} {K+1}}\mathbf{H_{NLoS}}  \qquad (3.1)
$$

where $$\mathbf{H}$$ is the channel matrix,  $$K$$ is the Rician factor, $$\mathbf{H_{LoS}}$$ is the Line-of-Sight component and $$\mathbf{H_{NLoS}}$$is the Non-Line-of-Sight component \(actually, is the Rayleigh fading process\).

For modeling of an additive noise Additive White Gaussian Noise \(AWGN\) model was selected.

Results and description were presented in \[\].

\(link\)

## 3.2. MATLAB script

```text
clear all
close all
clc

EbNo = 0:40;
K = [4.0; 0.6];
M = [4; 8; 16; 64; 256]; %Positions of modulation (M-PSK or M-QAM)

for k = 1:length(K)
    for m = 1:length(M)

        if M(m) >= 16    
            hModulator = comm.RectangularQAMModulator('ModulationOrder',M(m),'BitInput',false);
            hDemod = comm.RectangularQAMDemodulator('ModulationOrder',M(m),'BitOutput',false);
            ric_ber(:,m,k) = berfading(EbNo,'qam',M(m),1,K(k));

        else 
            hModulator = comm.PSKModulator('ModulationOrder',M(m),'BitInput',false); 
            hDemod = comm.PSKDemodulator('ModulationOrder',M(m),'BitOutput',false);
            ric_ber(:,m,k) = berfading(EbNo,'psk',M(m),1,K(k));
        end
    

        message = randi([0,M(m)-1],100000,1);
        mod_msg = step(hModulator,message);
        Es = mean(abs(mod_msg).^2);
        No = Es./((10.^(EbNo./10))*log2(M(m)));

        r = sqrt( K(k)/(K(k)+1)) + sqrt( 1/(K(k)+1))*(1/sqrt(2))*(randn(size(mod_msg)) + 1j*randn(size(mod_msg)));
        ric_msg = mod_msg.*r; % Rician flat fading

        for c = 1:100
            for jj = 1:length(EbNo)
                noisy_mod = ric_msg + sqrt(No(jj)/2)*(randn(size(mod_msg)) + 1j*randn(size(mod_msg))); %AWGN
                noisy_mod = noisy_mod ./ r; % zero-forcing equalization
                demod_msg = step(hDemod,noisy_mod);
                [number,BER(c,jj)] = biterr(message,demod_msg);
            end
        end
        sum_BER(:,m, k) = sum(BER)./c;
        reset(hModulator);
        reset(hDemod);
    end
end

figure(1) 

semilogy(EbNo,sum_BER(:,1,1),'o',EbNo,sum_BER(:,2,1),'o',EbNo,sum_BER(:,3,1),'o',EbNo,sum_BER(:,4,1),'o',EbNo,sum_BER(:,5,1),'o',...
         EbNo,ric_ber(:,1,1),'-',EbNo,ric_ber(:,2,1),'-',EbNo,ric_ber(:,3,1),'-',EbNo,ric_ber(:,4,1),'-',EbNo,ric_ber(:,5,1),'-','LineWidth', 1.5) 
title('Rician model (K = 4.0)') 
legend('QPSK(simulated)', '8-PSK(simulated)', '16-QAM(simulated)', '64-QAM(simulated)' ,'256-QAM(simulated)',...
    'QPSK(theory)','8-PSK(theory)', '16-QAM(theory)', '64-QAM(theory)' ,'256-QAM(theory)') 
xlabel('EbNo (dB)') 
ylabel('BER')
grid on


figure(2) 

semilogy(EbNo,sum_BER(:,1,2),'o',EbNo,sum_BER(:,2,2),'o',EbNo,sum_BER(:,3,2),'o',EbNo,sum_BER(:,4,2),'o',EbNo,sum_BER(:,5,2),'o',...
         EbNo,ric_ber(:,1,2),'-',EbNo,ric_ber(:,2,2),'-',EbNo,ric_ber(:,3,2),'-',EbNo,ric_ber(:,4,2),'-',EbNo,ric_ber(:,5,2),'-','LineWidth', 1.5) 
title('Rician model (K = 0.6)') 
legend('QPSK(simulated)', '8-PSK(simulated)', '16-QAM(simulated)', '64-QAM(simulated)' ,'256-QAM(simulated)',...
    'QPSK(theory)','8-PSK(theory)', '16-QAM(theory)', '64-QAM(theory)' ,'256-QAM(theory)') 
xlabel('EbNo (dB)') 
ylabel('BER')
grid on
```

## 3.3. Model verification

For verification of the proposal model we model random binary message \(length of the message equals to 100000 bits\), modulate it by pi/4-QPSK Gray mapping rule, multiply elementwise with fading process, add white gaussian noise, equalize by Zero-Forcing method, demodulate and calculate BER. The number of trials is equal to 100.

![Figure 3.1. Bit error ratio performance of described ways of the modeling.](.gitbook/assets/4.png)

![Figure 3.2. Bit error ratio performance of described ways of the modeling.](.gitbook/assets/06.png)

As we can see in figures 3.1 and 3.2 BER performance of the proposal approaches completely matched with theoretical \(**berfading\(\) function in MatLab**\) results.

## 3.4. Ergodic capacity limits

Ergodic capacity for our simplified channel model can be estimated cause of flat nature of considered fading process. For this we use following formula:

$$
C_{erg} = \frac{1}{2}E\left\{ log_2\left(1+|r|^2\frac{S}{N}\right)\right\}  \quad [bits/transmission] \qquad (3.2)
$$

where $$S/N$$ is the Signal to Noise Ration in linear scale,  $$r$$  is the fading process and $$E\{*\}$$ denotes expectation. Avereged ergodic capacity is provided just for illustration: 

$$
C_{erg} = \frac{1}{2}E\left\{ log_2\left(1+E\{|r|^2\}\frac{S}{N}\right)\right\}  \quad [bits/transmission] \qquad (3.3)
$$

 For AWGN channel capasity can be described via the Shannon theorem:

$$
C = \frac{1}{2}log_2\left(1+\frac{S}{N}\right)  \quad [bits/transmission] \qquad (3.4)
$$

![Figure 3.3. Ergodic capacity in dependance of some set of SNRs.](.gitbook/assets/capacity.png)

To estimate capasity in bits per channel use we can use following formula based on [\[2\]](http://www.gatestudymaterial.com/study-material/communication%20systems/text%20books/Communication-Systems-4Th-Edition-Simon-Haykin-With-Solutions-Manual.pdf): 

$$
C_{erg} = \frac{1}{2}E\left\{ log_2\left(1+|r|^2\frac{S}{2W\frac{N_0}{2}}\right)\right\}  =  \frac{1}{2}E\left\{ log_2\left(1+|r|^2\frac{S}{WN_0}\right)\right\} \quad [bits/channel-use] \qquad (3.5)
$$

 where _W_ is the channel bandwidth.

To estimate capasity in bits second \(more common\) \(3.5\) should be multiplied  by sampling rate $$f_{samp} = 2W$$  \(by Kotelnikov / Nyquist criterion\):

$$
C_{erg} = WE\left\{ log_2\left(1+|r|^2\frac{S}{WN_0}\right)\right\} \quad [bits/s] \qquad (3.6)
$$

 Final values depend on channel bandwidth selection. Let us to fix it to 1 MHz.

## References

\[1\] Farrokhi, Farrokh R., et al. "Spectral efficiency of FDMA/TDMA wireless systems with transmit and receive antenna arrays." IEEE transactions on wireless communications 1.4 \(2002\): 591-599.

\[2\]  Haykin S. Communication systems. – John Wiley & Sons, 2008. - p.366-368

