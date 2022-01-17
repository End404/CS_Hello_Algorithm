
#***********************#
#   
#   513 映射抽象数据类型及Pyth
#       -- 实现ADT Map: 应用实例 ---
#   ---1 保存key的列表就作为散列表处理---
#
#***********************#



class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


