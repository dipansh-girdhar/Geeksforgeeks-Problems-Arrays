#code
t=int(input())
c=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c.append(a)
res=[]
for i in c:
    final=[]
    start=0
    end=0
    flag=0
    for j in range(1,len(i)):
        if(i[j]>=i[end]):
            end=end+1
            if(end==len(i)-1):
                final.append((start,end))
                flag=1
        else:
            if(end>start):
                final.append((start,end))
                flag=1
            start=end+1
            end=end+1
    # res.append(final)
    if(flag==1):
        for k in final:
            mystring = ' '.join(map(str, k))
            print('('+mystring+')',end=' ')
        print("\t")
    else:
        print("No Profit")
# for i in res:
    
#     print(*i,sep=' ')

    