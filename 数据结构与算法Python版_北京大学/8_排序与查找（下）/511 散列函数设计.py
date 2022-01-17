
#***********************#
#   
#   511 散列函数设计
#       -- 非数项 ---
#
#***********************#



def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    
    return sum%tablesize


