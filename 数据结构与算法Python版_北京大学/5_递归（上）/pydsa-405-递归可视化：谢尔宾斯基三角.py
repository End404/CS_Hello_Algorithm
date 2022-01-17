
# pydsa-405-递归可视化：谢尔宾斯基三角


#谢尔宾斯基Sierpinski三角形；代码
import turtle

def sierpinski(degree, points):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    drawTriangle(points, colormap[degree])    #等边三角形
    if degree > 0:    #最小规模，0直接退出
        #减小规模：getMid边长减半；调用自身，左上右次序
        sierpinski(degree - 1, 
                {'left':points['left'], 
                'top':getMid(points['left'], points['top']),
                'right':getMid(points['left'], points['right'])})
        sierpinski(degree - 1,
                {'left':getMid(points['left'], points['top']),
                'top':points['top'],
                'right':getMid(points['top'], points['right'])})
        sierpinski(degree - 1,
                {'left':getMid(points['left'], points['right']),
                'top':getMid(points['top'], points['right']),
                'right':points['right']})

#绘制等边三角形
def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

#取两个点的中点
def getMid(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) /2 )
    
t = turtle.Turtle()

#外轮廓三个顶点
points = {
    'left':(-200, -100),
    'top':(0, 200),
    'right':(200, -100)
        }

#画degree=5的三角形
sierpinski(5, points)

turtle.done()

