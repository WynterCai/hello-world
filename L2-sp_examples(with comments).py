# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:43:16 2019

@author: zheng
"""


import pandas as pd 					
# 如之前所说，pandas库是python的一个数据处理库，常常用来读写文件，使用pandas可以方便地读写csv类型的文件
import matplotlib.pyplot as plt 		
# plt是python的一个画图库，各种类型的数据统计图可以通过这个库方便地画出，这里应该都非常熟悉了
import numpy as np  					
# 无需重复介绍了
import time 							
# time:时间库
# absolute path
# sp = pd.read_csv('/Users/zheng/OneDrive/Docs/Carol/CUHKSZ/2019/FIN6102Python/data/S&P500.csv')
# relative path
sp = pd.read_csv('data/S&P500.csv')			
# 使用pandas的read_csv()方法读取 `data` 文件夹下的 `S&P500.csv` 文件
sp['Date'] = pd.to_datetime(sp['Date'])		
# 跟上次课操作一样，sp['Date']这一列的数据类型是str，例如'2014-07-14'，现在通过 `to_date` 方法将其数据类型转化为pandas中专用于表示时间的数据格式
sp = sp.set_index('Date')					
# 将 `Date` 这一列变为列表的行索引（同时`Date`这一列就不存在了）
#date = sp['Date']
sp_adj_close = sp['Adj Close'] 				
# 将 sp 中的 `Adj Close` 列存储到 sp_adj_close 变量中
plt.plot(sp_adj_close)						
# 使用 matplotlib 库画图，x是`Date`(已经成为行索引了)，y是`Adj Close`
plt.title('Adj Close')						
# 将图的标题设为 `title`
plt.legend(['S&P500'])						
# 将折线名称设为 `S&P500`
plt.show()									
# 到目前为止和上次课的文件都是一样的，这个命令可以将图显示出来，如果没有这个声明，将无法看到定义好的图形

sp_daily = sp_adj_close.pct_change()		
# 表示计算当前元素与先前元素的相差百分比，并放到 sp_daily 变量中
sp_daily = sp_daily.dropna()				
# 虑除缺失的数据（NaN）
plt.hist(sp_daily,bins=50)					
# hist()方法表示绘制条形图，bins指定了有多少个条形
plt.title('S&P Daily Return')				
# 同上，设置标题
plt.legend(['S&P500'])						# 同上，设置条形的名称
plt.show()									# 显示图片
# calculate using pandas
mean_pd = sp_daily.mean()					# 计算均值
std_pd = sp_daily.std()						# 计算标准差

# calculate using for loops
mean_sum=0											# 定义变量
for x in sp_daily:									# for 循环
    mean_sum = mean_sum + x							# 对平均值进行求和，存储在名为mean_sum的float（数据格式）下
mean_for = mean_sum/len(sp_daily)					# 对 mean_sum 再求平均，和上次课一样，就求出均值了

std_sum=0											# 同上，是计算标准差的过程
for x in sp_daily:
    std_sum = std_sum + np.square(x-mean_for)		# np.square 是计算平方值
std_for = np.sqrt(std_sum/(len(sp_daily)-1))		# np.sqrt 是求平方根

sp_daily_value = sp_daily.values					
# 这里有个tricky的部分，pandas中的数据格式默认是 DataFrame，通过 `.values`可以将其转化为 numpy 中的 `array` 格式，上次有提到
mean_np = np.mean(sp_daily_value)					
# numpy求均值
std_np = np.std(sp_daily_value, ddof=1)				
# numpy求方差
#前面第一次课都有提到过，新的内容在下面：
n=len(sp_daily)										
# 得到 sq_daily 的长度
s0 = sp_adj_close.iloc[0]							
# 得到 sp_adj_close 中第一行的数据

# time.time() will record the time when this line is executed, we use this to record how much time it takes 
# to run from t to t1 (defined below)
t = time.time()										
# 记录当前时间 t
s=[s0]												
# 将 s0 放入 list 中
total_s=[]											
# 一个空的 lost
# use two for loops for generating 200 series (the j for loop) of 1259 prices (the i for loop)
for j in range(200):								# 外层循环 200 次
    for i in range(n):								# 内层循环次数为 sq_daily 的长度 n
        r = np.random.randn()*std_np + mean_np		# np.random.randn() 指的是一个随机数，前面有说过，通过*std+mean变成一个符合均值方差的随机分布
        current_s=s[-1]*(1+r)
        s.append(current_s)							# append()是 list 的方法，表示从list末尾添加数据，比如 a = [1, 2, 3, 4], 那么 a.append(5)后，a = [1, 2, 3, 4, 5]
    total_s.append(s)								# 同上，往 total_s 中添加元素s（s也是个list，list是可以嵌套的）
    s=[s0]
total_s = np.array(total_s)  						# 将 total_s 由 list 转化为 numpy 中的 array
total_s = total_s.T  								# 转置
t1 = time.time()									# 记录当前的时间 t1
print("time for loops,", t1-t)						# 输出上述操作所用时间长度
# plt.plot(total_s)

t = time.time()										# 同上，记录当前事件 t
# generate all the return data that we are going to use simultaneously to increase efficiency
r = np.random.randn(n, 200)*std_np + mean_np		# np.random.randn(n, 200) 表示产生一个 n~200 之间的随机数
# np.cumprod will calculate the cumulative product for a given series.
cum_r = np.cumprod(1+r, axis=0)						# 在数组r的每个元素上加1，再在第0轴方向上对这个新数组进行累乘运算（对列求积），返回值是“由中间结果组成的数组”
s = s0 * cum_r
s = np.insert(s, obj=0, values=s0, axis=0)			# insert() 是插入元素的方法，s表示目标数组，obj表示插入的位置，values表示插入的值，axis表示在哪个维度插入，综合来说就是：将values插入到s的第0维的第0个位置上
df_simulation = pd.DataFrame(data=s, index=sp_adj_close.index)		# 将 s 由 numpy 的 array 转化为 pandas 的 DataFrame 数据结构，并将 sp_adj_close 定为这个 DataFrame 的索引值
t1 = time.time()													# 记录当前时间
print("time for cumprod,", t1-t)									# 输出上述操作所用时间
plt.plot(df_simulation)												# 画图，图数据是 df.simulation

# we add mean_np to np.zeros([n]) to generate a series of shape [n] but with value mean_np.
mean_return = np.zeros([n]) + mean_np								# np.zeros([10]) 表示构建一个长度为10的零数组
s_mean = s0 * np.cumprod(1+mean_return, axis=0) 					# 同上，累乘操作
s_mean = np.insert(s_mean, obj=0, values=s0, axis=0)				# 同上，插入操作
df_mean = pd.DataFrame(data=s_mean, index=sp_adj_close.index)		# numpy的array类型数据 --> pandas的DataFrame类型数据
plt.plot(df_mean, color='red', linewidth=4, label='Mean Return')	# 画图，图数据是 df_mean, 图线颜色为红色，指定线宽为4，图线名称为`Mean Return`
plt.legend()														# 图线名称置空