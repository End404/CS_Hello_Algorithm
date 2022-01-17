

# ---- 算法分析_大O表示法 ---- #
# -202-

"""
    ❖大O表示法
        表示了所有上限中最小的那个上限。
"""

#从代码分析确定执行时间数量级函数：
#❖代码赋值语句可以分为4个部分
# T(n) = 3+3n^2+2n+1 = 3n^2+2n+4
a = 5
b = 6
c = 10

#3n^2项
for i in range(n):
    for j in range(n):
        x = i*i
        y = j*j
        z = i*j

#2n项
for k in range(n):
    w = a*k + 45
    v = b*b

#1项
d = 33


