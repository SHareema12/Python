import sys
import os
from sklearn.cluster import KMeans
import numpy as np

### This program takes in simulatd GWAS under logistic regression model and classifies the data using nearest means classifier ####

##### python hw9_multivariateFR.py trainingdata3.5_20_0 testdata3.5_20_0 #####


#### Read in training dataset from file ### 
training = []
file = open(sys.argv[1],'r')
line = file.readline()
while(line != ""):
  a = []
  x = line.split()
  for i in range(0,len(x),1):
    a.append(x[i])
  training.append(a)
  line = file.readline()

training_len = len(training) 
training_colsb4 = len(training[0])

### Read in test dataset from file ####
test = []
file = open(sys.argv[2],'r')
line = file.readline()
while(line != ""):
  a = []
  x = line.split()
  for i in range(0,len(x),1):
    a.append(x[i])
  test.append(a)
  line = file.readline()
  
test_len = len(test)

#### Convert both arrays to numpy arrays ### 
trainingdata = np.asarray(training)
testdata = np.asarray(test) 

######## Feature Selection to get rid of noisy features ########
fs_cmd = 'python feature_selection.py trainingdata3.5_20_0 trainingTrueLabels.txt testdata3.5_20_0 50 > feature_selection.txt'
os.system(fs_cmd)

print("Number features selected:", 50)

### Run Linear SVM on features selected ###
nmcmd = 'python SVM.py feature_selection.txt trainingTrueLabels.txt 1 > svm_result.txt' 
os.system(nmcmd) 

### Read ranked weights and predictions from SVM ####
ranked_weights = []
file = open("ranked_weights.txt",'r')
line = file.readline()
while(line != ""):
  a = []
  x = line.split()
  for i in range(0,len(x),1):
    a.append(x[i])
  ranked_weights.append(a)
  line = file.readline()

for i in range(0,len(ranked_weights),1):
  print("W value number ", i,ranked_weights[i])

#  
### Compare predicted with true labels ### 
errorcmd = 'python error.py testTrueLabels.txt svm_result.txt'
os.system(errorcmd)
