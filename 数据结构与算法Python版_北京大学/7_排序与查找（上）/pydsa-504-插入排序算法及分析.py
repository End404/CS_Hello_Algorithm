
# pydsa-504-插入排序算法及分析

"""
❖第1趟，子列表仅包含第1个数据项，将第
2个数据项作为“新项”插入到子列表的
合适位置中，这样已排序的子列表就包含
了2个数据项.

❖第2趟，再继续将第3个数据项跟前2个数
据项比对，并移动比自身大的数据项，空
出位置来，以便加入到子列表中.

❖经过n-1趟比对和插入，子列表扩展到全
表，排序完成.

"""
def insertionSort(alist):
    for index in range(1, len(alist)):
        
        #新项/插入项。
        currentvalue = alist[index]
        position = index

        #比对、移动.
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position -1 
        
        #插入新项.
        alist[position] = currentvalue


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
