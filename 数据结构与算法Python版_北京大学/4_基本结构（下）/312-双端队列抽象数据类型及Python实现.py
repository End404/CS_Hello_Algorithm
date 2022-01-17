
 # -*- 双端队列抽象数据类型及Python实现 -*- #
 # -321-
 
 
'''
❖deque定义的操作如下：
Deque()：创建一个空双端队列.
addFront(item)：将item加入队首.
addRear(item)：将item加入队尾.
removeFront()：从队首移除数据项，返回值为移除的数据项.
removeRear()：从队尾移除数据项，返回值为移除的数据项.
isEmpty()：返回deque是否为空.
size()：返回deque中包含数据项的个数.

'''
 
 
class Deque:
    def __init__(self):
        self.items=[]
    
    def __isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

#“回文词”判定：
from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()
    
    for ch in aString:
        chardeque.addRear(ch)
        
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("123321"))



    