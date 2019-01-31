import numpy as np
import matplotlib.pyplot as plt
class LinkBudget:
    def __init__(self, h, mode, L_node = None,\
                 incl = None, lat_gs = None, long_gs = None, eps_min = 0):
        # h - orbit height
        # mode - 'draft' (w/o coordinates consideration) or 'precise' (w/ coordinates consideration)
        # L_node - instantaneous ascending node (degrees)
        # incl - instantaneous orbit pole (degrees)
        # lat_gs - ground station latitude (degrees)
        # long_gs - ground station logtitude (degrees)
        # eps_min - minimum spacecraft elevation (degrees)
        self.h = h
        self.mode = mode
        self.R_E = 6356863
        if mode == 'precise':
            if L_node == None:
                L_node = float(input('Print  different for\
                distinct passes of the satellite\
                over the ground station (L_node) in degrees: '))
            long_pole = (L_node - 90)*np.pi/180
            if incl == None:
                incl = float(input('Print  orbit inclination (incl) in degrees: '))
            lat_pole = (90 - incl)*np.pi/180
            if lat_gs == None:
                lat_gs = float(input('Print latitude\
                of the ground station (lat_gs) in degrees: '))
            if long_gs == None:
                long_gs = float(input('Print longtitude\
                of the ground station (long_gs) in degrees: '))
            lat_gs = lat_gs*np.pi/180
            long_gs = long_gs*np.pi/180
            
            self.eps_min = eps_min*np.pi/180
            delta_l = long_gs - long_pole
            
            sin_lambda_min = np.sin(lat_pole)*np.sin(lat_gs)\
                + np.cos(lat_pole)*np.cos(lat_gs)*np.cos(delta_l)
            self.lambda_min = np.arcsin(sin_lambda_min)
            
            sin_rho = self.R_E /(self.R_E+self.h)
            self.rho = np.arcsin(sin_rho)
            self.eta_max = np.arcsin(sin_rho*np.cos(self.eps_min))
            self.lambda_max = np.pi/2 - self.eps_min - self.eta_max
            

    def distance(self):
        # Outputs:
            # d - satellite-to-ground distance (m)
        if self.mode == 'draft':
            phi = np.pi*np.array(range(0,181,5))/180
            d = np.array(np.sqrt((self.R_E+self.h)**2\
                                 - (self.R_E**2)*np.cos(phi)**2) - self.R_E*np.sin(phi))
        else:
            #minimum distance 
            tan_eta_min = np.sin(self.rho)*np.sin(self.lambda_min)\
                / (1 - np.sin(self.rho)*np.cos(self.lambda_min))
            sin_eta_min = np.sin(np.arctan(tan_eta_min))
            dmin = self.R_E*(np.sin(self.lambda_min)/sin_eta_min)
            #maximum distance 
            sin_eta_max = np.sin(self.eta_max)
            dmax = self.R_E*(np.sin(self.lambda_max)/sin_eta_max)            
            d = np.array(range(int(np.round(dmin)),int(np.round(dmax))))
        return d
                
    def path_loss(self, f0):
        #Inputs:
            # f0 - carrier frequency (Hz)
        #Outputs:
            # 20*np.log10(L) - path loss (dB)
        c = 3*1e8 #electromagnetic wave speed
        lambd = c/f0
        d = self.distance()
        L = 4*np.pi*d/lambd
        return 20*np.log10(L)
    
    def received_power(self, Pt, f0, Gt, Gr, eta_t=0, eta_r = 0, Lt=0, Lr=0, Ladd=5):
        #Inputs:
            # Pt - transmitted power (Watts)
            # f0 - carrier frequency (Hz)
            # Gt - transmitt antenna gain (dBi)
            # Gr - receive antenna gain  (dBi)
            # eta_t - transmitt fider gain (dB)
            # eta_r - receive fider gain (dB)
            # Lt - transmitt fider loss (dB)
            # Lr - receive fider loss (dB) 
            # Ladd - additional losses (dB)
        #Outputs:
            # Pr - received power (dBm)
        Lpl = self.path_loss(f0)
        Pr = 10*np.log10(Pt*1e3) + Gt + Gr + eta_t + eta_r - Lt - Lr - Lpl - Ladd
        return Pr
    
    def noise_power(self, B, Tnoise, gamma = 1):
        #Inputs:
            # B - receiver bandwidth (Hz)
            # Tnoise - noise temperature (K)
            # gamma - nose bandwith constant
        #Outputs:
            # 10*np.log10(N*1e3) - noise spectral density (dBm)
        k = 1.38064852*1e-23 #Bolzman constant
        N = k*B*gamma*Tnoise
        return 10*np.log10(N*1e3)
        
    def expected_snr(self, f0, Pt, Gt, Gr, B, Tnoise, eta_t = 0, eta_r = 0, Lt=0, Lr=0, Ladd = 5, gamma=1):
        #Inputs:
            # f0 - carrier frequency (Hz)
            # Pt - transmitted power (Watts)
            # Gt - transmitt antenna gain (dBi)
            # Gr - receive antenna gain  (dBi)
            # B - receiver bandwidth (Hz)
            # Tnoise - noise temperature (K)
            # eta_t - transmitt fider gain (dB)
            # eta_r - receive fider gain (dB)
            # Lt - transmitt fider loss (dB)
            # Lr - receive fider loss (dB) 
            # Ladd - additional losses (dB)
            # gamma - nose bandwith constant
        #Outputs:
            # snr - expected SNR (dB)
            # EIRP - equivalent isolated radiated power (dBm)
        EIRP = 10*np.log10(Pt*1e3) + Gt
        Pr = self.received_power(Pt, f0, Gt, Gr, eta_t, eta_r, Lt, Lr, Ladd)
        N = self.noise_power(B, Tnoise, gamma)
        snr = Pr - N
        return snr, EIRP
        
    def visibility_time(self):
        #Outputs:
            # T - visibility time (min) 
        if self.mode == 'precise':
            P = 1.658669e-4*((6378.14 + self.h*1e-3)**1.5)
            T = (P/np.pi)*np.arccos(np.cos(self.lambda_max)/np.cos(self.lambda_min))
        elif self.mode == 'draft':
            R_E = 6356863
            v = np.sqrt(6.67e-11*6e24/(R_E + self.h))
            T = (2*(self.R_E + self.h)*np.arccos(self.R_E/(self.R_E + self.h)) / v)/60
        else:
            print('Wrong mode.')
        return T 
