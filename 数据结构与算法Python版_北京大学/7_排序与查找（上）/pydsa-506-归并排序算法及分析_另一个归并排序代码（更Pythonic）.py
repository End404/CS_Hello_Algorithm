
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

# 另一个归并排序 代码（更Pythonic）


def merge_sort(lst):
    # 递归结束条件。
    if len(lst) <= 1:
        return lst

    #分解问题，并递归调用。
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])    #左半部排好序。
    right = merge_sort(lst[middle:])    #右半部排好序。

    #合并左右半部，完成排序。
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged.extend(right if right else left)
    return merged


# ls = [54,26,93,17,77,31,44,55,20]
# merge_sort(ls)
# print(ls)


