import sys
from sklearn.feature_selection import f_regression

##################
### Read data ####
##################
datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
l = f.readline()
while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])

#print("rows: ", rows)

###########################
### Read training labels ##
###########################
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
 
#### Read in test data ####
datafile = sys.argv[3]
f = open(datafile, 'r')
testdata = []
l = f.readline()
while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	testdata.append(l2)
	l = f.readline()
 
testlen = len(testdata)

k = int(sys.argv[4])

X = []
Y = []
for i in range(0, rows, 1):
	if(trainlabels.get(i) != None):
		X.append(data[i])
		Y.append(trainlabels.get(i))		

#print("rows of X: ", len(X))
#print("rows of Y: ", len(Y))

### Append dummy row of 1's to prevent 0 mean and variance ###
dummyrow = []
for i in range(0, cols, 1):
	dummyrow.append(1)

X.append(dummyrow)
Y.append(0)

#print("rows of X after: ", len(X))
#print("rows of Y after: ", len(Y))
#
#for i in range(0,len(X),1):
#  print(len(X[i]))

return_value = f_regression(X,Y)

templist = return_value[0]
#print(templist)
Pearson = {}
index=[]
for i in range(0, len(templist), 1):
	Pearson[i] = templist[i]
	index.append(i)

#sortedindex = sorted(index, key=Pearson.__getitem__)
sortedindex = sorted(index, key=Pearson.__getitem__, reverse=True)

#for i in range(0, k, 1):
#        print(sortedindex[i])
#        
#exit(0)

datatopK = []
for i in range(0, rows, 1):
	templ = []
	for j in range(0, k, 1):
		templ.append(data[i][sortedindex[j]])
	datatopK.append(templ)

for i in range(0,testlen, 1):
	templ = []
	for j in range(0, k, 1):
		templ.append(testdata[i][sortedindex[j]])
	datatopK.append(templ)

for i in range(0, len(datatopK), 1):
	for j in range(0, k, 1):
		print(datatopK[i][j], end=" ")
	print()