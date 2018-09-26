f = open("dna.fasta")
data = f.readlines()
print(data)

for i in range(0,len(data),1):
        data[i]= data[i].strip('\n')

seq1 = data[1]
seq2 = data[3]

m = 5
mm = -4
g = -26

V = []
T = []

rows = len(seq1)+1
cols = len(seq2)+1

print(rows)

#make space for V
for i in range(0,rows,1):
        l = []
        l2 = []
        for j in range (0,cols,1):
            l.append(0)
            l2.append(0)
        V.append(l)
        T.append(l2)

for i in range(0,len(V), 1):
    print(V[i])
print()

##initialization
for i in range(1,rows,1):
    V[i][0] = i*g
    T[i][0] = 'U'
    print(V[i])
    print()
for i in range(1,cols,1):
    V[0][i] = i*g
    T[0][i] = 'L'
print(V)
print(T)

##Recurrence
for i in range(1,rows,1):
    for j in range(1,cols,1):
        if (seq1[i-1] == seq2[j-1]):
            d = V[i-1][j-1] + m
        else:
            d = V[i-1][j-1] + mm
        u = V[i-1][j] + g
        l = V[i][j-1] + g

        if (d >= u and d >= l):
            V[i][j] = d
            T[i][j] = "D"
        elif(u >= d and u >= l):
            V[i][j] = u
            T[i][j] = "U"
        elif(l >= u and l >= d):
            V[i][j] = l
            T[i][j] = "L"

            
##Traceback
aligned_seq1 = ""
aligned_seq2 = ""
i = len(seq1)
j = len(seq2)
while (i != 0 or j!= 0):
    if (T[i][j] == "L"):
        aligned_seq1 = '-' + aligned_seq1
        aligned_seq2 = seq2[j] + aligned_seq2
        j = j-1
    elif (T[i][j] == "U"):
        aligned_seq2 = '-' + aligned_seq2
        aligned_seq1 = seq1[i-1] + aligned_seq1
        i = i-1
    else:
        aligned_seq1 = seq1[i-1] + aligned_seq1
        aligned_seq2 = seq2[j-1] + aligned_seq2
        i = i-1
        j = j-1
print(aligned_seq1)
print(aligned_seq2) 
