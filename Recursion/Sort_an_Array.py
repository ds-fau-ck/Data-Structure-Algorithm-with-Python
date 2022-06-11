
def insert(arr, alpha):
    if len(arr)==0 or arr[-1]>alpha:
        arr.append(alpha)
        return
    val=arr.pop(-1)
    insert(arr,alpha)
    arr.append(val)


def sort_an_array(arr):
    if len(arr) ==1:
        return
    #removing the last elements
    alpha=arr.pop(-1)
    sort_an_array(arr)
    insert(arr, alpha)



in_array=[6,1,9,4,0,8,2]
sort_an_array(in_array)
print(in_array)