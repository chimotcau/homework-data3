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