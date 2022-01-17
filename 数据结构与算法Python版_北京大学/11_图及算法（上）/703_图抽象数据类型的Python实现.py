#*************************************
# 
#   703 图抽象数据类型的Python实现
#
#*************************************


# ADT Graph的实现：顶点Vertex类
class Vertex:       # Vertex包含了顶点信息，以及顶点连接边信息
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        # nbr是顶点对象的key
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
                + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

# ADT Graph的实现：图Graph类
class Graph:        # ❖Graph保存了包含所有顶点的主表
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):   #新加顶点
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):     #通过key查找顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)      #不存在的顶点先添加
        if t not in self.vertList:
            nv = self.addVertex(t)
        #调用启示顶点的方法添加邻接边
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())



# ADT Graph的实现：实例
g = Graph()
for i in range(6):
    g.addVertex(i)

print (g.vertList)

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:
    for w in v.getConnections():
        print ( "(%s, %s)" % (v.getId(), w.getId()) )


