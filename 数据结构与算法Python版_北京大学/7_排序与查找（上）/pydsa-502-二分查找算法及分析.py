
#pydsa-502-二分查找算法及分析


#二分查找：代码.
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2    #取中间值；从列表中间开始比对。
        #中间项比对.
        if alist[midpoint] == item:     #只有一个值时; 如果列表中间的项匹配查找项，则查找结束.
            found = True
        else:   #如果不匹配，那么就有两种情况。
            #缩小比对范围.
            if item < alist[midpoint]:      #数据项小于中间项；列表中间项比查找项大，那么查找项只可能出现在前半部分。
                last = midpoint - 1         #向前面（左部）比对.
            else:
                first = midpoint + 1        ##向右面（右部）比对；列表中间项比查找项小，那么查找项只可能出现在后半部分。
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print( binarySearch(testlist, 3) )
print( binarySearch(testlist, 13) )


