lenV=0
def lengthofNum(num):
    global lenV
    if num<10:
        lenV=lenV+1
        return
    lenV=lenV+1  
    lengthofNum(num//10)

num=153
lengthofNum(num)
value=0
def armstrongValue(num, lenV):
    global value 
    if num<10:
        value=value+(num%10)**lenV
        return

    value=value+(num%10)**lenV
    armstrongValue(num//10, lenV)


if value==num:
    print(f'Yes this num : {num} is an armstrong number.')
else:
    print(f'Yes this num: {num} is not an armstrong number.')