
#*********************************#
# pydsa-404-递归可视化：分形树
# 递归可视化：图示
#*********************************#


#一个递归作图的例子：螺旋
import turtle

t = turtle.Turtle()

def drawSpiral(t, lineLen):
    if lineLen > 0:    #最小规模，0直接退出
        t.forward(lineLen)
        t.right(90)
        #减小规模，边长减5
        drawSpiral(t, lineLen - 5)  #调用自身

drawSpiral(t, 100)
turtle.done()


