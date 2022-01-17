
#pydsa-502-二分查找算法及分析
#递归算法
'''递归算法就是一种典型的分治策略
算法，二分法也适合用递归算法来实现.'''


#二分查找：分而治之.
def binarySearch(alist, item):
    if len(alist) == 0:
        return False    #结束条件.
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            #缩小规模.
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item) # :midpoint 调用自身.
            else:
                return binarySearch(alist[midpoint + 1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print( binarySearch(testlist, 3) )
print( binarySearch(testlist, 13) )


