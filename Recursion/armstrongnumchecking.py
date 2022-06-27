lenV=0
def lengthofNumber(num):
    global lenV
    if num <10:
        lenV=lenV+1
        return
     
    lenV =lenV+1
    lengthofNumber(num//10) 
val=0
def armstrongNumber(num, lenV):
    global val
    if num<10:
        val=val+(num%10)**lenV
        return
    
    val=val+(num%10)**lenV
    armstrongNumber(num//10,lenV)
num=153
lengthofNumber(num)
armstrongNumber(num, lenV)
if val==num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")