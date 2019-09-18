# -*- coding: utf-8 -*-
"""
Lecture 1一共学习了四部分的知识点，这个codes有三部分
第一部分是学习数据导入、绘表
第二部分是学习用loop(for函数)计算mean和std，然后和np,pd算出的结果做了对比
第三部分模拟股票产生随机数
"""
#第一部分：学读表和画图，#和"""都代表注释不会被执行
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#导入pandas,matplotlib.pyplot,numpy
#Python里的等号表示将某一数值赋予某变量，下文的sp、sp_adj_close、sp_daily都表示变量（名）
sp=pd.read_csv('C:/Users/ThinkPad/Desktop/Autumn/FIN6102/Computing/Spyder/data/S&P500.csv')
#读取数据文件
sp['Date']=pd.to_datetime(sp['Date'])
#原本的日期列是string/字符串,pandas里的.to_datetime让我们将string转化成日期方便识别
sp=sp.set_index('Date')
#这一步是将日期替代里之前表格里的序号12345...，直接让日期作为index
sp_adj_close=sp['Adj Close']
#提取里数据表里的Adj Close这一列，给它命名为sp_adj_close
plt.plot(sp_adj_close)
#你可以给你想处理的那一列取任何的名字，绘图的时候记得也用相应的名字就行里
plt.title('S&P500')
plt.legend(['S&P500'])
#title:标题，legend:图例（数据的对应名称）
plt.show()
#绘图命令，如果这里没有这个命令，那后面又用了plt绘图就会和现在的图放在一起绘制
sp_daily=sp_adj_close.pct_change()
#.pct_change:计算当前元素和前一个元素的百分比变化
#这个时候你可以看到第一个格子显示nan,因为第一行的数值没法除以前面一个
sp_daily=sp_daily.dropna()
#这是一个把nan的数值都去掉的命令，执行完就能看到sp_daily的数据里，没有第一格的nan了
plt.hist(sp_daily,bins=50)
#画一个直方图（histogram），bins为有几条方柱
plt.title('S&P Daily Return')
plt.legend('S&P 500')
#前面已经解释过了，标题，图例
plt.show()

#第二部分，学计算均值和标准差
#方法一，用pandas
mean_pd=sp_daily.mean()
std_pd=sp_daily.std()
#这是用pandas计算出来的赋名为sp_daily这列数据（看前面：也就是pct change）的mean和std
#Calculating using loops
#方法二，用loops计算的mean和std
mean_sum=0
for x in sp_daily:
    mean_sum=mean_sum+x
"""
这里设计了一个循环下去的函数，初始是0+sp_daily里的第一个数,for表示前面的等式
对sp_daily里的每一个x都执行，所以是0+第一个，再加第二个，再加第三个这样下去
直到加完最后一个数，因此这个for函数，最后算出的是所有sp_daili这列数的和
"""
mean_for=mean_sum/len(sp_daily)
"""
mean_for表示用for命令的方法求出的均值起的名字叫mean_for，
也可以自己改成自己喜欢的名字. 
len():列表元素个数。
len(sp_daily)指的是sp_daily有多少个数
因此sum/个数，就可以得到均值了
算出来mean_pd和mean_for是一样的
"""
#下面求std,对照PPT的14页公式
std_sum=0
for x in sp_daily:
    std_sum=std_sum+np.square(x-mean_for)
#这里是求的是sum(xi-u)^2,也就是PPT的14页求std的公式的根号里面的右半部分，自己对应一下
std_for=np.sqrt(std_sum/(len(sp_daily)-1))
#右半部分除以（N-1）,再用np.sqrt()这个numpy自带公式开根号

#方法三，用numpy求mean和std
mean_np=np.mean(sp_daily)
#多插一步老师code没有的
std_np_0=np.std(sp_daily)
"""
比较pandas, numpy, loops(for)三种方法求的mean和std, 
可以发现numpy求的std和另外两个不一样，
为什么不一样？自己查，网上有答案
"""
#要求出一样的std怎么办：
std_np=np.std(sp_daily,ddof=1)
#ddof:delta degree of freedom, by default=0, set it to 1 to get sample std
"""
注意，我上面的计算和Carol老师的原件相比漏了一步，
Carol老师的文件多了sp_daily_values=sp_daily.values, 
这里.values是将列表数值化的意思,也就是运行下面的命令你会得到单独的一组数值，具体变化看右边窗口
"""
sp_daily_values=sp_daily.values

#第三部分，学习generate random variable
n=len(sp_daily)
s0=sp_adj_close.iloc[0]
## iloc[0]:first row of data frame 
s=[s0]
total_s = []
for i in range(500):
    r=np.random.randn()*std_np+mean_np
#np.random.randn()这个函数可以返回一个N（0，1）的随机数，然后你把它乘std,再加均值，
#得到n个服从N(mean,std)的正态分布的随机数，和你的股票数据服从一样的均值方差
#这一步，完成了PPT17页的第一行式子
    current_s=s[-1]*(1+r)
    s.append(current_s)
#完成了第二行的式子，.append是把current_s的出来的数加到s0后面
    total_s.append(s)
    s = s[0]
total_s = np.array(total_s)
total_s = total_s.T
s = np.array(s)
#将前面产生的随机数s变成array/数组序列
plt.plot(s)
#画图

df_simulation = pd.Dataframe

np.abs

r_mean = np.zeros([n]) + mean_np
s_mean = np*np.cumprod(r_mean+1,axis=0)
s_mean = np.insert(s_mean,obj=0,values=s0,axis=0)
plt.plot(s_mean,c)

