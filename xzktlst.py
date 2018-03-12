#!/usr/bin/env python
#coding = utf-8
#Author:CaoYang(157226691@qq.com)
#Time:2018/3/3 16:09

import time
time1 = 0                          #开始时间
time2 = 0                          #结束时间
time3 = 0                          #程序运行用时
def buxiangling(a,b):              #判断答案是否相邻
    if abs(a-b) == 1:
        return False
    else:
        return True

def daan(a):
    b = [0,"A","B","C","D"]        #将原列表中答案中的 1，2，3，4 转换成A,B,C,D
    return b[a]

def answerlistall():               #生成一个全部可能答案的列表，十一个数字，第一个随便（这里为1），第二到十一个为1-4，对应A-D
    list1 = []
    for a1 in range(1,5):
        for a2 in range(1,5):
            for a3 in range(1,5):
                for a4 in range(1, 5):
                    for a5 in range(1, 5):
                        for a6 in range(1, 5):
                            for a7 in range(1, 5):
                                for a8 in range(1, 5):
                                    for a9 in range(1, 5):
                                        for a10 in range(1,5):
                                            list1num = int('1'+str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8)+str(a9)+str(a10))
                                            list1.append(list1num)
    return list1






def jieti():
    answer = []                             #定义一个装全部答案的列表。PS:事实上只有一个答案，以为全有多解的。
    num = 0                                 #计数答案总数
    zimudaan = []                           #单个的字母答案
    for answernum in answerlistall():
        a = []                              #一组可能答案的列表（11个1-4的整数，多了一位是为了方便对应a[3]就是第3 个答案。
        answerlist = []                     #这个是少第一位的列表，共10个整数。
        countlist = []                      #统计答案A——D字母的个数
        for anschr in str(answernum):       #生成a及answer
            a.append(int(anschr))
            answerlist = a[1:]
        for i in range(1, 5):               #生成countlist
            countlist.append(answerlist.count(i))
        daxiaochazhi = max(countlist) - min(countlist) #计算答案最多字母个数与最小个数的差
        if (a[2]+2) % 4 == a[5]:            #第二题
            if ((a[3] == a[6] == a[2]) and (a[3] != a[4]) and a[3] == 4 ) or \
                    ((a[3] == a[6] == a[4]) and (a[3] != a[2]) and a[3] == 3 ) or \
                    ((a[2] == a[6] == a[4]) and (a[3] != a[2]) and a[3] == 1 ) or \
                    ((a[2] == a[3] == a[4]) and (a[3] != a[6]) and a[3] == 2 ):             #第三题
                if ((a[1] == a[5]) and a[4] ==1 ) or ((a[2] == a[7]) and a[4] == 2) or \
                        ((a[1] == a[9]) and a[4] == 3) or ((a[6] == a[10]) and a[4] == 4):  #第四题
                    if ((a[5] == a[8]) and a[5] == 1) or ((a[5] == a[4]) and a[5] == 2) or\
                         ((a[5] == a[9]) and a[5] == 3) or ((a[5] == a[7]) and a[5] == 4):  #第五题
                        if ((a[8] == a[2] == a[4]) and a[6] == 1) or ((a[8] == a[1] == a[6]) and a[6] ==2 ) or \
                                ((a[8] == a[3] == a[10]) and a[6] == 3 ) or ((a[8] == a[5] == a[9]) and a[6] == 4):#第六题
                            if (buxiangling(a[1], a[7]) and a[8] == 1) or (buxiangling(a[1], a[5]) and a[8] == 2)\
                                        or (buxiangling(a[1], a[2]) and a[8] == 3) or (buxiangling(a[1], a[10]) and a[8] == 4):#第八题
                                if (((a[1] == a[6]) != (a[5] == a[6])) and a[9] == 1) or \
                                        (((a[1] == a[6]) != (a[5] == a[10])) and a[9] == 2)or \
                                        (((a[1] == a[6]) != (a[5] == a[2])) and a[9] == 3)or \
                                        (((a[1] == a[6]) != (a[5] == a[9])) and a[9] == 4):     #第九题
                                    if (daxiaochazhi == 3 and a[10] == 1) or (daxiaochazhi == 2 and a[10] == 2 )\
                                          or (daxiaochazhi == 4 and a[10] == 3) or (daxiaochazhi == 1 and a[10] ==4):       #第十题
                                        if countlist.index(min(countlist)) + 1 == 3 or a[7] == 1 or \
                                            countlist.index(min(countlist)) + 1 == 2 or a[7] == 2 or \
                                            countlist.index(min(countlist)) + 1 == 1 or a[7] == 3 or \
                                            countlist.index(min(countlist)) + 1 == 4 or a[7] == 4 :         #第七题 PS:这个条件没写时，已生成唯一解了。

                                            num += 1
                                            for aa in answerlist:
                                                zimudaan.append(daan(aa))
                                            answer.append(zimudaan)
    return answer



time1 = time.time()
answer = jieti()
time2 = time.time()
time3 = time2 - time1
print('这道题的答案共有%s组,用时%s秒。'%(len(answer),time3))
print('答案分别是：')
for i in range(1,len(answer)+1):
    print('第%s组答案是：'%i)
    for j in range(1,11):
        print('第%s题：%s'%(j,answer[i-1][j-1]))