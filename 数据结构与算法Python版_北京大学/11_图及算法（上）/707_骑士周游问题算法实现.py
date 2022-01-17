
#********************************************
#
#   707-骑士周游问题算法实现
#
#********************************************


from pythonds.graphs import Graph,Vertex


def knightTour(n, path, u, limit):      #n:层次；path:路径；u:当前顶点；limit:搜索总深度
    u.setColor('gray')
    path.append(u)      #当前顶点加入路径
    if n < limit:
        nurList = list(u.getConnections())      #对所有合法移动逐一深入
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nurList[i].getColor() == 'white':        #选择白色未经过的顶点深入
                done = knightTour(n+1, path, nbrList[i], limit)     #层次加1，递归深入
            i = i + 1
        if not done:    # prepare to backtrack（准备回溯）
            #都无法完成总深度，回溯，试本层下一个顶点
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


    
