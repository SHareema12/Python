import sys
import numpy as np
import random
from sklearn.cluster import KMeans
import os

print("Working..may take a few minutes")

### Encode snps via a system call ### 
file = sys.argv[1] 
cmd = 'python SNPencode.py ' + file + ' > encodedSNP'
os.system(cmd)

### Take in input of encoded SNP file ###
data_withLabels = []
f = open("encodedSNP",'r')
line = f.readline()
while(line != ""):
  a = []
  x = line.split()
  for i in range(0,len(x),1):
    a.append(x[i])
  data_withLabels.append(a)
  line = f.readline()

true_labels = 'python extractTrueLabels.py > true_labels'
os.system(true_labels)

data_noLabels = []
for i in range(0,len(data_withLabels),1):
  x = []
  for j in range(1,len(data_withLabels[0]),1):
    x.append(data_withLabels[i][j])
  data_noLabels.append(x)

#for i in range(0,len(data_noLabels),1):
#  print(data_noLabels[i])
  
kmeans=KMeans(n_clusters=2, random_state=0).fit(data_noLabels)
print("kmean: ", kmeans)
#cluster_centers = kmeans.cluster_centers_
#print(kmeans.cluster_centers_)
labels = kmeans.labels_
#print(labels)

predicted_labels = open("predicted_labels",'w') 
for i in range(0,len(labels),1):
  if (labels[i] == 0):
    labels[i] = 2
  z = str(labels[i])
  y = z + " " + str(i)
  predicted_labels.write(y + '\n')

#print(labels)

## Testing to see if predicted_labels can be accessed 
predicted_labels = {}
f = open("predicted_labels", 'r')
line = f.readline()
while(line != ""):
  l = line.split()
  predicted_labels[int(l[1])] = int(l[0])
  line = f.readline()

#print("Predicted labels hash table:", predicted_labels)
  
cluster_error = 'python clusteringerror.py true_labels predicted_labels'
os.system(cluster_error) 