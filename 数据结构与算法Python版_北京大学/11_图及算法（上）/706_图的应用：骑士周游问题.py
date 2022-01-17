
#********************************************
#
#   706-图的应用：骑士周游问题
#
#********************************************


from pythonds.graphs import Graph


#合法走棋位置函数
def genLeaglMoves(x, y, bdSize):
    newMoves = []
    #马走日8个格子
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append( (newX, newY) )
    return newMoves

def legalCoord(x, bdSize):      #确认不会走出棋盘
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

#构建走棋关系图
def knightGraph(bdSize):
    ktGraph = Graph()
    #遍历每个格子
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col, bdSize)
            newPositions = genLeaglMoves(row, col , bdSize)     #单步合法走棋
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)    #添加边及顶点
    return ktGraph

def posToNodeId(row, col, bdSize):
    return row*bdSize+col




    
