"""Trailing Zeros"""
 
n=int(input())
 
cnt=0
while n>=5:
    n//=5
    cnt+=n
    
print(cnt)
