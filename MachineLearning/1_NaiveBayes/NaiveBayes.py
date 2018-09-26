##### naive bayes classication #####
import sys
import math

#### python NaiveBayes.py breast_cancer.data <trainlabelsfile> ####


### read data form file

f = open(sys.argv[1], "r")
lines = f.readlines()

data = []

for i in range(0, len(lines), 1):
    l = lines[i].split()

    for j in range(0, len(l), 1):
        l[j] = float(l[j])

    data.append(l)

rows = len(data)
cols = len(data[0])

#print (rows)


### read labels from file

f = open(sys.argv[2], "r")
line = f.readline()

trainLabels = {}
class_size = [0,0]

while(line != ""):
	  l = line.split()
	  trainLabels[int(l[1])] = int(l[0])
	  line = f.readline()
	  class_size[int(l[0])] +=1

### compute means and standard deviation for naive bayes

m0 = []
sd0 = []
for i in range(0, cols, 1):
	  m0.append(0.00000001)
	  sd0.append(0.00000001)
m1 = []
sd1 = []
for i in range(0, cols, 1):
	  m1.append(0.00000001)
	  sd1.append(0.00000001)

for i in range(0, len(data), 1):
    if(trainLabels.get(i) != None and trainLabels[i] == 0):
        for j in range(0, cols, 1):
            m0[j] = m0[j] + data[i][j]

    if(trainLabels.get(i) != None and trainLabels[i] == 1):
        for j in range(0, cols, 1):
            m1[j] = m1[j] + data[i][j]

for j in range(0, cols, 1):
    m0[j] = m0[j]/class_size[0] ## mean
for j in range(0, cols, 1):
	  m1[j] = m1[j]/class_size[1] ## mean

for i in range(0, len(data), 1):
    if(trainLabels.get(i) != None and trainLabels[i] == 0):
        for j in range(0, cols, 1):
            sd0[j] = sd0[j] + (data[i][j] - m0[j])**2
    if(trainLabels.get(i) != None and trainLabels[i] == 1):
        for j in range(0, cols, 1):
            sd1[j] = sd1[j] + (data[i][j] - m1[j])**2

for j in range(0, cols, 1):
	  sd0[j] = math.sqrt(sd0[j]/(class_size[0] - 1)) ## standard deviation
for j in range(0, cols, 1):
	  sd1[j] = math.sqrt(sd1[j]/(class_size[1] - 1)) ## standard deviation


### prediction

for i in range(len(data)):
	  d0 = 0
	  d1 = 0
	  if(trainLabels.get(i) == None):
		    for j in range(0, cols, 1):

			      d0 += ((data[i][j] - m0[j]) / sd0[j])**2
			      d1 += ((data[i][j] - m1[j]) / sd1[j])**2

		    if(d0<d1):
			      print("0 ", i)
		    else:
			      print("1 ", i)
