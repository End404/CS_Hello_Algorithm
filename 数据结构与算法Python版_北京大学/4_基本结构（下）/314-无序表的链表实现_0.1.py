
#************************************
#
#   pydsa-314-无序表的链表实现
#   链表实现：无序表UnorderedList
#   -0.1-
#
#************************************
'''
❖add方法

❖按照右图的代码调用，形成的链表如下图
    31是最先被加入的数据项，所以成为链表中最后一个项.
    而54是最后被加入的，是链表第一个数据项.

链表实现：无序表UnorderedList.
'''



# 链表实现：add方法实现
def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp


    
