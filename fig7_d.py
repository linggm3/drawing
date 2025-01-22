import pickle
import matplotlib.pyplot as plt
with open(r'pickle_data/change_d.pkl', 'rb') as f:
    yyy = pickle.load(f)

# 0 test, 1 train, 2 all
target_set = 0
x = [2, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100]  # 维度 D

y1 = yyy[0][target_set][:11]  # reduce 99%
y2 = yyy[1][target_set][:11]  # reduce 98%
y3 = yyy[2][target_set][:11]  # reduce 95%


plt.figure(figsize=(10, 6))  # 设置图形大小

# 绘制折线图
plt.plot(x, y1, label="reduce 99%", color="blue", marker="o", linestyle="-", linewidth=2)  # 第一组数据
plt.plot(x, y2, label="reduce 98%", color="green", marker="s", linestyle="--", linewidth=2)  # 第二组数据
plt.plot(x, y3, label="reduce 95%", color="red", marker="^", linestyle="-.", linewidth=2)  # 第三组数据

# 添加标题和标签
plt.title("D", fontsize=16, fontweight="bold")  # 图表标题
plt.xlabel("D", fontsize=14)  # X轴标签
plt.ylabel("Spearman Correlation", fontsize=14)  # Y轴标签

plt.legend(fontsize=12)

plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()  # 自动调整布局
plt.show()