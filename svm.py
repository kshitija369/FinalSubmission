#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:12:00 2017

@author: kshitijap
"""
import sys
from sklearn import svm

path = sys.argv[1]
feat_count = int(sys.argv[2])

datafile = "{0}/traindata.data".format(path)
#datafile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Project/Dataset/traindata.data"
#feat_count = 15

clf = svm.SVC()

### Read index of top features ###
f = open("Dataset/rank_snr")
top_feat = []
l = f.readline()
while(l != ''):
    top_feat.append(int(l))
    l = f.readline()
f.close()

## Print top features ##
print("Features used are: \n")
for i in range(0,feat_count,1):
    print(top_feat[i])

for k in range(0, 10, 1):            
    #####Read labels#####
    labelfile = "Dataset/trainlabel.{0}".format(k)
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
    
    f = open(datafile)
    data = []
    pred = []
    i = 0
    l = f.readline()
    
    #####Read Data######
    while(l != ''):
        a = l.split()
        l2 = []
        for j in range(0, feat_count, 1):
            l2.append(float(a[top_feat[j]]))
            
        if(trainlabels.get(i) != None):
            data.append(l2)
        else:
            pred.append(l2)
        i += 1;    
        l = f.readline()
        
    rows = len(data)
    cols = len(data[0])
    pred_rows = len(pred)
    f.close()
    
    Y = []
    Y = list(trainlabels.values())
    clf.fit(data, Y) 
    
    ##### Classify CV set #####  
    y = []           
    y = list(clf.predict(pred))
    
    ## Write prediction values for CV ###
    predfile = "Dataset/pred.{0}".format(k)
    f = open(predfile, "w") 
    
    for x in range(0, pred_rows, 1):
        if( trainlabels.get(x) == None): 
            f.write(str("{0} {1}\n".format(y[x], x)))  
    f.close()  


### Write Prediction values for Test dataset
testfile = "Dataset/testdata"
f = open(testfile)
test = []
i = 0
l = f.readline()

##### Read Test Data ######
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, feat_count, 1):
        l2.append(float(a[top_feat[j]]))
        
    test.append(l2)
    i += 1;    
    l = f.readline()
    
test_rows = len(test)
test_cols = len(test[0])
f.close()

##### Classify Test dataset #####  
y = []           
y = list(clf.predict(test))

## Write prediction values for CV ###
predfile = "Dataset/testpred"
f = open(predfile, "w") 

for x in range(0, test_rows, 1): 
    f.write(str("{0} {1}\n".format(y[x], x)))  
    
f.close() 