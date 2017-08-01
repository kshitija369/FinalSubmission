#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:31:52 2017

@author: kshitijap
"""
import os, sys

path = sys.argv[1]
#path = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Project/Dataset/"


#####Read labels#####
labelfile = "{0}/train.labels".format(path)
f = open(labelfile)
data = {}
i = 0
l = f.readline()

while(l != ''):
    a = l.split()
    data[int(a[1])] = int(a[0])
    l = f.readline()
    
rows = len(data)
f.close()

error = 0
for k in range(0, 10, 1):       
    #####Read predictions#####
    predfile = "{0}/pred.{1}".format(path,k)
    f = open(predfile)
    predlabels = {}
    n = []
    n.append(0)
    n.append(0)
    l = f.readline()
    
    while(l != ''):
        a = l.split()
        predlabels[int(a[1])] = int(a[0])
        l = f.readline()
        n[int(a[0])] += 1
    f.close()
    
    #####Compute balanced error#####   
    a=b=c=d=0
    for i in range(0, rows, 1):
        if( predlabels.get(i) != None and data.get(i) != None):
           if(predlabels.get(i) == 0 and data.get(i) == 0): 
               a=a+1 
           if(predlabels.get(i) == 0 and data.get(i) == 1): 
               b=b+1 
           if(predlabels.get(i) == 1 and data.get(i) == 0): 
               c=c+1 
           if(predlabels.get(i) == 1 and data.get(i) == 1): 
               d=d+1 
    if( (a+b) == 0 and (c+d) == 0):
        print("failed")
    elif( (a+b) == 0):
        error = error + 0.5*(c/(c+d)) 
    elif( (c+d) == 0):
        error = error + 0.5*(b/(a+b)) 
    else:
        error = error + 0.5*(b/(a+b) + c/(c+d))
       
error = round((error/10),4)
print("Average Balanced error : {0}".format( error))
           
            
            
            

