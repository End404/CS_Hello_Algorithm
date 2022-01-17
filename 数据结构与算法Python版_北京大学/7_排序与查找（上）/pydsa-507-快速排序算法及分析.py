
# pydsa-507-快速排序算法及分析


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:    #基本结束条件。
        #分裂。
        splitpoint = partition(alist, first, last)
        #递归调用。
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)


def partition(alist, first, last):
    pivotvalue = alist[first]   #选定“中值”。

    #左右标初值。
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        #向右移动左标。
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        
        #向左移动右标。
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        
        #两标相错就结束移动。
        if rightmark < leftmark:
            done = True
        else:
            #左右标的值交换。
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    
    #中值就位。
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark    #中值点，也是分裂点。



# quickSortHelper()

