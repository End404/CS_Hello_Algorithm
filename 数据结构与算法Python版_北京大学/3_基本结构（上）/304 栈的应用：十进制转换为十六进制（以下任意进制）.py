

# -*- 304 栈的应用：十进制转换为十六内的任意进制 -*- #


from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    
    remstack = Stack()
    
    while decNumber > 0 :
        rem = decNumber % base    #求余数
        remstack.push(rem)
        decNumber = decNumber // base    #整数除
        
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
        
        return newString
    
print(baseConverter(25, 2))
print(baseConverter(25, 16))

