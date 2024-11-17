import datetime
import random
import pandas as pd
import matplotlib.pyplot as plt

with open("data1.txt", "w", encoding="utf-8") as f:
    f.write("日期,销售额\n")
    d = datetime.datetime(2024, 1, 1)
    for i in range(366):
        n = random.randint(10000, 100000)
        f.write(d.strftime("%Y-%m-%d") + ',' + str(n) + '\n')
        d += datetime.timedelta(1)

df = pd.read_csv("data1.txt", encoding='utf-8')
df['日期'] = pd.to_datetime(df['日期'])
df['月份'] = df['日期'].dt.to_period('M')
monthly_sales = df.groupby('月份')['销售额'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='orange', width=0.8)
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(df['日期'], df['销售额'], color='blue', linewidth=1)
plt.title('2024年营业额')
plt.xlabel('日期')
plt.ylabel('营业额')
plt.xticks(rotation=45)
plt.show()