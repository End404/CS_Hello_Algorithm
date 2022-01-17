#**************************************************
#                                                 #
# pydsa-313-无序表抽象数据类型及Python实现.         #
#                                                 #
#**************************************************


##############################################
##                                          ##
# 1、链表实现：节点Node                       ##
##                                          ##
# ❖链表实现的最基本元素是节点Node             ##
#   1.1 每个节点至少要包含2个信息：数据项本身， ##
# 以及指向下一个节点的引用信息.                ##
#   1.2 注意next为None的意义是
# 没有下一个节点了，这个很重要.                ##
##                                           ##
###############################################

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext


temp = Node(93)
print( temp.getData() )


###############################################
# 2、链表实现：无序表UnorderedList             ##
##                                           ##
#     2.1 设立一个属性head，                  ##
# 保存对第一个节点的引用空表的head为None.       ##
##                                           ##
###############################################

class UnorderdList:     #无序表的head始终指向链条中的第一个节点.
    def __init__(self):
        self.head = None   #空表的head为None.
        self.head1 = [1,2]   #表头为[1,2]

mylist = UnorderdList()
print(mylist.head)
print(mylist.head1)




