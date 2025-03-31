#define repeat function KMP algorithms
def repeat(s):
    n=len(s)
    if n==0: 
        return 0
    p=[0]*n
    j=0  
    for i in range(1, n):
        while j>0 and s[i]!=s[j]: #each letter in repetition start with s[0] 
            j=p[j-1]
        if s[i]==s[j]:
            j+= 1
            p[i]=j
#calculate the repetiton:            
    l=n-p[-1]
    if n%l==0:
        return n//l
    return 1
lines = []
while True:
    line = input().strip()
    if line == '.':
        break
    lines.append(line)
for line in lines:
    print(repeat(line))
