
#***********************#
#   
#   513 映射抽象数据类型及Pyth
#       --3 实现ADT Map: get方法 ---
#   --- ---
#
#***********************#



def get(self, key):
    startslot = self.hashfunction(key)      #标记散列值未查找起点

    data = None
    stop = False
    found = False
    position = startslot
    #找key，直到空槽回到起点
    while self.slots[position] != None and \
        not found and not stop:
        if self.slots[position] == key:
            found = True
            data = self.data[position]
        else:      #未找到key，再散列继续找
            position = self.rehash(position)
            if position == startslot:
                stop = True     #回到起点，停
    return data


#附加代码
# *通过特殊方法实现[]访问
def __getitem__(self, key):
    return self.get(key)

def __setitem__(self, key, data):
    self.put(key, data)

