

# -*- 307 后缀表达式求值 -*- #

"""

    ❖跟中缀转换为后缀问题不同，
❖在对后缀表达式从左到右扫描的过程中，
❖由于操作符在操作数的后面，
❖所以要暂存操作数，在碰到操作符的时候
，再将暂存的两个操作数进行实际的计算
仍然是栈的特性：操作符只作用于离它最近的两
个操作数

"""

'''
后缀表达式求值：流程
    ❖ 创建空栈operandStack用于暂存操作数
    
    ❖ 将后缀表达式用split方法解析为单词（token）的列表
    
    ❖ 从左到右扫描单词列表
        如果单词是一个操作数，将单词转换为整数int，
    压入operandStack栈顶.
        
        如果单词是一个操作符（*/+-），就开始求值，
    从栈顶弹出2个操作数，先弹出的是右操作数，后弹出的
    是左操作数，计算后将值重新压入栈顶
    
    ❖ 单词列表扫描结束后，表达式的值就在栈顶
    
    ❖ 弹出栈顶的值，返回。
'''


from pythonds.basic.stack import Stack

def postfiEcal(postfixExpr):
    operandStack = Stack()
    toekenList = postfixExpr.split()
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))     #操作数
        else:
            operand2 = operandStack.pop()    #操作符
            operand1 = operandStack.pop()    #操作符
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    

