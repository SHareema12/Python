import sys
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

### Read Data ###
datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
l = f.readline()
while (l != ''):
  a = l.split()
  l2 = []
  for j in range(0, len(a), 1): 
    l2.append(float(a[j]))
  data.append(l2)
  l = f.readline()

rows = len(data)
cols = len(data[0])

### Read training labels ###
labelfile = sys.argv[2] 
f = open(labelfile) 
trainlabels = {}
n = [0,0]
l = f.readline()
while(l != ''):
  a = l.split()
  trainlabels[int(a[1])] = int(a[0])
  l = f.readline()
  n[int(a[0])] += 1

X = []
Y = []

for i in range(0,rows,1):
  if(trainlabels.get(i) != None):
    X.append(data[i])
    Y.append(trainlabels.get(i))

clf = RandomForestClassifier(n_estimators=1000)
s = clf.fit(X,Y)

for i in range(0,rows,1):
  if(trainlabels.get(i) == None):
    t = []
    t.append(data[i])
    x = clf.predict(t)
    print(x[0], i)