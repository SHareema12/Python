import sys

### Import data
data = []
f = open("encodedSNP",'r')
line = f.readline()
while(line != ""):
  a = []
  x = line.split()
  for i in range(0,len(x),1):
    a.append(x[i])
  data.append(a)
  line = f.readline()
  
for i in range(0,len(data),1):
  print(str(data[i][0]), str(i), end =" ")
  print()  