from pygal_maps_world.maps import World
"""有了国别码之后，制作北美中美南美的地图"""

wm = World()
wm.title = "North, Central, and South America"

wm.add('North america', ['ca', 'mx', 'us'])
wm.add('Central america', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South america', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
	'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('america.svg') # 创建一个图表文件，在浏览器中打开