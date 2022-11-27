openList = ["[", "{", "(", "<"]
closeList = ["]", "}", ")", ">"]

def balance(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            if i == "<" and stack[-1] == "(":
                    continue
            stack.append(i)
        elif i in closeList:
            if i == ">" and stack[-1] == "(":
                    continue
            pos = closeList.index(i)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Brackets incorrecly nested "

    if len(stack) == 0:
        return "Brackets correcly nested"
    
