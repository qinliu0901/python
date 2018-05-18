
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
"添加自定义工具提示，也就是将鼠标指向条形将显示它表示的信息"

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'python projects'
chart.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [
	{'value': 16101, 'label': 'description of httpie'},
	{'value': 15101, 'label': 'description of django'},
	{'value': 14101, 'label': 'description of flask'},
	]
# 向add传递一个字典列表，而不是值列表
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')