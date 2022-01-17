# 七、排序与查找（上）
#pydsa-501-顺序查找算法及分析.


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1   #下标顺序增长。
    return found

testlist = [1,2,32,8,17,19,4,13,0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


