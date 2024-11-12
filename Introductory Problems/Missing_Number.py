"""Missing Number"""
 
n=int(input())
num=sorted([int(e) for e in input().split()])
 
for i in range(len(num)):
    if i+1!=num[i]:
        print(i+1)
        exit()
        
print(n)
