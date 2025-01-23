import matplotlib.pyplot as plt
import numpy as np
import pickle

# 创建一个2行3列的子图布局
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

sub_scenarios = ['Single-Document QA', 'Multi-Document QA', 'Summarization', 'Few-shot Learning', 'Code Completion', 'Synthetic Task']

with open('pickle_data/change_number.pkl', 'rb') as f:
    data = pickle.load(f)
    
# 柱子的标签
labels = ['5', '10', '15', '20', '25', '30']

# 遍历每个子图
for i in range(2):
    for j in range(3):
        # 获取当前子图的索引
        index = i * 3 + j
        # 绘制柱状图
        bars = axs[i, j].bar(labels, data[index], color=plt.cm.viridis(np.linspace(0, 1, len(data[index]))))
        
        # 添加数据标签
        for bar in bars:
            yval = bar.get_height()
            axs[i, j].text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontsize=8)
        
        # 设置标题
        axs[i, j].set_title(sub_scenarios[index], fontsize=12, fontweight='bold')
        # 设置x轴标签
        axs[i, j].set_xlabel('number of train LLMs', fontsize=10)
        axs[i, j].set_ylim(0.5, 1)
        # 设置y轴标签
        axs[i, j].set_ylabel('sp on all LLMs', fontsize=10)
        
        # 添加网格线
        axs[i, j].grid(axis='y', linestyle='--', alpha=0.7)

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
# plt.show()
plt.savefig('fig9_m.pdf', dpi=1000, bbox_inches='tight')