"""Distinct Numbers"""
 
n=int(input())
num=[int(e) for e in input().split()]
 
cnt=1
num.sort()
for i in range(len(num)-1):
    if num[i]!=num[i+1]:
        cnt+=1
print(cnt)
