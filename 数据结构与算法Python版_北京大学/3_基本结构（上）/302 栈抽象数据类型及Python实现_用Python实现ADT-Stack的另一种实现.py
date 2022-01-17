

#---- 栈抽象数据类型及Python实现_用Python实现ADT-Stack ----#

'''
    ❖如果我们把List的另一端（首端index=0 ）
        作为Stack的栈顶，同样也可以实现Stack。
    
    ❖不同的实现方案保持了ADT接口的稳定性.

'''
#伪代码


class Stack:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    


