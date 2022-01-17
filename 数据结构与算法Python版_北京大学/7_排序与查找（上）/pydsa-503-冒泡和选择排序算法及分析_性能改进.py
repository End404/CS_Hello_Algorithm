
# pydsa-503-冒泡和选择排序算法及分析
# 性能改进
# -0.2-


"""
❖另外，通过监测每趟比对是否发生过交换
，可以提前确定排序是否完成.

❖这也是其它多数排序算法无法做到的.

❖如果某趟比对没有发生任何交换，说明列
表已经排好序，可以提前结束算法.

"""

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
    
        for i in range(passnum):
            #序错，交换
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

alist = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)


