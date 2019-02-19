import pandas as pd
import numpy as np
import csv
import optparse

date = ['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04', '2017-11-05', '2017-11-06', '2017-11-07']
# 设置日期数据，为后面的np.random.choice引用
area = ['华北', '华东', '华南', '西南', '华中', '东北', '西北']
order_type = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

col1 = np.random.choice(date, 1000000, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.1])
# 随机抽样100万次，各个日常出现的概率是P。
col2 = np.random.choice(area, 1000000, p=[0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1])
col3 = np.random.choice(order_type, 1000000, p=[0.05, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05])
col4 = np.random.choice(100, 1000000)
col5 = np.random.choice(10000, 1000000)

df = pd.DataFrame({'date': col1, 'area': col2, 'order_type': col3, 'qty': col4, 'revenue': col5})
df = df.set_index('date')
# 合并各个numpy生产的随机数据成为Pandas的DataFrame


with open('E:\\mess_files\\sample_data.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入columns_name
    writer.writerow(['date', 'area', 'order_type', 'qty', 'revenue'])

# 为了减少内存占用，没有直接在上面生成1亿行数据，先生产100万，然后循环100次。
for i in range(100):
    i = i + 1
    df.to_csv('E:\\mess_files\\sample_data.csv', encoding='gbk', header=False, mode='a')
    print(i * 1000000)

############################################################################


# 4.
# 数据分析代码
# 涉及的功能：读取数据，增加计算字段，group
# by ，merge(left
# join)， index(set & reset)， 输出数据（CSV & excel）。


############################################################################
import pandas as pd
import time
import csv

start = time.clock()
# 开始计时


with open('E:\\mess_files\\pd_sum.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入columns_name
    writer.writerow(['date', 'area', 'order_type', 'qty', 'revenue'])
# 为汇总的输出，建立一个CSV文件，并包含表头字段明。

# 分块（每100万行）进行数据汇总, 并循环写入csv中


reader = pd.read_csv('E:\\mess_files\\sample_data.csv', encoding='gbk', sep=',', iterator=True)
i = 0
while True:
    try:
        start2 = time.clock()
        # 每次循环开始时间

        # 从csv文件迭代读取
        df = reader.get_chunk(1000000)

        mini_sum = df.groupby(['date', 'area', 'order_type']).sum()
        # 按date, area, order_type 进行汇总
        mini_sum.to_csv('E:\\mess_files\\pd_sum.csv', mode='a', header=False)
        # 汇总结果写入CSV文件，'header=False' 避免重复写入表头。

        # 计时
        i = i + 1
        end2 = time.clock()
        # 每次循环结束时间
        print('{} 秒: completed {} rows'.format(end2 - start2, i * 1000000))
    except StopIteration:
        print("Iteration is stopped.")
        # 循环结束退出

        break

df = pd.read_csv('E:\\mess_files\\pd_sum.csv', encoding='gbk', sep=',')

df = df.groupby(['date', 'area', 'order_type']).sum()

df = df.reset_index()
# pandas汇总时，会根据groupby的字段建立multi_index, 需要重置index。


df['date'] = pd.to_datetime(df['date'])
# 将date列 设置为日期类型


df['avg'] = df['revenue'] / df['qty']
# 增加一个计算字段 avg 平均客单价


df_sub = df[['date', 'area', 'qty']].groupby(['date', 'area']).sum().add_prefix('sum_')
# 建立一个新DataFrame, 用于后面的left join 计算各个order_type的占比


df_merge = pd.merge(df, df_sub, how='outer', left_on=['date', 'area'], right_index=True)
# 相当于SQL的left join


df_merge['type_qty%'] = df_merge['qty'] / df_merge['sum_qty']
# 增加计算字段


df_merge = df_merge.set_index('date')

output = pd.ExcelWriter('E:\\mess_files\\output_xls.xlsx')
df_merge.to_excel(output, 'sheet1')
output.save()
# 最终结果输出到excel


end = time.clock()
# 最终使用时间计时
print('final{} 秒'.format(end - start))

###############################################################################
使用了两台机器进行数据运算，DELL
R720
2
U
SAS硬盘
96
GB内存的服务器，Thinkpad
E450
SSD硬盘
i5
8
G内存的笔记本电脑。
运行时，CUP占用率服务器5 %，笔记本30 %， 总内存占用都是约6GB，耗时也非常接近， 每处理100万行用时在
1
秒种以内， 处理1亿行数据的运算还是很轻松的。


服务器循环每次计算100万行用时
0.8
秒， 总用时79
.3
秒。
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃


0.789916201370346
秒: completed
90000000
rows
0.7889745154019323
秒: completed
91000000
rows
0.7875460356832349
秒: completed
92000000
rows
0.7883160047623932
秒: completed
93000000
rows
0.7929830807664189
秒: completed
94000000
rows
0.7884885093438072
秒: completed
95000000
rows
0.8129294153000615
秒: completed
96000000
rows
0.8298620396579395
秒: completed
97000000
rows
0.787222294208533
秒: completed
98000000
rows
0.7879615432937328
秒: completed
99000000
rows
0.7891974322811279
秒: completed
100000000
rows
Iteration is stopped.
final79
.22691993069884
秒


＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃


笔记本电脑循环每次计算100万行用时
0.83， 总用时85
.1
秒。


＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃


0.817601222058812
秒: completed
92000000
rows
0.8092709856398557
秒: completed
93000000
rows
0.8277913177203118
秒: completed
94000000
rows
0.8203788228361191
秒: completed
95000000
rows
0.8211909342874009
秒: completed
96000000
rows
0.8238487924599838
秒: completed
97000000
rows
0.825806156394961
秒: completed
98000000
rows
0.8143844225134984
秒: completed
99000000
rows
0.8465947555305036
秒: completed
100000000
rows
Iteration is stopped.
final85
.11640178604648
秒


＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
---------------------
作者：jambone
来源：CSDN
原文：https: // blog.csdn.net / jambone / article / details / 78769421
版权声明：本文为博主原创文章，转载请附上博文链接！