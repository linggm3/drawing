import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import pickle


with open(r"pickle_data/subscenarios_position.pkl", 'rb') as f:
    subscenarios_position = pickle.load(f)
with open(r"pickle_data/kmeans.pkl", 'rb') as f:
    kmeans = pickle.load(f)
with open(r"pickle_data/X_tsne.pkl", 'rb') as f:
    X_tsne = pickle.load(f)
# subscenarios_position, kmeans, X_tsne

# 设置颜色映射表
colors = ['#FF0000', '#000000']  # 红色和黑色

fig, axes = plt.subplots(1, 3, figsize=(16, 5))  

to_paint_scenarios = [11, 1, 20]
for idx, i in enumerate(to_paint_scenarios):
    tmp = list(subscenarios_position['longbench'].keys())[i]
    task = subscenarios_position['longbench'][tmp]
    others = [j for j in range(4750) if j not in task]
    labels = kmeans.labels_

    # 绘制子图
    ax = axes[idx]  
    ax.scatter(X_tsne[others, 0], X_tsne[others, 1], color=colors[1], label="Others", s=15)
    ax.scatter(X_tsne[task, 0], X_tsne[task, 1], color=colors[0], label="Task", s=50)

    strr = list(subscenarios_position['longbench'].keys())[i]
    # 添加标题和标签
    ax.set_title(strr, fontsize=14)
    ax.set_xlabel('t-SNE Component 1', fontsize=12)
    ax.set_ylabel('t-SNE Component 2', fontsize=12)

    # 添加图例
    ax.legend(fontsize=10)

plt.tight_layout()

plt.savefig('fig6_vis.pdf', format='pdf', dpi=1000)