#**********************************#
# pydsa-403-递归调用的实现
# Python中的递归深度限制
#**********************************#

#Python中的递归深度限制
'''
❖在调试递归算法程序的时候经常会碰到这样的错误：RecursionError.
    递归的层数太多，系统调用栈容量有限.

❖这时候要检查程序中是否忘记设置基本结束条件，
导致无限递归.
    或者向基本结束条件演进太慢，导致递归层数太多，
调用栈溢出.
'''

"""
def tell_story():
    print(" “从前有座山，山上有座庙，庙里有个老和尚，他在讲：” ")
    tell_story()

print("给你讲故事：")
tell_story()
"""


#❖在Python内置的sys模块可以获取和调整最大递归深度.
import sys

print( sys.getrecursionlimit() )

sys.setrecursionlimit(3000)
print( sys.getrecursionlimit() )


