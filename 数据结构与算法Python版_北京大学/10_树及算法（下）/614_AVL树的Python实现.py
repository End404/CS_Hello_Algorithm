
#***************************
#
#   614-AVL树的Python实现
#
#***************************


#AVL树的实现：_put方法
def _put(self, key, val, currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key, val, currentNode.leftChild())
        else:
            #调整因子
            currentNode.leftChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.leftChild)
    else:
        if currentNode.hasRightChild():
            self._put(key, val, currentNode.rightChild)
        else:
            #调整因子
            currentNode.rightChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.rightChild)

#AVL树的实现：UpdateBalance方法
def updateBalance(self, node):
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)    #重新平衡
        return 
    if node.parent != None:
        if node.isLeftChild():
            node.parent.balanceFactor += 1
        elif node.isRightChild():
            node.parent.balanceFactor -= 1
        if node.parent.balanceFeactor != 0:
            self.updateBalance(node.parent)     #调整父节点因子

#AVL树的实现：rebalance重新平衡
def rotateLeft(self, rotRoot):      #旋转左
    newRoot = rotRoot.rightChild
    rotRoot.rightChild = newRoot.leftChild
    if newRoot.leftChild != None:
        newRoot.leftChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isLeftChild():
            rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parnt.rightChild = newRoot
    newRoot.leftChild = rotRoot
    rotRoot.parent = newRoot
    #仅有两个节点需要调整因子
    rotRoot.balanceFactor = rotRoot.balanceFactor + \
                            1 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + \
                            1 + max(rotRoot.balanceFactor, 0)

#平衡因子
def rebalane(self, node):
    if node.balanceFactor < 0:      #右重需要左旋
        if node.rightChild.balanceFactor > 0:
            # Do an LR Rotation  右子节点左重，先右旋
            self.rotateRight(node.rightChild)
            self.rotateLeft(node)
        else:
            # single left
            self.rotateLeft(node)
    elif node.balanceFactor > 0:        #左重需要右旋
        if node.leftChild.balanceFactor < 0:
            # Do an RL Rotation  左子节点右重，先左旋
            self.rotateLeft(node.leftChild)
            self.rotareRight(node)
        else:
            # single right
            self.rotateRight(node)



