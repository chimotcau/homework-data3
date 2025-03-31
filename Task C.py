#input A,B,C
A,B,C=map(int,input().split())
current=set()
current.add(1)
p=1
for i in range(1,2000001):
    p=(A*p+(p%B))%C   
    if p in current:  
        print(i)
        exit()
    current.add(p)
print("-1")  