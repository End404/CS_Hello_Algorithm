
# pydsa-503-冒泡和选择排序算法及分析
# -0.1-

"""
❖第1趟比较交换，共有n-1对相邻数据进行比较.
    一旦经过最大项，则最大项会一路交换到达最后一项.

❖第2趟比较交换时，最大项已经就位，需要排序的数据减少为n-1，共有n-2对相邻数据进行比较.

❖直到第n-1趟完成后，最小项一定在列表首位，就无需再处理了。

"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):  #n-1趟.
        for i in range(passnum):
            #序错，交换
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

