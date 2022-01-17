
# pydsa-410-找零兑换问题的递归解法

"""
找零兑换问题：递归解法
    *我们来找一种肯定能找到最优解的方法.
        贪心策略是否有效依赖于具体的硬币体系.
    *首先是确定基本结束条件，
兑换硬币这个问题最简单直接的情况就是，
需要兑换的找零，其面值正好等于某种硬币.
        如找零25分，答案就是1个硬币！
    *其次是减小问题的规模，我们要对每种硬币尝试
1次，例如美元硬币体系：
        找零减去1分(penny)后，求兑换硬币最少数量（递归调用
自身）；
        找零减去5分(nikel)后，求兑换硬币最少数量
        找零减去10分(dime)后，求兑换硬币最少数量
        找零减去25分(quarter)后，求兑换硬币最少数量
上述4项中选择最小的一个。
"""


#找零兑换问题：递归解法代码
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:     #最小规模，直接返回
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)   #调用自身；减小规模：每次减去一直硬币面值，挑选最小数量。
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

# print(recMC([1,5,10,25], 63))


# 递归解法虽然能解决问题，但其最大的问题是：极！其！低！效！
import time 

print( time.perf_counter() )
a = recMC([1,5,10,25], 63)
print(a)
print( time.perf_counter() )


# 递归调用过程: 发现一个重大秘密，就是重复计算太多！


