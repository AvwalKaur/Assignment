# Print first n fibonacci numbers
def fibo(n):
    a=0
    b=1
    for i in range(1,n+1):
        print(a)
        c=a+b
        a=b
        b=c
# print first five fibonacci numbers
fibo(5)

