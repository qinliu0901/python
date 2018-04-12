import matplotlib.pyplot as plt

from random_walk import RandomWalk
# 创建一个实例，绘制所有点
# 只要程序处于活动状态，就不断模拟随机漫步
# 用颜色映射来指出漫步中各点的先后顺序，删除每个点的黑色轮廓

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    # point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                # edgecolor='none', s=1)
    # 突出起点和终点
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
    #             s=100)
    plt.plot(rw.x_values, rw.y_values, linewidth=2)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
