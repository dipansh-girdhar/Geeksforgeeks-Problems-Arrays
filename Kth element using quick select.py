#code
import random
t=int(input())

def kelement(a,k):
    ai=random.choice(a)
    less=[]
    more=[]
    for j in a:
        if(j<ai):
            less.append(j)
        elif(j>ai):
            more.append(j)
    
    if(len(less)==k-1):
        print(ai)
    elif(len(less)>=k):
        kelement(less,k)
    else:
        kelement(more,k-len(less)-1)
        
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    kelement(a,k)
    
    