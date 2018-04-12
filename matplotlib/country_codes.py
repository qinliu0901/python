from pygal_maps_world.i18n import COUNTRIES
# 获取两个字母的国别码，字典COUNTRIES包含的是国别码和国家名

# for country_code in sorted(COUNTRIES.keys()):
# 	# 将键按字母顺序排序
# 	print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定国家，返回none
    return None
