# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:06:13 2017

@author: bjr21
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#get birth and retirement years for calculating bend points
#birthyr = input('What year were you born? ')
#birthyr = eval(birthyr)
#retyr = birthyr + 67

#avgwg=input('What is your average indexed wage? ')
#avgwg = eval(avgwg)
avgwg =  40000 #average indexed wage
AIMEinput = avgwg/12 #average Indexed monthly earnings

mydir=os.getcwd()
BParray=pd.read_csv(os.path.join(mydir,'BendPoint.csv'))
#BPfirst=pd.ols(y=BParray['Year'],x=BParray['First'])


BP1=885
BP2=5536

def pia(AIME):
    out = 0.9*min(AIME, BP1)+0.32*min(BP2-BP1,max(0,AIME-BP1))+0.15*max(0,AIME-BP2)
    return out

AIME0=0
AIMEf=BP2+0.333*BP2
step=50

aimeplt = np.linspace(AIME0,AIMEf,AIMEf/step)
piaplt = np.zeros(len(aimeplt))

for i in range(len(aimeplt)):
    piaplt[i] = pia(aimeplt[i])
    
sns.set_context('poster')
plt.plot(aimeplt,piaplt)
plt.plot(AIMEinput,pia(AIMEinput),'ro')
plt.annotate(str(np.ceil(pia(AIMEinput))),xy=(AIMEinput+step/2,pia(AIMEinput)-50))
plt.xlabel('Average Indexed Monthly Earnings')
plt.ylabel('Primary Insurance Amount')
plt.title('Social Security Payment')

