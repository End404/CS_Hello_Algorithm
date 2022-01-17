
#********************************************
#
#   708-骑士周游问题算法分析与改进
#
#********************************************


from pythonds.graphs import Graph,Vertex



# ❖新的算法，仅修改了遍历下一格的次序
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'whilte':
                    c = c + 1
            resList.append( (c, v) )
    resList.sort(key=lambda x: x[0])

    return [y[1] for y in resList]


