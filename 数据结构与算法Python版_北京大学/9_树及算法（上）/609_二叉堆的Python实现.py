
#**********************************
#
#    -609 二叉堆的Python实现-
#
#**********************************


#二叉堆初始化
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
def percUp(self, i):
    while i // 2 > 0:
        if self.heapList[i] < self.heapList[i//2]:
            tmp = self.heapList[i // 2]
            #与父节点交换
            self.heapList[ i// 2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i // 2    #沿路径向上

def insert(self, k):
    self.heapList.append(k)     #添加末尾
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)    #新key上浮
    
def percDown(self, i):
    while (i * 2) <= self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.healList[i]
            #交换下沉
            self.heapList[i] = self.heapLsit[mc]
            self.heapList[mc] = tmp
            #沿路径向下
        i = mc

def minChild(self, i):
    if i * 2 + 1 > self.currentSize:
        #唯一子节点
        return 1 * 2
    else:
        if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
            return i * 2
        #返回较小的
        else:
            return i * 2 + 1

def delMin(self):
    retval = self.heapList[1]    #移走堆顶
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize = self.currentSize - 1
    self.heapList.pop()
    self.percDown(1)    #新顶下沉
    return retval


# buildHeap(lst)方法：从无序表生成“堆”
def buldHeap(self, alist):
    #从最后节点的父节点开始，因叶节点无需下沉
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    print(len(self.heapList), i)
    while ( i > 0 ):
        print(self.heapList, i)
        self.percDown(i)
        i = i - 1 
    print(self.heapList, i)


