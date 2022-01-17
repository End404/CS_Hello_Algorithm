# 七、排序与查找（上）
# pydsa-501-顺序查找算法及分析.
# 顺序查找：有序表查找


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1   #下标顺序增长。
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))


