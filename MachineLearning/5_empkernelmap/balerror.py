import sys

###################
##To run do: python error.py true_labels predicted_labels
###################

######################
## Read true labels from file
######################
true_labels = {}
f = open(sys.argv[1], 'r')
line = f.readline()
while(line != ""):
    l = line.split()
    true_labels[int(l[1])] = int(l[0])
    line = f.readline()

######################
## Read predicted labels from file
######################
predicted_labels = {}
f = open(sys.argv[2], 'r')
line = f.readline()
while(line != ""):
    l = line.split()
    predicted_labels[int(l[1])] = int(l[0])
    line = f.readline()

#######################
## Determine the number of misclassified points (divided by total test points)
#######################

allkeys = list(predicted_labels.keys())
error0 = 0
error1 = 0
n0 = 0
n1 = 0
for i in range(0, len(allkeys), 1):
    if(true_labels[allkeys[i]] == 0):
        n0 += 1
        if(predicted_labels[allkeys[i]] == 1):
            error0 += 1
    if(true_labels[allkeys[i]] == 1):
        n1 += 1
        if(predicted_labels[allkeys[i]] == 0):
            error1 += 1

error0 = error0/n0
error1 = error1/n1
error = (error0 + error1)/2
print(100*error)