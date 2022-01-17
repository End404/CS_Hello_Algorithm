
# -*- 队列抽象数据类型及Python实现 -*- #

#Python实现ADT Queue
'''
    ❖ 采 用List的数据项来容纳Queue。
        将List首端作为队列尾端.
        List的末端作为队列首端.
        enqueue()复杂度为O(n).
        dequeue()复杂度为O(1).
    
    ❖ 首尾倒过来的实现，复杂度也倒过来。

'''


class Queue:    #创建一个空队列对象

    def __init__(self): #初始化
        self.items = []

    def isEmpty(sefl):  #测试是否空队列 
        return self.items == []

    def enqueue(sefl, item):    #将数据项item添加到队尾
        self.items.insert(0, item)
    
    def dequeue(self):  #从队首移除数据项
        return self.items.pop()

    def size(self): #返回队列中数据项的个数
        return len(self.items)



