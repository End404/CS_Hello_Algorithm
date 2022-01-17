
#*******************************#
#
#   ---607_树的遍历---
#       --递归算法--
#
#*******************************#



#
def perorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLdftChild())
        preorder(tree.getRightChild())


# 后序和中序遍历，仅需要调整顺序
def perorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


#============================================
#BinaryTree类中实现前序遍历的方法：需要加入子树是否为空的判断。
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()


#===========================================
#后序遍历：表达式求值
def postordereval(tree):
    opers = { '+':operator.add, '-':operator.sub, \
              '*':operator.mul, '/':operator.truediv }
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())       #左子树
        res2 = postordereval(tree.getRightChild())      #右子树
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)     #根节点
        else:
            return tree.getRootVal()


#============================================
#中序遍历：生成全括号中缀表达式
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal)
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal



