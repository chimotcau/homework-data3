#define repeat function
def repeat(s):
    n=len(s)
    for l in range(1,n + 1):
        if n%l==0:
            m=s[:l]
            r=n//l
            if m*r == s:
                return r
    return 1
lines=[]
while True:
    line=input().strip()
    if line=='.':
        break
    lines.append(line)
for line in lines:
    print(repeat(line))