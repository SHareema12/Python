##### Support Vector Machine (SVM) classication #####
import sys
from sklearn import svm

#######################
### read data form file
#######################
f = open(sys.argv[1], "r")
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

#########################
### read labels form file
#########################
f = open(sys.argv[2], "r")
line = f.readline()
trainLabels = {}
while(line != ""):
	  l = line.split()
	  trainLabels[int(l[1])] = int(l[0])
	  line = f.readline()

d=[]
t=[]
for i in range (0,rows,1):	
    if(trainLabels.get(i) != None):
        d.append(data[i])
        t.append(trainLabels.get(i))
        
#print("data: ", d)
#print("trainlabels: ", t)

clf=svm.SVC(C=1, kernel= 'linear')
fit=clf.fit(d,t)

weights=fit.coef_
print("length of weights: ", len(weights[0]))

weights2=[]

for i in range(0, len(weights[0], 1):
    weights2.append(math.fabs(weights[0][i]))

sorted_weights = sorted(weights2, reverse=True)

fh = open("ranked_wights.txt", "w")
for i in range(0, len(sorted_weights), 1):
    fh.write(str(sorted_weights[i]) + "\n")
    fh.write("")
fh.close()

### prediction
for i in range(0,rows,1):
    if(trainLabels.get(i) == None):
        test=[]
        test.append(data[i])
        testlabels=clf.predict(test)
        #print(testlabels[0],i)
        print(testlabels[0], i-len(trainlabels))
