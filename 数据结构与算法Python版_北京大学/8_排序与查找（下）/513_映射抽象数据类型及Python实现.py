
#***********************#
#   
#   513 映射抽象数据类型及Pyth
#       -- 实现ADT Map: 应用实例 ---
#
#***********************#

import hashlib

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[20] = "chicken"
H[17] = 'tiger'

print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20] = 'duck'
print(H[20])
print(H[99])


