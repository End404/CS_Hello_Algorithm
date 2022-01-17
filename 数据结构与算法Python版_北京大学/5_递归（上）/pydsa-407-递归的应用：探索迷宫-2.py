
# pydsa-407-递归的应用：探索迷宫

"""
    ---探索迷宫：算法思路---
❖这样，探索迷宫的递归算法思路如下：（内容省略）。

❖思路看起来很完美，但有些细节至关重要。

❖所以需要有个机制记录海龟所走过的路径。

❖递归调用的“基本结束条件”归纳如下：（内容省略）。

"""



def searchFrom(maze, startRow, startColumn):
    # 1.碰到墙壁，返回失败.
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    
    # 2.碰到面包屑，或者死胡同，返回失败.
    if maze[startRow][startColumn] == TRIED or \
        maze[startRow][startColumn] == DEAD_END:
        return False
    
    # 3.碰到了出口，返回成功.
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    # 4.洒一下面包屑，继续探索.
    maze.updatePostition(startRow, startColumn, TRIED)

    # 向北南西东4个方向依次探索，or操作符具有短路效应.
    found = searchFrom(maze, startRow-1, startColumn) or \
        searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
                searchFrom(maze, startRow, startColumn+1)
    
    # 如果探索成功，标记当前点，失败则标记为“死胡同”.
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePoaition(startRow, startColumn, DEAD_END)
    return found




