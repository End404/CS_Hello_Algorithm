
# pydsa-411-找零兑换问题的动态规划解法

#找零兑换：动态规划算法代码
def dpMakeChange(coinValueList, change, minCoins):
    #从1分开始到change逐个计算最小硬币数
    for cnents in range(1, change + 1):
        # 1.初始化一个最大值
        coinCount = cnents
        # 2.减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cnents]:
            if minCoins[cnents - j] + 1 < coinCount:
                coinCount = minCoins[cnents-j] + 1
        # 3.得到当前最少硬币数，记录到表中
        minCoins[cnents] = coinCount
    #返回最后一个结果
    return minCoins[change]     #循环结束，得到最优解

print( dpMakeChange([1,5,10,21,25], 63, [0]*64) )

