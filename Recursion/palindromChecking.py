op=0
def Palindrom(n):
    global op
    if n<10:
        op=op*10+n%10
        return
    op=op*10+n%10
    Palindrom(n//10)
num=34473
Palindrom(num)
#print(op)
if op==num:
    print("Palindrom")
else:
    print("Not a Palindrom")

