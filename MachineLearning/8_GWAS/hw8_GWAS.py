import sys
import os
from sklearn.cluster import KMeans

### This program takes in simulatd GWAS under logistic regression model and classifies the data using nearest means classifier ####

##### python hw8_GWAS.py trainingdata3.5_20_0 testdata3.5_20_0 #####


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

#print("Length of training dataset array: ", training_len)
#print("Length of test dataset array: ", test_len)

######## Feature Selection to get rid of noisy features ########
fs_cmd = 'python feature_selection.py trainingdata3.5_20_0 trainingTrueLabels.txt testdata3.5_20_0 10 > feature_selection.txt'
os.system(fs_cmd)

print("Number features selected:", 10)

### Run Nearest Means on test data ###
nmcmd = 'python NearestMeans.py feature_selection.txt trainingTrueLabels.txt > nm_result.txt' 
os.system(nmcmd) 


#  
### Compare predicted with true labels ### 
errorcmd = 'python error.py testTrueLabels.txt nm_result.txt'
os.system(errorcmd)
