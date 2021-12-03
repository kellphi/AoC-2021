#reading file
from os import close


with open(r'D:\Users\Philip\OneDrive\Documents\AoC 2021\Inputs\Day1.txt') as f:
    data1 = [int(l) for l in f.readlines()]


#part 1
count1 = 0
for i in range(len(data1)-1):
  if data1[i+1]>data1[i]:
    count1+=1
  
print("Part 1:", count1)

#part 2
count2 = 0
for i in range(len(data1)-3):
  sum1 = data1[i]+data1[i+1]+data1[i+2]
  sum2 = data1[i+1]+data1[i+2]+data1[i+3]
  if sum2>sum1:
    count2 += 1

print("Part 2:", count2)