
# pydsa-410-找零兑换问题的递归解法 
# 找零兑换问题：递归解法改进

"""
?对这个递归解法进行改进的关键就在于消除重复计算.
    我们可以用一个表将计算过的中间结果保存起来,
在计算之前查表看看是否已经计算过

?这个算法的中间结果就是部分找零的最优解，
在递归调用过程中已经得到的最优解被记录下来.
    在递归调用之前，先查找表中是否已有部分找零的最优解.
    如果有，直接返回最优解而不进行递归调用如果没有，才进行递归调用.
"""


#找零兑换问题：递归解法改进代码
def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:     #最小规模，直接返回
        knownResults[change] = 1    #记录最优解
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]    #查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList,\
                 change-i, knownResults)   
            if numCoins < minCoins:
                minCoins = numCoins
                #找到最优解，记录到表中
                knownResults[change] = minCoins
    return minCoins

print( recMC([1,5,10,25], 63, [0]*64) )

print()

#改进后的解法，极大减少了递归调用次数
import time 

memo = [0]*64
print( time.perf_counter() )
print( recMC([1,5,10,25], 63, memo) )
print( time.perf_counter() )
print(memo)



