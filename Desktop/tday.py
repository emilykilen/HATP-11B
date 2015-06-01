# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:55:04 2015

@author: ekilen
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:51:11 2015

@author: ekilen
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:30:43 2015

@author: ekilen
"""

import numpy as np
import matplotlib.pyplot as plt


#Constants used
#Planck's constant (kg/s)
h = 6.62606957e-34 
#speed of light (m/s)
c = 299792458
#Boltzmanns constant (m^2*kg*s^-2*K^-1)
k = 1.3806488e-23
#Radius of star (m)
Rs = .683*695800*1000
#Radius of planet (m)
Rp = 4.31*6371*1000
#Temperature of star (K)
Ts = 4780
#Albedo
At = .0001
AO = .95
#Radius of Orbit
Rot = .053*149597871*1000/2-799953630.7
RoO = .053*149597871*1000/2+799953630.7
#Adjustment
b = 1.76


#Constraints

#Ratio of signal over noise (unitless)
SN = 5

#White noise constant over time (unitless)
Sw = .00001281 #Fraine et. al 2014

#Reflection Constant (unitless)
RCt = At*(Rp**2/Rot**2)*b
RCO = AO*(Rp**2/RoO**2)*b

#Number of eclipses (unitless)
Ne = 5

#wavelenght 1 (m)
L1 = 3.6e-6

#wavelenght 2 (m)
L2 = 4.5e-6


#Begin computation


#Red noise variable over time due to factors of
#image persistance, stellar variability, thermal changes, zodi variability
step = .000001
Sr = .00006481 #Fraine
Epsilon = np.arange(.00001,1+step,step)

#planet temp equation(derived from Rich)
Tp1t = h*c/(L1*k*np.log((np.exp(h*c/(L1*k*Ts))-1)*(Ne/(Sw**2+Sr**2))**.5/(SN-RCt*(Ne/(Sw**2+Sr**2))**.5)+1))
Tp2t = h*c/(L2*k*np.log((np.exp(h*c/(L2*k*Ts))-1)*(Ne/(Sw**2+Sr**2))**.5/(SN-RCt*(Ne/(Sw**2+Sr**2))**.5)+1))

Tp1O = h*c/(L1*k*np.log((np.exp(h*c/(L1*k*Ts))-1)*(Ne/(Sw**2+Sr**2))**.5/(SN-RCO*(Ne/(Sw**2+Sr**2))**.5)+1))*(2-Epsilon)**.25
Tp2O = h*c/(L2*k*np.log((np.exp(h*c/(L2*k*Ts))-1)*(Ne/(Sw**2+Sr**2))**.5/(SN-RCO*(Ne/(Sw**2+Sr**2))**.5)+1))*(2-Epsilon)**.25

plt.plot(Epsilon,Tp1O,'r', label = '3.5 microns')
plt.plot(Epsilon,Tp2O,'b', label = '4.5 microns')
plt.ylabel('Planet Day Temp (K)',fontsize = 16, fontweight = 'bold')
plt.xlabel('Heat Transfer Efficiency',fontsize = 16,fontweight = 'bold')
plt.legend(loc =2)



plt.show()
