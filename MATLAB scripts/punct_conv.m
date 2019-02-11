
function ber_conv_fin = punct_conv(message, trellis, PuncturePattern,...
 TracebackDepth, InputFormat, EbNo, infobits, codelength, modorder)
  
%  QPSK coded by puctured Convolutional codes (AWGN) 
% by Vladimir Fadeev
% vladimir_fadeev1993@mail.ru

% inputs: 
%        message: input message
%        trellis: Trellis structure
%        PuncturePattern: vector for puncturing
%        TracebackDepth: Traceback Depth
%        InputFormat: Hard, Soft or Unquantized
%        EbNo: Energy bit to Noise Variance ratio
%        infobits: Length of initial message
%        codelength: Length of codeword
%        modorder: Modulation order (can be replaced)

% outputs:
%        decoded: Decoded vector


  codeRate = infobits/codelength;
  k = (codeRate)*log2(modorder); 
  k2 = log2(modorder);
  snr = EbNo+10*log10(k); % Signal-to-Noise ratio for QPSK
  
  if InputFormat == 'Hard'
      d = 'Hard decision';
      else d =  'Log-likelihood ratio';
  end
 
  
  % QPSK modulator/demodulator
  hModulator = comm.QPSKModulator('BitInput',true,'PhaseOffset',pi/4);
  hDemod = comm.QPSKDemodulator('PhaseOffset',pi/4,'BitOutput',true,...
    'DecisionMethod',d);
 
  
  
  % Encoder
  hConvEnc = comm.ConvolutionalEncoder(trellis);
  hConvEnc.PuncturePatternSource = 'Property';
  hConvEnc.PuncturePattern = PuncturePattern;
  
  % Decoder
  hVitDec = comm.ViterbiDecoder(trellis, ...
  'InputFormat',InputFormat);
  hVitDec.PuncturePatternSource = 'Property';
  hVitDec.PuncturePattern = PuncturePattern;
  hVitDec.TracebackDepth = TracebackDepth;
  hVitDec.SoftInputWordLength = 3; 
  %In case 4 bits are used 
  %the soft-values are quantized to 2^4=16 amplitude levels. 
  %We often forget that on a micro controller or DSP 
  %we would have some more restrictions 
  %as compared to our Matlab processing. 
  %I think from 8-10 bits you should get results 
  %that almost match the ideal soft-processing. 
  %(Thanks for Marko Hennhofer (TU Ilmenau), but works only 3)
  
  hErrorCalc = comm.ErrorRate('ReceiveDelay', hVitDec.TracebackDepth);
  %Encoding
  encoded = step(hConvEnc,message);
  qpsk_msg = step(hModulator,encoded);
  
  ber_conv_fin = zeros(size(EbNo));
  
  for ii = 1:length(EbNo)
    
    reset(hConvEnc)
    reset(hVitDec)
    reset(hErrorCalc)
    % AWGN CHANNEL
    chanAWGN = comm.AWGNChannel('NoiseMethod','Signal to noise ratio (Eb/No)', ...
    'BitsPerSymbol',k2);
    EbNoCoded = EbNo(ii) + 10*log10(codeRate);
    chanAWGN.EbNo = EbNoCoded;
  
    % QUANTIZER
    scalQuant = dsp.ScalarQuantizerEncoder('Partitioning','Unbounded');
    snrdB = EbNo(ii) + 10*log10(k);
    NoiseVariance = 10.^(-snrdB/10);
    scalQuant.BoundaryPoints = (-1.5:0.5:1.5)/NoiseVariance;

    % Processing
    noisy_encoded = awgn(qpsk_msg,snr(ii),'measured','dB');
    demodul = step(hDemod,noisy_encoded);
  
    if InputFormat == 'Soft'
        demodul = step(scalQuant,-demodul);
    end
  
    decoded = step(hVitDec,double(demodul));
    ber_conv = step(hErrorCalc,message,decoded);
    ber_conv_fin(ii) = ber_conv(1,:);
   end
end
