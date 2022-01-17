

# ---- 算法分析_'变位词'判断问题 ----
# -204-


'''

    解法3：暴力法: 
    ❖暴力法解题思路为：穷尽所有可能组合.
    ❖将s1中出现的字符进行全排列，再查看s2是否出现在全排列列表中.
    ❖这里最大困难是产生s1所有字符的全排列.
        (暴力法恐怕不能算是个好算法)

    解法4：计数比较: 
    ❖解题思路：对比两个词中每个字母出现的次数，如果26个字母出现的次数都相同的话，这两个字符串就一定是变位词.
    ❖具体做法：为每个词设置一个26位的计数器，先检查每个词，在计数器中设定好每个字母出现的次数.
    ❖计数完成后，进入比较阶段，看两个字符串的计数器是否相同，如果相同则输出是变位词的结论.

''' 

#解法4：计数比较-程序代码
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    #分别都计数：
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a') 
        c2[pos] = c2[pos] + 1

    j = 0
    still0k = True

    #计数器比较：
    while j < 26 and still0k:
        if c1[j] == c2[j]:
            j = j + 1 
        else:
            still0k = False

    return still0k

print(anagramSolution4('apple', 'pleap')) 


