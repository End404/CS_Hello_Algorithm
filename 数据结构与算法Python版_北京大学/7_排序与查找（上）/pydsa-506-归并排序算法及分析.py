
# pydsa-506-归并排序算法及分析

"""

 ---归并排序Merge Sort---
❖下面我们来看看分治策略在排序中的应用.

❖归并排序是递归算法，思路是将数据表持
续分裂为两半，对两半分别进行归并排序.
    递归的基本结束条件是：数据表仅有1个数据项
，自然是排好序的；
    缩小规模：将数据表分裂为相等的两半，规模减
为原来的二分之一；
    调用自身：将两半分别调用自身排序，然后将分
别排好序的两半进行归并，得到排好序的数据表.
"""


def mergeSort(alist):
    print("分裂：", alist)

    # 基本结束条件
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #递归调用
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i= j= k= 0
        while i <len(lefthalf) and j < len(righthalf):
            #拉链式交错把左右半部从小到大归并到结果列表中。
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        
        while i<len(lefthalf):
            #归并左半部剩余项。
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j<len(righthalf):
            #归并右半部剩余项。
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
        
    print("归并：", alist)



alist = [54,26,93,17,77,31,44,55,20]
print()

mergeSort(alist)
print()

print(alist)


