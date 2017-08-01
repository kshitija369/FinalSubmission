#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:41:30 2017

@author: kshitijap
"""
import sys, random

path = sys.argv[1]
labelfile = "{0}/train.labels".format(path)

#### Generate cross-validation set ####

f = open(labelfile)
#####Read labels#####
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

rows = len(trainlabels)
cv_size = int(0.9 * rows)

for x in range(0,10,1):
    f = open("Dataset/trainlabel.{0}".format(x), "w")
    for i in range(0, cv_size, 1):
        idx = random.randint(0,cv_size)
        f.write(str("{0} {1}\n".format(trainlabels[idx], idx))) 
    f.close()    
    
        
        
        
        
        
        
        
        
        
        
        
        
    