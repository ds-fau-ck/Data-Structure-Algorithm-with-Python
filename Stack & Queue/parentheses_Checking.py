def askParenthesesChecking(exp):
    stak=[]
    for char in exp:
        if char in ['(','{','[']:
            stak.append(char)
        elif char in [')','}',']']:
            alpha=stak.pop()
            if stak=='(':
                if char !=')':
                    return False  
            if stak=='{':
                if char !='}':
                    return False 
            if stak=='[':
                if char !=']':
                    return False 
    if stak:
        return False 
    return True 
exp="{()[](())}"
flag=askParenthesesChecking(exp)
print(flag)


        
        
