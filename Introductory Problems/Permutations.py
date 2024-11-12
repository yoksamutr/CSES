"""Permutations"""
 
n=int(input())
 
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
elif n==4:
    print(2,4,1,3)
else:
    lt=[int(e) for e in range(1,n+1)]
    res=[0]*n
    if n%2==0:
        res[::2]=lt[:n//2]
        res[1::2]=lt[n//2:]
    else:
        res[:n//2+1]=lt[::2]
        res[n//2+1:]=lt[1::2]
    print(*res)
