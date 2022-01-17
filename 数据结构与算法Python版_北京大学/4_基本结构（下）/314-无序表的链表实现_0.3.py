
#************************************
#
#   pydsa-314-无序表的链表实现
#   链表实现：无序表UnorderedList
#   -0.3-
#
#************************************
'''
链表实现：search
    ❖从链表头head开始遍历到表尾，
同时判断当前节点的数据项是否目标.
'''

def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
        if current.getData()== item:
            found = True
        else:
            current = current.getNext()
    return found 





    




    
