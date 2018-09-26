import sys
import random
import math

### read data and labels from file
datafile=sys.argv[1]
all_data=open(datafile, 'r')
trainlabelfile=sys.argv[2]
trainlabels_data=open(trainlabelfile, 'r')



data=[]
train_label=[]

for line in all_data:
    row=[float(num)for num in line.split()]
    data.append(row)
    train_label.append(0)
    
#assign labels
for line in trainlabels_data:
    t=[float(num) for num in line.split()]
    train_label[int(t[1])]=t[0]


rows=len(data)
cols=len(data[0])

#-------------------------------#
##compute Y mean
sum=0
for i in range(0,len(train_label),1):
    sum=sum+train_label[i]
ymean=sum/len(train_label)


#-------------------------------#
##compute X mean
maxlen = len(max(data, key = len))
#print("maxlen: ", maxlen)
for l in data:
    if len(l) < maxlen:
        numzero = maxlen - len(l)
        l.append(numzero * 0.00001)
#print("data: ", data)
        
Xsum=[]
Xmean=[]
extra_num=0
for i in range(0, maxlen, 1):
    n=0
    col_sum = 0
    for innerlist in data:
        n+=1
        if innerlist[i] == 0.00001:
            extra_num +=1
            continue
        col_sum += innerlist[i]
    #print("col_sum: ", col_sum)
    Xsum.append(col_sum)
    Xmean.append(col_sum / (n - extra_num))
#print("Xsum: ", Xsum)
#print("Xmean: ", Xmean)

##-------------compute r---------------------
#(1)compute (Xi-Xmean)(Yi-Ymean)
#(2)compute (Xi-Xmean)** (Yi-Ymean)**

r=[]
fenzi=[]
fenmu1=[]
fenmu2=[]
fenmu=[]
r_values = {}
for i in range(0, cols, 1):
    r.append(0)
    fenzi.append(0)
    fenmu1.append(0)
    fenmu2.append(0)
    fenmu.append(0.00000001)
    
for i in range(0,cols,1):
    for j in range(0,rows,1):
        if data[j][i] == 0.00001:
            continue
        fenzi[i]+=(data[j][i]-Xmean[i])*(train_label[j]-ymean)
        fenmu1[i]+=(data[j][i]-Xmean[i])**2
        fenmu2[i]+=(train_label[j]-ymean)**2
        if(fenmu1[i]==0 or fenmu2[i]==0):
            fenmu1[i]=0.000000000001
            fenmu2[i]=0.000000000001
        fenmu[i]=math.sqrt(fenmu1[i]*fenmu2[i])
    r[i]=fenzi[i]/fenmu[i]
    r_values[r[i]] = i


#----------------------choose top K----------------------
#rank r
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] < lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

bubble_sort(r)
#print("sort r: ", r)

#choose top features, number=k
k=int(sys.argv[3])
feature=[]
topfeatures=[]
for i in range(0, k, 1):
    feature.append(0)
    feature[i]=r[i]
    #print("Feature number ", i+1, ": Column ",r_values.get(feature[i]))
    topfeatures.append(r_values.get(feature[i]))

data2=[]
index=-1
a =[]
for i in range(0, rows, 1):
    a=[]
    for j in range(0, len(topfeatures), 1):
        #print("column to keep: ", topfeatures[j])
        a.append(data[i][topfeatures[j]])
    data2.append(a)
#print(data2)

for i in data2:
    for j in i:
        print(j, "", end = '')
    print()
