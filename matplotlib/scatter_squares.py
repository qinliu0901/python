import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)  # s为点的尺寸
# 设置图表标题并设置坐标轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')


"""excise"""
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
            edgecolor='none', s=40)
plt.xlabel('Value', fontsize=14)
plt.ylabel('', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 5000, 0, 50000000000])
plt.show()
