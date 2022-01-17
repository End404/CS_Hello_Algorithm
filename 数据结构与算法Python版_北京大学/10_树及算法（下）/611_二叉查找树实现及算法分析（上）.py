
#*************************************#
#
#   -611_二叉查找树实现及算法分析（上）-
#
#*************************************#


#二叉查找树实现：BST.put方法
def put(self, key, val):
    if self.root:
        self._put(key, val, self.root)
    else:
        self.root = TreeNode(key, val)
    self.size = self.size + 1


#二叉查找树实现：_put辅助方法
def _put(self, key, val, currentNode):
    if key < currentNode.key:
        if currentNode.hasLdftChild():
            #递归左子树
            self._put(key, val, currentNode.leftChild)
        else:
            currentNode.leftChild = \
                    TreeNode(key, val, parent=currentNode)
    else:
        if  currentNode.hasRightChild():
            #递归右子树
            self._put(key, val, currentNode.rightChild)
        else:
            currentNode.rightChild = \
                TreeNode(key, val, parent=currentNode)


#二叉查找树实现：索引赋值
def __setitem__(self, k, v):    # *特殊方法（前后双下划线）
    self.put(k, v)

# mytree = BinarySerchTree()
# mytree[3] = "red"
# mytree[4] = "blue"
# mytree[6] = "yellow"


#二叉查找树实现：BST.get方法
def get(self, key):     # *在树中找到key所在的节点取到payload
    if self.root:
        res = self._get(key, self.root)     #递归函数
        if res:
            return res.payload      #找到节点
        else:
            return None
    else:
        return None

def _get(self, key, currentNode):
    if not currentNode:
        return None
    elif currentNode.key == key:
        return currentNode
    elif key < currentNode.key:
        return self._get(key, currentNode.leftChild)
    else:
        return self._get(key, currentNode.rightChild)


#二叉查找树实现：索引和归属
def __getitem__(self, key):     #实现val = myZipTree['puk']
    return self.get(key)

def __contains__(self, key):        #实现'PUK' in myZipTree的归属判断符in
    if self._get(key, self.root):
        return True
    else:
        return False


#二叉查找树实现：迭代器
def __iter__(self):
    if self:
        if self.hasLeftChild():
            for elem in self.leftChild:
                yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem
