
# pydsa-411-找零兑换问题的动态规划解法 
# 找零兑换：动态规划算法扩展


#找零兑换：动态规划算法扩展代码
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    
    for cnents in range(1, change + 1): #从1分开始到change逐个计算最小硬币数
        
        coinCount = cnents  # 1.初始化一个最大值
        newCoin = 1     #初始化一下新加硬币

        # 2.减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cnents]:
            if minCoins[cnents - j] + 1 < coinCount:
                coinCount = minCoins[cnents-j] + 1
                newCoin = j     #对应最小数量，所减的硬币
        minCoins[cnents] = coinCount    # 3.得到当前最少硬币数，记录到表中
        coinsUsed[cnents] = newCoin     #记录本步骤加的1个
    
    #返回最后一个结果
    return minCoins[change]     #循环结束，得到最优解

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

amnt = 63
clist = [1,5,10,21,25]
coinsUsed = [0]*(amnt+1)
coinCount = [0]*(amnt+1)

print("Making change for", amnt, "requires")
print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
print("They are: ")
printCoins(coinsUsed, amnt)
print("The used list is as follows: ")
print(coinsUsed)



