"""Repetitions"""
 
word=input()
 
res,count=0,1
for i in range(len(word)-1):
    if word[i]==word[i+1]:
        count+=1
    else:
        res=max(res,count)
        count=1
res=max(res,count)
        
print(res)
