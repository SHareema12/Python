import random

f = open("dna.fasta")
data = f.readlines()
print (data)

##taking off ''\n' at the end of each word
for i in range(0,len(data),1):
    data[i] = data[i].strip('\n')

##Extract sequences- all even lines of data
dataArray = []
for i in range(1,len(data), 2):
    dataArray.append(data[i])
print (dataArray)

##Declare array containing number of leaf nodes that we will randomize
items = []
for i in range(0,len(dataArray),1):
    items.append(i)
print (items)

##Randomize numbers in list to pick
random.shuffle(items)

print(items) 

##Initialize S array, L array, and R array, declare P array
##Initialize leafNodes, totalNodes
P = []
S = []
L = []
R = []

leafNodes = len(dataArray)
totalNodes = (2*leafNodes)-1

##Initialize S array with sequences first
for i in range(0,len(dataArray),1):
    S.append(dataArray[i])
print (S)

##Fill rest of S with empty string ''
x = totalNodes-leafNodes
print(x)
for j in range(0, totalNodes-leafNodes, 1):
    S.append('')
print("S:", S)

##Initialize L and R values with -1
for i in range(0,leafNodes,1):
    L.append(-1)
    R.append(-1)

##Initialize remaining spots of L and R with empty strings
for i in range(0, totalNodes-leafNodes,1):
    L.append('')
    R.append('')
print("L:", L)
print("R:", R)

##Initialize P with empty string values
for i in range(0,totalNodes,1):
    P.append('')
print("P:", P)

##Generating Random Tree
nextPnode = leafNodes 
while(len(items)>1):
    print("Items before: ", items)
    nodeL = items.pop()
    nodeR = items.pop()
    print("nodeL:", nodeL)
    print("nodeR:", nodeR)
    L.pop(nextPnode)
    L.insert(nextPnode,nodeL)
    R.pop(nextPnode)
    R.insert(nextPnode,nodeR)
    P.pop(nodeL)
    P.insert(nodeL,nextPnode)
    P.pop(nodeR)
    P.insert(nodeR,nextPnode)
    items.append(nextPnode)
    random.shuffle(items)
    nextPnode += 1
    print("New Items:", items)

##Assign last node-aka root's parent as -1
root = items.pop()
P.pop(root)
P.insert(root, -1)

print("P:", P)
print("L:", L)
print("R:", R)

T = [P,L,R,S]

