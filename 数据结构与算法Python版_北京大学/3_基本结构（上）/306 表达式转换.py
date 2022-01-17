

# -*- 306 表达式转换 -*- #
#通用的中缀转后缀算法


from pythonds.basic.stack import Stack

#记录操作符优先级
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()    #解析表达式到单词列表
    
    #从左到右进行扫描
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":    #操作数
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:   #操作符
            while (not opStack.isEmpty()) and \ (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())    #操作符
    return " ".join(postfixList)    #合成后缀表达式字符串
                  



                  