# 1+1/(1+(1^2))+......1/(n^2+(n-1)^2+......+1)

def square(n):
    if n>0:
        return n**2+square(n-1)
    else:
        return 0
        
def add(n):
    sum_=0
    for i in range(1,n+1):
        sum_=sum_+(1/square(n))
        n=n-1
    print(sum_)
   

# Euler's number evaluation

def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1

def e(n):
    sum_=1
    for i in range(1,n+1):
        sum_+=(1/factorial(n))
        n=n-1
    print(sum_)
