
# pydsa-503-冒泡和选择排序算法及分析
# 选择排序
# -0.3-

"""
❖选择排序对冒泡排序进行了改进，保留了
其基本的多趟比对思路，每趟都使当前最大项就位。 

❖但选择排序对交换进行了削减，相比起冒
泡排序进行多次交换，每趟仅进行1次交换，
记录最大项的所在位置，最后再跟本趟最后一项交换.

❖选择排序的时间复杂度比冒泡排序稍优.
    比对次数不变，还是O(n2).
    交换次数则减少为O(n).
"""

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

