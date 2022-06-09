out_array=[]# using extra space here
def reverese_array_extra_space(in_array):
    if len(in_array)==1:
        out_array.append(in_array[0])
        return
    reverese_array_extra_space(in_array[1:])
    out_array.append(in_array[0])

def reverse_array_inspace(in_array):
    if len(in_array)==1:
        return
    alpha=in_array.pop(0)
    reverse_array_inspace(in_array)
    in_array.append(alpha)
in_array=[1,2,3]
reverese_array_extra_space(in_array)
print(f"Reverse_array_using_extra_space:{out_array}")
reverse_array_inspace(in_array)
print(f"Reverse_array_using_inspace:{in_array}")