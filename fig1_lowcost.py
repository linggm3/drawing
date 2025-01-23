import matplotlib.pyplot as plt

# 数据
data = [
    {"title": "llama-30b", "values": [81184.65519, 3668.957943]},
    {"title": "30B-Epsilon(x)", "values": [81184.65519, 3668.957943]},
    {"title": "LwQ-30B-Instruct(x)", "values": [81184.65519, 3668.957943]},
    {"title": "OPT-30B-Erebus(x)", "values": [81184.65519, 3668.957943]},
    {"title": "Wizard-Vicuna-30B(x)", "values": [50000.84708, 2250.655876]},
    
#     {"title": "Loyal-Macaroni-Maid-7B", "values": [36739.84708, 1776.655876]},
#     {"title": "Kunoichi-7B", "values": [37523.10977, 1780.510724]},
]


# 将秒转换为小时
def sec_to_hour(seconds):
    return seconds / 3600

# 计算加速倍数
speedups = [group["values"][0] / group["values"][1] for group in data]

# 设置柱状图的宽度和位置
bar_width = 0.35
index = range(len(data))

# 创建一个图形和子图
fig, ax = plt.subplots(figsize=(12, 4))  # 调整图形大小

# 定义两种颜色
color2 = "#ff7f0e"  # 橙色
color1 = "#1f77b4"  # 蓝色

# 绘制柱状图
for i, group in enumerate(data):
    # 转换为小时
    values_in_hours = [sec_to_hour(value) for value in group["values"]]
    # 第一个数值用第一个颜色，第二个数值用第二个颜色
    ax.bar(i - bar_width / 2, values_in_hours[0], width=bar_width, color=color1, label=group["title"] if i == 0 else "")
    ax.bar(i + bar_width / 2, values_in_hours[1], width=bar_width, color=color2, label=group["title"] if i == 0 else "")

# 添加数据标签
for i, group in enumerate(data):
    values_in_hours = [sec_to_hour(value) for value in group["values"]]
    ax.text(i - bar_width / 2, values_in_hours[0] + 0.05, f"{values_in_hours[0]:.2f}h", ha="center", va="bottom", fontsize=9, color="black")
    ax.text(i + bar_width / 2, values_in_hours[1] + 0.05, f"{values_in_hours[1]:.2f}h", ha="center", va="bottom", fontsize=9, color="black")

# 添加加速倍数标签
for i, speedup in enumerate(speedups):
    ax.text(i+0.18, min(values_in_hours) + 2, f"{speedup:.2f}x", ha="center", va="bottom", fontsize=10, color="red", fontweight="bold")

# 添加标题和标签
ax.set_ylabel("Test Time (hours)", fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels([f"{group['title']}" for group in data], rotation=0, ha="center", fontsize=12)

# 添加网格线
ax.grid(axis="y", linestyle="--", alpha=0.7)

# 添加图例
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=color1, label="LongBench"),
                   plt.Rectangle((0, 0), 1, 1, color=color2, label="MiniLongBench")],
          loc="upper right", fontsize=12)

# 调整布局
plt.tight_layout()

# 显示图形
plt.savefig('fig1_lowcost_v2.pdf', format='pdf', dpi=1000)
plt.show()