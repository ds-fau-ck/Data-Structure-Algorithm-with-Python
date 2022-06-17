def reverseANumber(n):
    if n<10:
        print(n)
        return 
    print(n%10)
    reverseANumber(n//10)
op=0
def reverseNum(n):
    global op
    if n<10:
        op=op*10+n 
        return 
    op=op*10+n%10
    reverseNum(n//10)


reverseNum(3456)
print(op)