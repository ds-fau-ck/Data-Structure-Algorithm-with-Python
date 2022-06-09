def factorialwithIterative(n):
    f=1
    for i in range(n,0,-1):
        f=f*i  
    return f 
n=5
fact=factorialwithIterative(5)
print(fact)