
#************************************
#
#   pydsa-314-无序表的链表实现
#   -0.4-
#
#************************************
'''
链表实现：remove(item)方法
    ❖首先要找到item，这个过程跟search一 样，但在删除节点时, 
需要特别的技巧current指向的是当前匹配数据项的节点.
    而删除需要把前一个节点的next指向current的
下一个节点.
    所以我们在search current的同时，还要维护
前一个(previous)节点的引用.
    ❖找到item之后，current指向item节点，
    previous指向前一个节点，开始执行删除,
需要区分两种情况：
    current是首个节点；或者是位于链条中间的节.

'''



# 链表实现：remove(item)代码
def remove(self, item):
    current = self.head
    previonus = None
    found = False
    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            current = current.getNext()
    if previonus == None:
        self.head = current.getNext()
    else:
        previonus.setNext(current.getNext())



