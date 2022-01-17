
#***********************#
#   
#   513 映射抽象数据类型及Pyth
#       --2 实现ADT Map: put方法代码 ---
#   --- ---
#
#***********************#



def hashfunction(self, key):
    return key% self.size

def rehash(self, oldhash):
    return (oldhash+ 1)% self.size

def put(self, key, data):
    hashvalue = self.hashfunction(key)

    if self.slots[hashvalue] == None:   #key不存在，未冲突
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
    else:       #key已存在，替换val
        if self.slots[hashvalue] == key:
            self.data[hashvalue] = data
        else:
            nextslot = self.rehash(hashvalue)
             #散列冲突，再散列，直到找到空槽 或者key
            while self.slots[nextslot] != None and \ 
                            self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)    
            
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data #replace

                    
                    
