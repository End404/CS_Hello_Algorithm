

# ---- 303 栈的应用：更多种括号的匹配  ---- #

'''
    从左到右扫描括号串.
    次序反转的识别.
    
    ❖在实际的应用里，我们会碰到更多种括号: 
        如python中列表所用的方括号“[]” .
        字典所用的花括号“{}” .
        元组和表达式所用的圆括号“()” .
    
'''

'''
    通用括号匹配算法：代码
    ❖ 需要修改的地方: 
        碰到各种左括号仍然入栈. 
        碰到各种右括号的时候需要判断栈顶的左括号是否跟右括号属于同一种类. 

'''


from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
                
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return open.index(open) == closers.index(close)

print(parChecker('((()))'))
print(parChecker('(()'))



