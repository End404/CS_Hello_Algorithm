
# -*- 309-队列的应用：热土豆 -*- #

#热土豆问题：算法
'''
    ❖ 用队列来实现热土豆问题的算法，参加游 戏的人名列表，以及传土豆次数num，算 法返回最后剩下的人名.
    ❖ 模拟程序采用队列来存放所有参加游戏的人名， 按照传递土豆方向从队首排到队尾.
        游戏时，队首始终是持有土豆的人.
    ❖ 模拟游戏开始，只需要将队首的人出队，随即再 到队尾入队，算是土豆的一次传递.
        传递了 num次后，将队首的人移除，不再入队.
        如此反复，直到队列中剩余 1人.

'''


from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())    #一次传递
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPotato(["bb", "dd", "ss", "jj", "kk", "br"], 7))


