out_stack=[]

def reverse_stack(in_stack):
    if len(in_stack)==1:
        out_stack.append(in_stack[0])
        return
    alpha=in_stack.pop(-1)
    out_stack.append(alpha)
    reverse_stack(in_stack)


in_stack=[3,4,5,6,7]
reverse_stack(in_stack)
print(out_stack)
    