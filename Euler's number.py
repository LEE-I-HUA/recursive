# 1+1/(1+(1^2))+......1/(n^2+(n-1)^2+......+1)

def square(n):
    if n>0:
        return n**2+square(n-1)
    else:
        return 0
        
def add(n):
    sum_1=0
    for i in range(1,n+1):
        sum_1=sum_1+(1/square(n))
        n=n-1
    return sum_1
   

# Euler's number evaluation

def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1

def e(n):
    sum_2=1
    for i in range(1,n+1):
        sum_2+=(1/factorial(n))
        n=n-1
    return sum_2

def main():
    n = int(input("please enter n: "))
    print(add(n))
    print("Euler's number is equal to ", e(n))

if __name__ == '__main__' :
    main()
