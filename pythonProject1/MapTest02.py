import json

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

with open("E:/疫情.txt", 'r', encoding='UTF-8') as file:
    data = file.read()
    data = json.loads(data)
    data_children = data['areaTree'][0]['children'][9]['children']

data_list = []
for child in data_children:
    name = child['name'] + '市'
    confirm = child['total']['confirm']
    data_list.append((name, confirm))

map = Map()
map.add("福建疫情图", data_list, "福建")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 19, "label": "1-19", "color": "#CCFFFF"},
            {"min": 20, "max": 39, "label": "20-99", "color": "#FFFF99"},
            {"min": 40, "max": 59, "label": "40-59", "color": "#FF9966"},
            {"min": 60, "max": 79, "label": "60-79", "color": "#FF6666"},
            {"min": 80, "max": 99, "label": "80-99", "color": "#CC3333"},
            {"min": 100, "label": "100", "color": "#990033"},
        ]
    )
)

map.render()