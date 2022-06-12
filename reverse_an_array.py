out_array=[]

def reverse_array(arr):
    if len(arr)==1:
        out_array.append(arr[0])
        return
    reverse_array(arr[1:])
    out_array.append(arr[0])


ip_array=[1,2,3,4,5,6,7,8]
reverse_array(ip_array)
print(out_array)