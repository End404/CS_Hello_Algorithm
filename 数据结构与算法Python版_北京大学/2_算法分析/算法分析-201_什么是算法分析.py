

# ---- 算法分析_什么是算法分析 ---- #
# -201-


"""
    --算法分析的概念--

❖比较程序的“好坏”，有更多因素:
        代码风格、可读性等等.
❖我们主要感兴趣的是算法本身特性.
❖算法分析主要就是从 计算资源 消耗的角度来评判和比较算法.
    
    -计算资源-
❖那么何为计算资源？
❖一种是算法解决问题过程中需要的存储空间或内存.
❖另一种是算法的执行时间

"""


# 运行时间检测：
# ❖累计求和程序的运行时间检测：用time检测总运行时间返回累计和，以及运行时间（秒）
import time 

def sum0fN2(n):
    start = time.time()     #开始时间
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()       #结束时间
    return theSum , end - start 

#连续运行次数：
for i in range(5):
    print("Sum 是 %d 需要 %10.7f 秒数" % sum0fN2(10000))    #1到10,000累加

print()


# 第二种无迭代的累计算法:

#利用求和公式的无迭代算法
def sum0fN3(n):
    start = time.time()
    theSum = (n * (n+1)) / 2
    end = time.time()
    return theSum, end - start

#采用同样的方法检测运行时间:
for i in range(5):
    print("Sum1 是 %d 需要 %10.7f 秒数" % sum0fN3(100000))


