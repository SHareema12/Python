import sys

### to run do: pythong cluseringerror.py true_labels predicted_labels

##Read true labels from file 
true_labels = {}
f = open(sys.argv[1], 'r')
line = f.readline()
while(line != ""):
    l = line.split()
    true_labels[int(l[1])] = int(l[0])
    line = f.readline()

#print("True labels hash table:", true_labels)--works 

T = []
### Checking each pair's labels compared to one another
keys = list(true_labels.keys())
for i in range(0,len(keys),1):
  l = []
  for j in range(0,len(keys),1):
    if(true_labels[keys[i]] == true_labels[keys[j]]):
      l.append(1)
    else:
      l.append(0)
    T.append(l)

##Read predicted labels from file 
predicted_labels = {}
f = open(sys.argv[2], 'r')
line = f.readline()
while(line != ""):
  l = line.split()
  predicted_labels[int(l[1])] = int(l[0])
  line = f.readline()

print("Predicted labels hash table:", predicted_labels)
C = []
keys = list(predicted_labels.keys()) 
for i in range(0, len(keys),1):
  l = []
  for j in range(0,len(keys),1):
    if(predicted_labels[keys[i]] == predicted_labels[keys[j]]):
      l.append(1)
    else:
      l.append(0)
    C.append(l)

##Determine the number of misclassified points (divided by total test points)

allkeys = list(predicted_labels.keys())
total = 0
error = 0
for i in range(0,len(allkeys),1):
  for j in range(i+1,len(allkeys),1):
    if(T[i][j] != C[i][j]):
      error += 1
    total += 1

error = error/total
print("Clustering error: ",100*error,"%")
print("Clustering accuracy: ",100-100*error,"%")