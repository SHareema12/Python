import sys 
import math

######
##Read data from file 
datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
i = 0
l = f.readline()
while(l != ''):
  a = l.split()
  l2 = []
  for j in range(0,len(a),1):
    l2.append(float(a[j]))
  data.append(l2)
  l = f.readline()

rows = len(data) 
cols = len(data[0]) 

##Read labels from file 
trainlabelfile = sys.argv[2]
l = open(trainlabelfile, 'r')
trainlabels = {}
f = l.readline()
while(f != ''):
  a = f.split()
  trainlabels[int(a[1])] = int(a[0])
  f = l.readline()

##### nearest mean #####
### compute means ###

n_m_neg1 = []
for i in range(0, cols, 1):
  n_m_neg1.append(0.00000001)

n_m1 = []
for i in range(0, cols, 1):
  n_m1.append(0.00000001)
  
n_neg1 = 0
n1 = 0 

for i in range(0, len(data), 1):
  if(trainlabels.get(i) != None and trainlabels[i] == -1):
    n_neg1 += 1
    for j in range(0, cols, 1):      
      n_m_neg1[j] += data[i][j]

  if(trainlabels.get(i) != None and trainlabels[i] == 1):
    n1 += 1
    for j in range(0, cols, 1):
      n_m1[j] += data[i][j]

for j in range(0, cols, 1):
  n_m_neg1[j] /= n_neg1
  n_m1[j] /= n1
#  n_m_neg1[j] = n_m_neg1[j]/class_size[0] ## mean
#  n_m1[j] = n_m1[j]/class_size[1] ## mean

#print("mean:")
#print("n_m1: ", n_m1)


### prediction

for i in range(len(data)):
  d_neg1 = 0
  d1 = 0
  if(trainlabels.get(i) == None):
    for j in range(0, cols, 1):
      d_neg1 += ((data[i][j] - n_m_neg1[j]))**2
      d1 += ((data[i][j] - n_m1[j]))**2
    if(d_neg1<d1):
      print("-1 ", i-len(trainlabels))
    else:
      print("1 ", i-len(trainlabels))