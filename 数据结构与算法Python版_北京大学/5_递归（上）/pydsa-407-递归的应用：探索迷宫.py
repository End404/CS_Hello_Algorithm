
# pydsa-407-递归的应用：探索迷宫

"""
❖将海龟放在迷宫中间，如何能找到出口.
❖首先，我们将整个迷宫的空间（矩形）分为行列整齐的方格，区分出墙壁和通道.
❖考虑用矩阵方式来实现迷宫数据结构.

"""


class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)   #保存矩阵
            columnsInMaze = len(rowList)



