import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# 执行API调用并存储响应
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)  # 打印状态码，200为请求成功
# 将api响应存储在一个变量中
response_dict = r.json()
# 打印总共有多少个仓库
print("total repositories:", response_dict['total_count'])

# 探索有关仓库的信息，与items关联的是一个列表，其中包含很多字典
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))
# #遍历最受欢迎的仓库
# print("\nselected information about each repository: ")
# for repo_dict in repo_dicts:
# 	print('\nname: ', repo_dict['name'])
# 	print('\nowner: ', repo_dict['owner']['login'])
# 	print('\nstars: ', repo_dict['stargazers_count'])
# 	print('\nrepository: ', repo_dict['html_url'])
# 	print('\ndescription: ', repo_dict['description'])

# # 研究第一个仓库，字典里嵌套字典
# repo_dict = repo_dicts[0]
# print("\nkeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
# 	print(key)

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),  # 有些描述为空
   		'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.lable_font_size = 14
my_config.major_lable_font_size = 18
my_config.truncate_label = 15  # 项目名缩短为15个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'most starred python projects on github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
