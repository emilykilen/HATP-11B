# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:38:46 2015

@author: ekilen
"""

import matplotlib.pyplot as plt

#Parameters to change

H_g = 6.00612e-7

H2_ref = 9.9895232e-03

H20_g = 9.7934795e-04

N_g = 7.1392985e-10

NH_g = 1.0542917e-08

NO_g = 4.3645127e-08

N2_ref = 6.7576251e-05

O_g = 3.6189143e-11

OH_g = 9.9380515e-08

O2_ref = 2.2606546e-11

#Find sum

total = H_g+H2_ref+H20_g+N_g+NH_g+NO_g+N2_ref+O_g+OH_g+O2_ref

#Find percentages

H = H_g/total*100

H2 = H2_ref/total*100

H20 = H20_g/total*100

N = N_g/total*100

NH = NH_g/total*100

NO = NO_g/total*100

N2 = N2_ref/total*100

O = O_g/total*100

OH = OH_g/total*100

O2 = O2_ref/total*100


#graph

#Slices ordered and plotted
labels = 'H_g', 'H2_ref', 'H20_g', 'N_g', 'NH_g', 'NO_g', 'N2_ref', 'O_g', 'OH-g', 'O2_ref'
fracs = [H, H2, H20, N, NH, NO, N2, O, OH, O2]
explode = (0,.05,0,0)

plt.pie(x, explode = None, labels = labels,autopct = None,pctdistance=1.5,shadow = False,labeldistance=1.5, startangle =None,radius=None)

plt.show()