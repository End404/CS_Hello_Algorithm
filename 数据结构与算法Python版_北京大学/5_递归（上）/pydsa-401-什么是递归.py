
# 五、递归（上）
# pydsa-401-什么是递归


# 初识递归：数列求和
# ❖递归算法变成程序
def listsum(numList):
    #最小规模
    if len(numList) == 1:
        return numList[0]
    else:
        #减小规模
        return numList[0] + listsum(numList[1:])    #调用自身

print( listsum([1,3,5,7,9]) )



'''
上面程序的要点：
    1，问题分解为更小规模的相同问题，
并表现为“调用自身” .
    2，对“最小规模”问题的解决：简单直接.
'''

