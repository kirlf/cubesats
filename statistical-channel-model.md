# Statistical channel model

## 3.1. Model

It makes scense to model Rician flat fading channel to estimate primaraly BER performance. Rician process  can be estimated based on described in \[34\] channel model with simplification to **SISO.**

For modeling of an additive noise Additive White Gaussian Noise \(AWGN\) model was selected.

Results and description were presented in

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
                %BER(c,jj) = just_ber(demod_msg,message);
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

As we can see in figure 5.1 BER performance of the proposal approaches completely matched with theoretical \(**berfading\(\) function in MatLab**\) results.

## 5.3. Ergodic capacity limits



