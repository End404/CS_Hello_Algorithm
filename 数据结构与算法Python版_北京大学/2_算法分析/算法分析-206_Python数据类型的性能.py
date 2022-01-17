

# ---- 算法分析_Python数据类型的性能（下） ----
# -206-


"""
    
   --- list.pop的计时试验 ---

        ❖我们注意到pop这个操作：
            pop()从列表末尾移除元素，O(1)。
            pop(i)从列表中部移除元素，O(n)。

        ❖原因在于Python所选择的实现方法：
            从中部移除元素的话，要把移除元素后面的元素全部向前挪位复制一遍，这个看起来有点笨拙。
            但这种实现方法能够保证列表按索引取值和赋值的操作很快，达到O(1)。
            这也算是一种对常用和不常用操作的折衷方案。

"""
#-------------------------------------------------



#❖为了验证表中的大O数量级（#此处没有显示表图。），我们把两种： 
#   情况下的pop操作来实际计时对比相对同一个大小的list，
#   分别调用 pop() 和 pop(0)。
#❖对不同大小的list做计时，期望的结果是：
#   pop()的时间不随list大小变化，pop(0)的时间随着list变大而变长。

import timeit 

popzero = timeit.Timer("x.pop(0)", "from __main__ import x") 
popend = timeit.Timer("x.pop()", "from __main__ import x")

#❖首先我们看对比.
#对于长度2百万的列表，执行1000次
x = list(range(2000000)) 
popzero.timeit(number = 1000)
#print( "pop(0)时间: ", popzero.timeit(number = 1000) )

x = list(range(2000000)) 
popend.timeit(number = 1000)
#print( "pop()时间: ", popend.timeit(number = 1000) )


#❖我们通过改变列表的大小来测试两个操作的增长趋势.

print( "    pop(0)          pop()" )

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number= 1000)
    x = list(range(i))
    pz = popzero.timeit(number= 1000)
    #print("%15.5f, %15.5f" % (pz, pt))     #不打印出来了，耗时 耗存储。


"""

    --- dict数据类型 ---
    
    ❖字典与列表不同，根据关键码（key）找到数据项，而列表是根据位置（index）.
        
        最常用的取值get和赋值set，其性能为O(1).
        
        另一个重要操作contains(in)是判断字典中是:
            否存在某个关键码（key），这个性能也是O(1).


"""

print('####################################3')

# list和dict的in操作对比
#❖设计一个性能试验来验证list中检索一个值，以及dict中检索一个值的计时对比.

import random 

for i in range(10000, 10000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" %i, 
                "from __main__ import random, x") 
    
    x = list(range(i))
    lst_time = t.timeit(number= 1000)

    x = {j:None for j in range(i)}
    d_time = t.timeit(number= 1000)
    #print("%d,     %10.3f,     %10.3f" % (i,   lst_time,   d_time))     #不打印出来了，耗时 耗存储。



