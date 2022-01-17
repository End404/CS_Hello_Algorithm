

# ---- 算法分析_Python数据类型的性能（上） ----
# -205-


"""
    
   ---Python两种内置数据类型上各种操作的大O数量级---
        列表list和字典dict.
        这是两种重要的Python数据类型.
        通过运行试验来估计其各种操作运行时间数量级.

"""
#-------------------------------------------------
'''
  --- List列表数据类型 ---
    ❖list类型各种操作（interface）的实现方
        法有很多，如何选择具体哪种实现方法？ 
    ❖总的方案就是，让最常用的操作性能最好
        ，牺牲不太常用的操作
  
    80/20准则：80%的功能其使用率只有20%

List列表数据类型常用操作性能: 
    ❖最常用的是：按索引取值和赋值（v =a[i], a[i]= v）;
    ❖另一个是列表增长，可以选择append()和__add__()“+”

'''
#----------------------------------------------------


# 4种生成前n个整数列表的方法:

#❖ 首先是循环连接列表（+）方式生成.
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

#❖ 然后是用append方法添加元素生成.
def test2():
    l = []
    for i in range(1000):
        l.append(i)

#❖ 接着用列表推导式来做.
def test3():
    l = [i for i in range(1000)]

#❖ 最后是range函数调用转成列表.
def test4():
    l = list(range(1000)) 

#----------------------------------------

# 4种生成前n个整数列表的方法计时:
# 使用timeit模块对函数计时。

#❖ 创建一个Timer对象，指定需要反复运行的语句和只需要运行一次的“安装语句” 
#❖ 然后调用这个对象的timeit方法，其中可以指定反复运行多少次

from timeit import Timer, timeit 

t1 = Timer("test1()", "from __main__ import test1") 
print ( "列表连接  %f seconds\n" % t1.timeit(number = 1000) )

t2 = Timer("test2()", "from __main__ import test2")
print ( "附加  %f seconds\n" % t2.timeit(number = 1000) )

t3 = Timer("test3()", "from __main__ import test3")
print ( "列表推导式  %f seconds\n" % t3.timeit(number = 1000) )

t4 = Timer("test4()", "from __main__ import test4")
print ( "列表range函数调用  %f seconds\n" % t4.timeit(number = 1000) )



