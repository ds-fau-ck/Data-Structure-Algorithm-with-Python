def reverseANumber(n):
    if n<10:
        print(n)
        return 
    print(n%10)
    reverseANumber(n//10)
reverseANumber(3456)