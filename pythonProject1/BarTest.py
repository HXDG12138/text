from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, AxisOpts
from pyecharts.globals import ThemeType

bar = Bar()
bar.add_xaxis(["美国", "中国", "英国"])
bar.add_yaxis("GDP", [10, 20, 30], label_opts=LabelOpts(position="right"))
bar.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["美国", "中国", "英国"])
bar2.add_yaxis("GDP", [30, 50, 40], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar, "GDP1")
timeline.add(bar2, "GDP2")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render()