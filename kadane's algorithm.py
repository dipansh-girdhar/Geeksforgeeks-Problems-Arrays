t=int(input())
c=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c.append(a)

for i in c:
    max_end_here=0
    max_so_far=0
    for j in i:
        max_end_here=max_end_here + j
        if(max_end_here<0):
            max_end_here=0
        if(max_so_far<max_end_here):
            max_so_far=max_end_here
    if(all(k < 0 for k in i)):
        print(max(i))
    else:
        print(max_so_far)