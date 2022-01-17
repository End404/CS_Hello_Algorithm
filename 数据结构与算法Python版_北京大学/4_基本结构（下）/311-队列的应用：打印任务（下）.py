
# -*- 311-队列的应用：打印任务（下） -*- #

'''
    --- 打印任务问题：模拟流程 ---
    ❖创建打印队列对象.
    ❖时间按照秒的单位流逝.
        按照概率生成打印作业，加入打印队列.
        如果打印机空闲，且队列不空，则取出队首作业打印，记录此作业等待时间.
        如果打印机忙，则按照打印速度进行1秒打印.
        如果当前作业打印完成，则打印机进入空闲.
    ❖时间用尽，开始统计平均等待时间.
    ❖作业的等待时间.
        生成作业时，记录生成的时间戳.
        开始打印时，当前时间减去生成时间即可.
    ❖作业的打印时间.
        生成作业时，记录作业的页数.
        开始打印时，页数除以打印速度即可.

'''


from pythonds.basic.queue import Queue
import random

class Printer:
    #pass
    def __init__(self, ppm):
        self.pagerate = ppm     #打印速度
        self.currentTask = None     #打印任务
        self.timeReaining = 0       #任务倒计时
    
    def tick(self):     #打印1秒
        if self.currentTask != None:
            self.timeReaining = self.timeReaining - 1
            if self.timeReaining <= 0:
                self.currentTask = None
    
    def busy(self):     #打印忙？
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):       #打印新作业
        self.currentTask = newtask
        self.timeReaining = newtask.getPages() * 60/self.pagerate


#打印任务问题：代码2
class Task:
    #pass
    def __init__(self, time):
        self.timestamp = time       #生成时间戳
        self.pages = random.randrange(1, 21)    #打印页数
    
    def getStamp(sefl):
        return self.timestamp
    
    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp     #等待时间


def newPrintTask():
    #pass
    num = random.randrange(1, 181)      #1/180概率生成作业
    if num == 180:
        return True
    else:
        return False 

#模拟
def simulation(numSeconds, pagesPerMinute):
    #pass
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    #时间流逝
    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and \
            (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append( \
                nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("平均等待 %6.2f 秒 %3d 剩余的任务." \
            %(averageWait, printQueue.size()))

#❖按5PPM、1小时的设定，模拟运行10次
for i in range(10):
    simulation(3600, 5)

print()
#提升打印速度到10PPM、1小时的设定
for i in range(10):
    simulation(3600, 10)


