def solution(s):
    s_list = list(s)
    stack = []

    for op in s_list:
        if op == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True