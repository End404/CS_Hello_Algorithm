
#*************************************#
#
#   -612_二叉查找树实现及算法分析（下）-
#       --  --
#*************************************#

###############
# ***伪代码*** #
###############

# BST.delete方法
def delete(self, key):
    if self.size > 1 :
        nodeToRemove = self._get(key, self.root)
        if nodeToRemove:
            self.remove(nodeToRemove)
            self.seize = self.size-1
        else:
            raise KeyError("Error, key not in tree")
    elif self.size == 1 and self.root.key == key:
        self.root = None
        self.size = self.size - 1
    else:
        raise KeyError("Error, key not in tree")

def __delitem__(self, key):     #实现del myZipTree['PUK]这样的语句操作
    self.delete(key)


# BST.removoe方法
def BSTremove(self, key):
    # 没有子节点的情况，直接删除
    if currentNode.isLeaf():    #leaf
        if currentNode == currentNode.parent.leftChild:
            currentNode.parent.leftChild = None
        else:
            currentNode.parent.rightChild = None
    # ❖第2种情形稍复杂：被删节点有1个子节点
    else:    
        if currentNode.hasLeftChild():
            if currnetNode.isLeftChild():
                #左子节点删除
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.leftChoild
            elif currentNode.isRightChild():
                #右子节点删除
                currentNode.keftChild.parent = currentNode.parent
                currnetNode.parent.rightChild = currentNode.leftChild
            else:
                #根节点删除
                currentNode.replaceNodeData(currnetNode.leftChild.key,
                                    currnetNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)    
        else:
            if currentNode.isLeftChild():
                #左子节点删除
                currentNode.rightChild.parent =currnetNone.parent
                currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                #右子节点删除
                currentNode.rigthChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
            else:
                #根节点删除
                currentNode.replaceNodeData(currentNode.rightChild.key, 
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.righChild)

    # ❖第3种情形最复杂：被删节点有2个子节点
    elif currentNode.hasBothChildren():     #interior
        succ = currentNode.findSuccessor()
        succ.spliceOut()
        currentNode.key = succ.key
        currentNode.payload = succ.payload

    # ❖TreeNode类：寻找后继节点目前不会遇到到左下角 Python 数据结
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            #目前不会遇到
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ 

    def findMin(self):
        current = self
        while current.hasLeftChild():
            #到左下角
            current = current.leftChild
        return current


# ❖TreeNode类：摘出节点spliceOut()
def spliceOut(self):
    if self.isLeaf():
        #摘出叶节点
        if self.isLeftChild():
            self.parent.leftChild = None
        else:
            self.parent.rightChild = None
    elif self.hasAnyChildren():
        if self.hasLeftChild():
            #目前不会遇到
            if self.isLeftChild():
                self.parent.leftChild = self.leftChild
            else:
                self.parent.rightChild = self.leftChild
            self.leftChild.parent = self.parent
        else:
            #摘出带右子节点的节点
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
            self.rightChild.parent = self.parent



