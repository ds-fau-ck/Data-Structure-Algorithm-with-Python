def factorialwithIterative(n):
    f=1
    for i in range(n,0,-1):
        f=f*i  
    return f 
def factorial_recursive(n):
    if n==1:
        return 1 
    return n*factorial_recursive(n-1)
n=5
fact=factorialwithIterative(n)
fact2=factorial_recursive(n)
print(fact2)
print(fact)