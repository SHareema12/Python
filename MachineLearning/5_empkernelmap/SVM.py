import sys
from sklearn import svm

#####Read data######
#datafile = sys.argv[1]
#f = open(datafile, 'r')
#data = []
#l = f.readline()
#while(l != ''):
#  a = l.split()
#  l2 = []
#  for j in range(0,len(a),1):
#    l2.append(float(a[j]))
#  data.append(l2)
#  l = f.readline()

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

####Read training labels####
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0,0]
l = f.readline()
while (l != ''):
#  print ("l:", l)
  a = l.split()
#  print ("a:", a)
  trainlabels[int(a[1])] = int(a[0])
  l = f.readline()
  n[int(a[0])] += 1

c = float(sys.argv[3])

X = []
Y = []

for i in range(0, rows, 1):
  if(trainlabels.get(i) != None):
    X.append(data[i])
    Y.append(trainlabels.get(i))

clf = svm.SVC(C=c, kernel = 'linear')
s = clf.fit(X,Y) 

for i in range(0, rows, 1):
  if(trainlabels.get(i) == None):
    t = []
    t.append(data[i]) 
    x = clf.predict(t)
    print(x[0],i)