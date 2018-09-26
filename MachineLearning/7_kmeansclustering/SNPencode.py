import sys
import numpy as np

###Take in input SNP file and encode each SNP genotype into its number of copies of MINOR allele
snps = []
f = open(sys.argv[1],'r')
line = f.readline()
while(line != ""):
  a = []
  x = line.split()
  for i in range(0,len(x),1):
    a.append(x[i])
  snps.append(a)
  line = f.readline()

#print("Input", snps)

#### Encode each SNP by going through each column 
allele_count = {}
rows = len(snps)
cols = len(snps[0]) 
#print("rows: ", rows)
#print ("cols: ", cols)
ch1 = 'x'
ch2 = 'y'
count1 = 0
count2 = 0
allele1 = 'a'
allele2 = 'b'
### Loop to count each  
for j in range(1,cols,1):
  allele1 = 'a'
  allele2 = 'b'
  count1 = 0
  count2 = 0
  for i in range(0,rows,1):
    pair = snps[i][j]
#    print ("pair:", pair)
    ch1 = pair[0]
    ch2 = pair[1]
    ## both the same allele 
    if (ch1 == ch2):
#      print("hi, both alleles same, alleles may need to be assigned", ch1, ch2)
      if(allele1 == 'a' and allele2 == 'b'):
        allele1 = ch1
        count1 += 2
      if (allele1 != 'a' and allele2 == 'b'):
        if(allele1 != ch1):
          allele2 = ch1
          count2 += 2
      if(allele1 == ch1):
        count1 += 2
      if(allele2 == ch1):
        count2 += 2 
    ## alleles are different 
    elif (ch1 != ch2):
#      print("both alleles different", ch1, ch2)
      ## no alleles have been assigned
      if(allele1 == 'a' and allele2 == 'b'):
        allele1 = ch1
        allele2 = ch2
      ## one allele has been assigned, need to assign the other
      elif(ch1 == allele1 and allele2 == 'b'):
        allele2 = ch2
      elif (ch1 != allele1 and allele2 == 'b'):
        allele2 = ch1        
      count1 += 1
      count2 += 1
#    print("Column: ", j, "Row: ", i, "Allele 1 = ", allele1, " Allele 2 = ", allele2)
#    print("Count1: ", count1, " Count 2" , count2)
#    print("Column: ", j, "Row: ", i, "Allele:", allele1, " count: ", count1)
#    print("Column: ", j, "Row: ", i, "Allele:", allele2, " count: ", count2)
  ### figure out which allele is minor 
  if (count1 <= count2):
    allele_count[j] = allele1 
  else: 
    if(allele2 == 'b'):
      allele_count[j] = '-'
    else:
      allele_count[j] = allele2

#print("Allele counts:", allele_count) 

### now we go through hapmap, and change data to number of minor allele that we computed above 
minAllele_count = 0
for j in range(1,cols,1):
  for i in range(0,rows,1):
    minAllele_count = 0
    minor_allele = allele_count[j]
    pair = snps[i][j]
    ch1 = pair[0]
    ch2 = pair[1]
    if (minor_allele == '-'):
      minAllele_count = 0  
    if (ch1 == minor_allele):
      minAllele_count += 1
    if (ch2 == minor_allele):
      minAllele_count += 1
    snps[i][j] = minAllele_count

for i in range(0,rows,1):
  for j in range(0,cols,1):
    print(snps[i][j], end =" ")
  print()