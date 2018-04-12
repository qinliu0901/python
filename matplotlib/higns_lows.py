import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'

# 分析csv文件头格式
# 从文件中获取日期、最低气温和最高气温

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 返回文件的下一行
    # for index, column_header in enumerate(header_row):
    # 	print(index, column_header)
    dates, higns, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        hign = int(row[1])
        higns.append(hign)
        low = int(row[3])
        lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, higns, c='red', alpha=0.5) # alpha 指定颜色的透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
# 给图表区域着色，传递一个x值，两个y值
plt.fill_between(dates, higns, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title('Daily hign and low temperature - 2014', fontsize=24)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()  # 绘制斜的日期标签
plt.ylabel("Temperature(F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
