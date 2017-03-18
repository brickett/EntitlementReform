# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:06:13 2017

@author: bjr21
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

avgwg =  40000 #average indexed wage
AIMEinput = avgwg/12 #average Indexed monthly earnings

BP1=1000
BP2=2000

def pia(AIME):
    out = 0.9*min(AIME, BP1)+0.32*min(BP2-BP1,max(0,AIME-BP1))+0.15*max(0,AIME-BP2)
    return out

AIME0=500
AIMEf=4000
step=50

aimeplt = np.linspace(AIME0,AIMEf,AIMEf/step)
piaplt = np.zeros(len(aimeplt))

for i in range(len(aimeplt)):
    piaplt[i] = pia(aimeplt[i])

plt.plot(aimeplt,piaplt)
plt.xlabel('Average Indexed Monthly Earnings')
plt.ylabel('Primary Insurance Amount')