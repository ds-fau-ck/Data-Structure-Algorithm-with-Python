out_array=[]
def reverse_array(arry):
    if len(arry)==1:
        out_array.append(arry[0])
        return
    reverse_array(arry[1:])
    out_array.append(arry[0])
def reverse_array_without_using_extra_space(array):
    if len(array)==1:
        return
    alpha=array.pop(0)
    reverse_array_without_using_extra_space(array)
    array.append(alpha)




in_array=[8,3,5,9,0,6]
reverse_array_without_using_extra_space(in_array)
print(in_array)