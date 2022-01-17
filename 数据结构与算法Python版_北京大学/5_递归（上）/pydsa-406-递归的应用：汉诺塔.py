
# pydsa-406-递归的应用：汉诺塔

"""
汉诺塔问题：递归思路

❖将盘片塔从开始柱，经由中间柱，移动到目标柱：
    首先将上层N-1个盘片的盘片塔，从开始柱，经
由目标柱，移动到中间柱；
    然后将第N个（最大的）盘片，从开始柱，移动
到目标柱；
    最后将放置在中间柱的N-1个盘片的盘片塔，经
由开始柱，移动到目标柱。

❖基本结束条件，也就是最小规模问题是：
    1个盘片的移动问题.
"""


def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height -1, fromPole, toPole, withPole)
        moveDisk(height, fromPole ,toPole)
        moveTower(height - 1 , withPole, fromPole, toPole)

def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, fromPole, toPole)

def moveDisk(disk, fromPole, toPole):
    # print(f"Moving disk[{disk}] from {fromPole} to {toPole}")
    print(f"移动碟盘：[{disk}]， 来自 {fromPole} ---> 到 {toPole}。")

moveTower(3, "#1", "#2", "#3")


