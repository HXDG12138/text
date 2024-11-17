import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts


def outbreak(url, forward, title, endTime):
    line = Line()
    with open(url, 'r', encoding='UTF-8') as us_f:
        us_data = us_f.read()
        us_data = us_data.replace(forward, "")
        us_data = us_data[:-2]
        us_py = json.loads(us_data)
        us_trend = us_py['data'][0]['trend']
        us_date = us_trend['updateDate'][:endTime]
        us_confirm = us_trend['list'][0]['data']
        us_physic = us_trend['list'][1]['data']
        us_death = us_trend['list'][2]['data']
        us_additional = us_trend['list'][3]['data']

        line.add_xaxis(us_date)
        line.add_yaxis("确诊", us_confirm, label_opts=LabelOpts(is_show=False))
        line.add_yaxis("治愈", us_physic, label_opts=LabelOpts(is_show=False))
        line.add_yaxis("死亡", us_death, label_opts=LabelOpts(is_show=False))
        line.add_yaxis("新增确诊", us_additional, label_opts=LabelOpts(is_show=False))

        line.set_global_opts(
            title_opts=TitleOpts(title=title, pos_left='center', pos_bottom='0'),
            legend_opts=LegendOpts(is_show=True),
            toolbox_opts=ToolboxOpts(is_show=True)
        )
        line.render()

outbreak("E:/美国.txt", "jsonp_1629344292311_69436(", "美国新冠疫情一览表", 366)
# outbreak("E:/日本.txt", "jsonp_1629350871167_29498(", "日本新冠疫情一览表", 366)
# outbreak("E:/印度.txt", "jsonp_1629350745930_63180(", "印度新冠疫情一览表", 365)