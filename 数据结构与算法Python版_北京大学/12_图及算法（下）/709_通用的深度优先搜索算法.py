
#*****************************
#
#   709_通用的深度优先搜索算法
#
#******************************



from pythonds.graphs import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')   #颜色初始化
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)      #如果还有未包括的顶点，则建森林

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1      #算法的步骤
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)       #深度优先递归访问
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)




