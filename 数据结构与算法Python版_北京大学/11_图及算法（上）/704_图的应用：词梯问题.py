#*************************************
# 
#   -704-图的应用：词梯问题-
#
#*************************************


#-------------------------------------------------------------------
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
#-------------------------------------------------------------------


# 词梯问题：采用字典建立桶
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter（创建相差一个字母的单词桶）
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1]
            if bucket in d:
                # 4字母单词，可属于4个桶
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertice and edges for words in the same bucket（为同一桶中的单词添加顶点和边缘）
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:     # 同一个单词之间建立边
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


