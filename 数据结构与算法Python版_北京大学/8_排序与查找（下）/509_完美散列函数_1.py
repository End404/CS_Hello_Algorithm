
#************************#
#                        #
# 509 完美散列函数        #
#
#  ---1--- 对任意长的数据分部分来计算 #
#
#************************#


import hashlib

m = hashlib.md5()
m.update("hello world!")
m.update("this is part #2")
m.update("this is part #3")
m.hexdigest()


