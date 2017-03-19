# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:06:13 2017

@author: Bryan Ricketts
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import os

#get birth and retirement years for calculating bend points
birthyr = input('What year were you born? ')
birthyr = eval(birthyr)
retyr = birthyr + 67
#retyr=2017

avgwg=input('What is your average indexed wage? ')
avgwg = eval(avgwg)
#avgwg =  40000 #average indexed wage
AIMEinput = avgwg/12 #average Indexed monthly earnings

#calculate bend point based on previous years' points
mydir=os.getcwd()
BParray=pd.read_csv(os.path.join(mydir,'BendPoint.csv'),encoding="utf-8-sig")
y=BParray['Year']
y=sm.add_constant(y)
x1=BParray['First']
x2=BParray['Second']

model1=sm.OLS(x1,y,missing='drop')
results1=model1.fit()
results1.summary()
BP1const=results1.params['const']
BP1param=results1.params['Year']

model2=sm.OLS(x2,y,missing='drop')
results2=model2.fit()
results2.summary()
BP2const=results2.params['const']
BP2param=results2.params['Year']

BP1=BP1param*retyr+BP1const
BP2=BP2param*retyr+BP2const

#calculate PIA
def pia(AIME):
    out = 0.9*min(AIME, BP1)+0.32*min(BP2-BP1,max(0,AIME-BP1))+0.15*max(0,AIME-BP2)
    return out

#create general plot for PIA
AIME0=0
AIMEf=BP2+0.333*BP2
step=50

aimeplt = np.linspace(AIME0,AIMEf,AIMEf/step)
piaplt = np.zeros(len(aimeplt))

for i in range(len(aimeplt)):
    piaplt[i] = pia(aimeplt[i])
    
#plot PIA with user's point
sns.set_context('poster')
plt.plot(aimeplt,piaplt)
plt.plot(AIMEinput,pia(AIMEinput),'ro')
plt.annotate(str(np.ceil(pia(AIMEinput))),xy=(AIMEinput+step/2,pia(AIMEinput)-50))
plt.xlabel('Average Indexed Monthly Earnings')
plt.ylabel('Primary Insurance Amount')
plt.title('Social Security Payment')

