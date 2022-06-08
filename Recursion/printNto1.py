def printNumberNToOne(n):
    if n==1:
        print(1)
        return
    print(n)
    printNumberNToOne(n-1)
print(printNumberNToOne(8))