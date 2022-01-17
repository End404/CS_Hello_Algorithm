#*****************************************
#
#   -712-图的应用：最短路径-
#
#*****************************************


from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    #对所有顶点建堆，形成优先队列
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        #优先队列出队 
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                #修改出队顶点所邻接顶点的dist，并逐个重排队列
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)



