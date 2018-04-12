import pygal
import matplotlib.pyplot as plt
import numpy as np
from die import Die

"""用pygal生成可缩放的矢量文件（常用在在线方式使用图表，每个设备分辨率不一样）"""

# 创建两个D6
die_1 = Die()
die_2 = Die()


# 掷几次骰子，将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 用pygal对结果进行可视化
# hist = pygal.Bar()
# hist.title = "Results of rolling two D6 1000 times."
# hist.x_labels = [i for i in range(2, 13)]
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add('D6 + D6', frequencies)
# hist.render_to_file('die_visual.svg')


# 用matplotlib对结果进行可视化
ind = np.arange(2, 13)

plt.bar(ind, frequencies, width=0.5)
plt.title("Results of rolling two D6 1000 times.")

plt.xlabel("Result")
plt.ylabel("Frequency of Result")

plt.xticks(ind)
plt.yticks(np.arange(0, 200, 20))

plt.savefig('die_visual2.svg', bbox_inches='tight')
