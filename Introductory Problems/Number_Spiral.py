"""Number Spiral"""

n=int(input())
res=[]
for _ in range(n):
    x,y=[int(e) for e in input().split()]
    if x>y:
        if x%2==0:
            num=(x**2)-(y-1)
        else:
            num=(((x-1)**2)+1)+(y-1)
    elif x<y:
        if y%2==0:
            num=(((y-1)**2)+1)+(x-1)
        else:
            num=(y**2)-(x-1)
    else:
        num=(x**2)-x+1
    print(num)
