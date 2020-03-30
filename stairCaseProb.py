def fib(n):
    a,b=1,2
    c=a+b
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    for i in range(2,n):
        c = a+b
        a = b
        b = c
    return c
print(fib(4))