#define repeat function
def repeat(s):
    n=len(s)
    for l in range(1,n//2+1):
        if n%l==0:
            m=s[:l]
            valid=True
            r=n//l
            for i in range(l, n, l):
                if s[i:i+l]!=m:
                    valid=False
                    break
            if valid:
                return n // l
    return 1
lines=[]
while True:
    line=input().strip()
    if line=='.':
        break
    lines.append(line)
for line in lines:
    print(repeat(line))