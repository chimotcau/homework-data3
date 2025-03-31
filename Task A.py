import math
#input n and k
n,k=map(int,input().split())
#input coordinates
station=[]
for i in range(n):
    x, y = map(int, input().split())
    station.append((x, y))
#print(station[0][0])
distances=[]
for i in range(n):
    for j in range(i+1,n):
        ox=station[i][0]-station[j][0]
        oy=station[i][1]-station[j][1]
        dxy=math.sqrt(ox*ox+oy*oy)
        distances.append((dxy,i,j))
distances.sort() 
#find root of each station
parent = [i for i in range(n)] #set each station is its own parent
def find(r):
    while parent[r] !=r: 
        parent[r]=parent[parent[r]] #trivial to the topmost node
        r=parent[r] #set that node to be it parent in line 20    
    return r  
#minimum spanning tree
minpath=[]
for distance in distances:
    d,x,y=distance
    x_root=find(x)
    y_root=find(y)
    if (x_root != y_root): #to not create cycle in mst
        parent[y_root]=x_root #set the parent of new node is the previous node
        minpath.append(d)
if k==0:
    d = minpath[-1]
elif k >=n:
    d=0
else:
    d=minpath[n-k-1]
print("{0:.2f}".format(d))         
        
    


                 

           

