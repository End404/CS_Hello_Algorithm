
#************************************
#
#   pydsa-314-无序表的链表实现
#   链表实现：无序表UnorderedList
#   -0.2-
#
#************************************
'''
链表实现：size
❖size：从链条头head开始遍历到表尾同时用变量累加经过的节点个数。
'''


def size(self):
    current = self.head
    count = 0
    while current != None:
        count = count + 1
        current = current.getNext()
    
    return count 





    
