# Name: Tina Mihm
# Date: 07/11/2019
# Description: Averages HF eigenvalues and uses them to find a special twist angle


import csv

import numpy as np
import numpy.ma as ma
import subprocess
import re
import pandas as pd
##import seaborn as sns
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.colors import *
from matplotlib.font_manager import fontManager, FontProperties
from scipy.optimize import curve_fit
from scipy.optimize import least_squares
from matplotlib.ticker import MaxNLocator

###
### SET UP FIGURE
###
rcParams['text.usetex'] = True
###
### Fonts
###
rcParams['axes.labelsize'] = 8
rcParams['xtick.labelsize'] = 8
rcParams['ytick.labelsize'] = 8
rcParams['legend.fontsize'] = 8
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = 'Computer Modern Roman'
rcParams['legend.numpoints'] = 1
rcParams['lines.linewidth'] = 2.0
rcParams['lines.markersize'] = 6.0
# http://stackoverflow.com/questions/7906365/matplotlib-savefig-plots-different-from-show
rcParams['savefig.dpi'] = 100
rcParams['figure.dpi'] = 200
###
### Size of the figure
###
ratio=(np.sqrt(5)-1)/2.0     # golden ratio
#ratio=1                     # square figure
plt.rcParams["figure.figsize"] = 3.37, (3.37)*ratio
#rcParams[‘figure.figsize’] = 3.37, 3.37
fig = figure()
Hartree = []
Coup_Clust = []
MOl_PLES = []
HF = []
CCD = []
MP2 = []
Twist = []
#df = pd.read_csv('line_up_mp2_twist_N14.out')
In = open('line_up_mp2_twist_N14_TA.out', 'r')
Input = In.readlines()
#print(Input)
Int = Input[:100]
#print(Int)
#for I in Input:
for I in Int:
    #a = averages
    #IND = Input.index(a)
    #print(IND)
    List = I.rstrip('\n')
    #Formula2 = Formula.rstrip(': ')
    L = List.split(' ')
    while("" in L):
        L.remove("")
    #print(L)
    t = L[:3]
    #print(t)
    Twist +=[t]
    ccd = L[5]
    mp2 = L[4]
    #print(ccd)
    hf = L[3]
    Coup_Clust +=[ccd]
    MOl_PLES += [mp2]
    Hartree +=[hf]
    #rint(t)
#print(MOl_PLES)
#print(Twist)

for i in Hartree[:]:
    i = float(i)
    HF +=[i]

#print(HF)

for i in Coup_Clust[:]:
    i = float(i)
    CCD +=[i]

print(CCD)

for i in MOl_PLES[:]:
    i = float(i)
    MP2 +=[i]

#MP2 = np.array(MP2)
#CCD = np.array(CCD)
#HF = np.array(HF)

MP2_tot = np.array(HF)+np.array(MP2)
CCD_tot = np.array(HF)+np.array(CCD)

Av_totMP2 = (sum(MP2_tot)/len(MP2_tot))
Av_totCCD = (sum(CCD_tot)/len(CCD_tot))


Closest_totCCD = min(enumerate(CCD_tot), key=lambda x: abs(x[1]-Av_totCCD))
Index_totCCD = Closest_totCCD[0]
Closest_totMP2 = min(enumerate(MP2_tot), key=lambda x: abs(x[1]-Av_totMP2))
Index_totMP2 = Closest_totMP2[0]

print('------------------------------------')
Av_HF = (sum(HF)/len(HF))
print('Average HF:', Av_HF)

Av = (sum(CCD)/len(CCD))
print('Average CCD:', Av)

Av_MP2 = (sum(MP2)/len(MP2))
print('Average MP2:', Av_MP2)

print('Average total MP2:', Av_totMP2)
print('Average total CCD:', Av_totCCD)

Closest_HF = min(enumerate(HF), key=lambda x: abs(x[1]-Av_HF))
Index_HF = Closest_HF[0]
Closest_CCD = min(enumerate(CCD), key=lambda x: abs(x[1]-Av))
Index = Closest_CCD[0]
Closest_MP2 = min(enumerate(MP2), key=lambda x: abs(x[1]-Av_MP2))
Index_MP2 = Closest_MP2[0]

HF_masked=ma.masked_array(np.array(HF[:]), (np.array(MP2[:]) == MP2[Index_HF]))
Closest_HF_masked = min(enumerate(HF_masked), key=lambda x: abs(x[1]-Av_HF))
Index_HF_masked = Closest_HF_masked[0]
#print((np.array(MP2[:]) == MP2[Index_HF]))
#print(HF_masked,Closest_HF_masked,Index_HF_masked)

print('------------------------------------')
print('------------------------------------')
print("HF twist:", Twist[Index_HF])
print("CCD twist:", Twist[Index])
print("MP2 twist:", Twist[Index_MP2])
print("Total CCD twist:", Twist[Index_totCCD])
print("Total MP2 twist:", Twist[Index_totMP2])

print('------------------------------------')
print('------------------------------------')
print("Closest HF:", Closest_HF)
print('HF at CCD index:', HF[Index])
print('HF at MP2 index:', HF[Index_MP2])
print('HF at total CCD index:', HF[Index_totCCD])
print('HF at total MP2 index:', HF[Index_totMP2])
print('Closest HF for MP2 agrement:', HF[Index_HF_masked])
print('------------------------------------')
print('------------------------------------')
print("Closest CCD:", Closest_CCD)
print('CCD at HF index:', CCD[Index_HF])
print('CCD at MP2 index:', CCD[Index_MP2])
print('CCD at total CCD index:', CCD[Index_totCCD])
print('CCD at total MP2 index:', CCD[Index_totMP2])
print('------------------------------------')
print('------------------------------------')
print("Closest MP2:", Closest_MP2)
print('MP2 at HF index:', MP2[Index_HF])
print('MP2 at CCD index:', MP2[Index])
print('MP2 at total CCD index:', MP2[Index_totCCD])
print('MP2 at total MP2 index:', MP2[Index_totMP2])
print('------------------------------------')
print('------------------------------------')
print("Closest total CCD:", Closest_totCCD)
print('------------------------------------')
print("Closest total MP2:", Closest_totMP2)
print('------------------------------------')
print('------------------------------------')


print('This is connectivity code:', "0.17663645744323730      -0.26898837089538574       0.11373567581176758" )
