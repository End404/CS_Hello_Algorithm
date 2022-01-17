
#* 栈抽象数据类型及Python实现 *#

# ---- Stack测试代码 ---- #

'''
    ❖抽象数据类型“栈”定义为如下的操作----
        Stack()：创建一个空栈，不包含任何数据项.
        push(item)：将item加入栈顶，无返回值.
        pop()：将栈顶数据项移除，并返回，栈被修改.
        peek()：“窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改.
        isEmpty()：返回栈是否为空栈.
        size()：返回栈中有多少个数据项.

'''

from pythonds.basic.stack import Stack

s=Stack()

print(s.isEmpty()) #若是空，为True
s.push(4)    
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

print(s)


