# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:06:13 2017

@author: bjr21
"""
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

avgwg =  40000 #average indexed wage
AIME = avgwg/12 #average Indexed monthly earnings

BP1=1000
BP2=2000

pia = 0.9*min(AIME, BP1)+0.32*min(BP2-BP1,max(0,AIME-BP1))+0.15*max(0,AIME-BP2)