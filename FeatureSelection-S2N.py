#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:10:09 2017

@author: kshitijap
"""
import sys

path = sys.argv[1]
datafile = "{0}/traindata.data".format(path)
labelfile = "{0}/trainlabel.0".format(path)

#datafile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Project/traindata.data"
#labelfile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Project/trainlabel.0"

### Feature ranking using SNR ###

f = open(datafile)
data = []
i = 0
l = f.readline()

##### Read Data ######
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
    
rows = len(data)
cols = len(data[0])
f.close()

#### Read Labels ####
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()

while(l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
f.close()     

#####Compute mean#####
m0 = []
for i in range(0, cols, 1):
   m0.append(0)
m1 = []
for i in range(0, cols, 1):
   m1.append(0)     

for i in range(0, rows, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            m0[j] = m0[j] + data[i][j]
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(0, cols, 1):
            m1[j] = m1[j] + data[i][j]             
   
for j in range(0, cols, 1):
    m0[j] = m0[j]/n[0]
    m1[j] = m1[j]/n[1]   

#####Compute Std. Deviation#####
s0 = []
for i in range(0, cols, 1):
   s0.append(0)
s1 = []
for i in range(0, cols, 1):
   s1.append(0)     

for i in range(0, rows, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            s0[j] = s0[j] + (data[i][j] - m0[j])**2
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            s1[j] = s1[j] + (data[i][j] - m1[j])**2             
   
for j in range(0, cols, 1):
    s0[j] = (s0[j]/n[0])**0.5
    s1[j] = (s1[j]/n[1])**0.5  

snr = []
for i in range(0, cols, 1):
   snr.append(0)
   
### Calculate SNR for each feature ###
for j in range(0, cols, 1):
     snr[j] = abs((m0[j] - m1[j])/(s0[j] - s1[j]))
     
idx = sorted(range(len(snr)), key=lambda k: snr[k], reverse = True)

f = open("Dataset/rank_snr", "w")
for j in range(0, cols, 1):
    f.write(str("{0}\n".format(idx[j]))) 


                                                                               