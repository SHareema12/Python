import sys

################################################
### pthyon error.py true_labels predicted_labels
################################################

##############################
### read true lables from file
##############################
true_labels = {}
f = open(sys.argv[1], 'r')
line = f.readline()
while(line != ""):
	  ln = line.split()
	  true_labels[int(ln[1])] = int(ln[0])
	  line = f.readline()

###################################
### read predicted lables from file
###################################
predicted_labels = {}
f = open(sys.argv[2], 'r')
line = f.readline()
while(line != ""):
    ln = line.split()
    predicted_labels[int(ln[1])] = int(ln[0])
    line=f.readline()

###############################################################################
### determine the number of misclassified points (divided by total test points)
###############################################################################
allkeys = list(predicted_labels.keys())
error_neg1 = 0
error1 = 0
n_neg1 = 0
n1 = 0
for i in range(0, len(allkeys), 1):
    if(true_labels[allkeys[i]] == -1):
        n_neg1 += 1
        if(predicted_labels[allkeys[i]] == 1):
            error_neg1 += 1
    if(true_labels[allkeys[i]] == 1):
        n1 += 1
        if(predicted_labels[allkeys[i]] == -1):
            error1 += 1

error_neg1=error_neg1/n_neg1
error1=error1/n1
error=(error_neg1+error1)/2
print("Error:", 100*error)
print("Accuracy:", 100-(100*error))