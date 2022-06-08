def printNumber(n):
    if n==1:
        print(1)
        return  
    printNumber(n-1)
    print(n)
printNumber(100)
    