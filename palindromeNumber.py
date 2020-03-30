n = int(input())
if n<0:
    print(False)
    exit()
k = n
s = 0
while k/10!=0:
    s = (s*10) + (k%10)
    print(s)
    k//=10
if s==n:
    print(True)
else:
    print(False)