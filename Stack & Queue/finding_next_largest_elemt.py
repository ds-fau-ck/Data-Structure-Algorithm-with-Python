def find_NGR(arr):
    op=[]
    stk=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stk)==0:
            op.append(-1)
        elif stk[-1]>arr[i]:
            op.append(stk[-1])
        else:
            while len(stk)>0 and stk[-1]<arr[i]:
                stk.pop(-1)
            if len(stk)==0:
                op.append(-1)
            else:
                op.append(stk[-1])
        stk.append(arr[i])
    op.reverse()
    return op
arr=[1,3,2,4]
res=find_NGR(arr)
print(res)