
#********************************************
#
#   705-实现广度优先搜索
#
#********************************************


from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()   #取队首作为当前顶点
        for nbr in currentVert.getConnections():    #遍历邻接顶点
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')       #当前顶点设黑色


# 通过一个回途追溯函数来确定FOOL到任何单词顶点的最短词梯.
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

# wordgraph = buildGraph("fourletterwords.txt")   #暂未有此文本文件
# bfs(wordgraph, wordgraph.getVertex('FOOL'))
# traverse(wordgraph.getVertex('SAGE'))

traverse(g.getVertex('sage'))

