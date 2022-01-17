

# ---- 303 栈的应用：简单括号匹配  ---- #

'''
    从左到右扫描括号串.
    次序反转的识别.
    
'''


from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s=Stack()
    balanced=True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
                
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
print(parChecker('((()))'))
print(parChecker('(()'))


            