

#---- 栈抽象数据类型及Python实现_用Python实现ADT-Stack ----#

'''
    Stack的两端对应list设置.
    选用List的末端（index=-1）作为栈顶.
    栈的操作就可以通过对list的append和pop来实现.

'''
#伪代码


class Stack:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    


