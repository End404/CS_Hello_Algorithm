
# pydsa-505-谢尔排序算法及分析

"""
❖ 我们注意到插入排序的比对次数，在最好的情况
下是O(n)，这种情况发生在列表已是有序的情况
下，实际上，列表越接近有序，插入排序的比对
次数就越少.

❖ 从这个情况入手，谢尔排序以插入排序作为基础
，对无序表进行“间隔”划分子列表，每个子列
表都执行插入排序.

❖随着子列表的数量越来越少，无序表的整
体越来越接近有序，从而减少整体排序的
比对次数.

❖间隔为3的子列表，子列表分别插入排序
后的整体状况更接近有序.
"""


def shellSort(alist):
    sublistcount = len(alist)//2    #间隔设定
    while sublistcount > 0:
        #子列表排序
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

            print("在大小增加之后: ", sublistcount, " , The list is: ", alist)
            sublistcount = sublistcount // 2    #间隔缩小

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap   ###

        alist[position] = currentvalue



alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
# gapInsertionSort(alist)
print(alist)


