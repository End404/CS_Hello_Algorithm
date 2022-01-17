
# pydsa-402-递归的应用：任意进制转换

"""
❖在递归三定律里，我们找到了“基本结束条件”，就是小于十的整数.
    拆解整数的过程就是向“基本结束条件”演进的过程.
❖我们用整数除，和求余数两个计算来将整数一步步拆开.
    除以“进制基base”（// base）.
    对“进制基”求余数（% base）.
❖问题就分解为：
    余数总小于“进制基base”，是“基本结束条件”，可直接进行查表转换.
    整数商成为“更小规模”问题，通过递归调用自身解决.
"""


#整数转换为任意进制
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]    #最小规模
    else:
        #减小规模，调用 
        return toStr(n//base, base) + convertString[n%base]

print(toStr(1453, 16))
print(toStr(14, 16))

