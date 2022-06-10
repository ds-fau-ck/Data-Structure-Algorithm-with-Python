out_stack=[]
def reverseStack(in_stack):
    if len(in_stack)==1:
        out_stack.append(in_stack[0])
        return 
    alpha=in_stack.pop(-1)
    out_stack.append(alpha)
    reverseStack(in_stack)
input_stack=[1,2,3,4,5,6,7]
reverseStack(input_stack)
print(out_stack)
