You can also find something [here ](http://psas.pdx.edu/research-notebooks/cubesat-linkbudget/cubesat-linkbudget)\(Python example\) and [here ](http://cedarweb.vsp.ucar.edu/wiki/index.php/File:Cubesat_Link-Budget.xls)\(xls-file with detailed calculation procedure\).

```MATLAB
function snr = sat_to_ground_lb(Pt, freq, Gt, Gr, BW, Tnoise)

% by Vladimir Fadeev
% vladimir_fadeev1993@mail.ru

% inputs:
%          Pt - power of transmitter (Watt)
%          freq - carrier frequency (Hz)
%          Gt - transmit antenna gain (dB)
%          Gr - receive antenna gain (dB)
%          BW - band width (Hz)
%          Tnoise - termal noise (K)

% output:
%          snr - expected Signal-to-Noise ratio (dB)

    Gt_lin = 10^(Gt/10);
    Gr_lin = 10^(Gr/10);

    Pt_dBm = 10*log10(Pt*1000);

    c = 3*10^8; 
    lambda = c / freq;
    d = 750*10^3; %for CubeSats
    L = lambda^2 /(16*(pi^2)*d^2); %Path losses
    Pathloss = 10*log10(L);

    Ladd = 5;
    Ladd = 10^(Ladd/10);

    k = 1.38064852*10^(-23); %Bolzman constant
    gamma = 1.11; %by Kantor
    Pinoise = gamma*BW;
    Lnoise = (k*Tnoise*Pinoise)
    Pnoise_dBm = 10*log10(Lnoise*1000)

    EIRP = Pt_dBm + Gt


    snr = 10*log10(Pt*Gt_lin*Gr_lin*L/(Ladd*Lnoise));
end
```

```MATLAB
function snr = intersat_lb(Pt, freq, Gt, Gr, BW, Tnoise,d)

% by Vladimir Fadeev
% vladimir_fadeev1993@mail.ru

% inputs:
%          Pt - power of transmitter (Watt)
%          freq - carrier frequency (Hz)
%          Gt - transmit antenna gain (dB)
%          Gr - receive antenna gain (dB)
%          BW - band width (Hz)
%          Tnoise - termal noise (K)
%          d - distance (m)

% output:
%          snr - expected Signal-to-Noise ratio (dB)

    Gt_lin = 10^(Gt/10);
    Gr_lin = 10^(Gr/10);

    Pt_dBm = 10*log10(Pt*1000);

    c = 3*10^8; 
    lambda = c / freq;
    %d = 750*10^3; %for CubeSats
    L = lambda^2 ./(16*(pi^2)*d.^2); %Path losses
    Pathloss = 10*log10(L);

    Ladd = 5;
    Ladd = 10^(Ladd/10);

    k = 1.38064852*10^(-23); %Bolzman constant
    gamma = 1.11; %by Kantor
    Pinoise = gamma*BW;
    Lnoise = (k*Tnoise*Pinoise)
    Pnoise_dBm = 10*log10(Lnoise*1000)

    EIRP = Pt_dBm + Gt;


    snr = 10*log10(Pt*Gt_lin*Gr_lin.*L./(Ladd*Lnoise));
end
```

```MATLAB
%% Calculation of margin for shadowing
% Strong shadowing
for i = 1:10000
    r(i) = lognrnd(-1.08, 2.5);
end

avr = sum(r')/length(r)

% Light shadowing
for i = 1:10000
    r(i) = lognrnd(0.13, 1.0);
end

avr = sum(r')/length(r)
```

```MATLAB
%% Rician flat fading channel for QPSK (4-QAM) transmission
% Source:
% https://www.mathworks.com/matlabcentral/newsreader/view_thread/11405
% (was available until December 2017)

mu = sqrt( K/(2*(K+1))); %mean
s = sqrt( 1/(2*(K+1)) ); %variance
r = ( s*randn(size(msg)) + mu ) + j*( s*randn(size(msg)) + mu ); %distribution
R = abs(r); %fading
% worked even withot equalization
```



