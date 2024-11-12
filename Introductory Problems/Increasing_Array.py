"""Increasing Array"""
 
n=int(input())
ip=[int(e) for e in input().split()]
 
count=0
for i in range(len(ip)-1):
    if ip[i]>ip[i+1]:
        count+=ip[i]-ip[i+1]
        ip[i+1]=ip[i]
        
print(count)
