
#*******************************#
#
#   ---606 树的应用：表达式解析（下）---
#       --建立表达式解析树--
#
#*******************************#



def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)      #入栈下降
    currentTree = eTree
    for i in fplist:
        if i == "(":        #表达式开始
            currentTree.insertLeft('')
            pStack.push(currentTree)        #入栈下降
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', "-", '*', '/', ')']:    #操作数
            currentTree.setRootVal(int(i))
            parent = pStack.pop()       #出栈上升
            currentTree = parent
        elif i in ['+', '-', '*', '/']:     #操作符
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':      #表达式结束
            currentTree = pStack.pop()      #出栈上升
        else:
            raise ValueError
    return eTree


#**********************************************
#==============================================
# 一个增加程序可读性的技巧：函数引用
import operator

op = operator.add
n = op(1,2)
print(n)
o = operator.add(1,2)
print(o)
print()
#===============================================

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, \
            '*':operator.mul, '/':operator.truediv}
        
        #缩小规模
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))        #递归调用
    else:
        return parseTree.getRootVal()       #基本结束条件


#************************************************


