from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts

with open("E:/1960-2019全球GDP数据.csv", 'r', encoding='GB2312') as f:
    data = f.readlines()
data.pop(0)

data_list = {}
for line in data:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    if year not in data_list:
        data_list[year] = []
        data_list[year].append([country, gdp])
    else:
        data_list[year].append([country, gdp])

time = Timeline()
sort_data = sorted(data_list.keys())
for year in sort_data:
    country = []
    gdp = []
    data_list[year].sort(key=lambda x: x[1], reverse=True)
    year_data = data_list[year][:8]
    for i in year_data:
        country.append(i[0])
        gdp.append(i[1]/100000000)
    country.reverse()
    gdp.reverse()

    bar = Bar()
    bar.add_xaxis(country)
    bar.add_yaxis(f"{year}年GDP排行(亿)", gdp, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    time.add(bar, f"{year}")

time.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
time.render()


# for i in data_list:
#     for j in range(8):
#         bar.add_xaxis(data_list[i][j][0])
#         bar.add_yaxis("GDP", data_list[i][j][1])
#     time.add(bar, str(i))

# print(sort_data)