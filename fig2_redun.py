import matplotlib.pyplot as plt
import numpy as np
import pickle

with open(r'pickle_data/random_remove1.pkl', 'rb') as f:
    data1 = pickle.load(f)
with open(r'pickle_data/random_remove2.pkl', 'rb') as f:
    data2 = pickle.load(f)
with open(r'pickle_data/random_remove5.pkl', 'rb') as f:
    data3 = pickle.load(f)
# x_tick_labels = ["Single-Document QA", "Multi-Document QA", "Summarization", "Few-shot Learning", "Code Completion", "Code Completion"]
x_tick_labels = ["SQA", "MQA", "SUM", "FSL", "CODE", "SYN"]

    
# 创建一个图形窗口，设置大小
fig, axs = plt.subplots(1, 3, figsize=(15, 4))  # 1行3列的子图布局

# 在第一个子图中绘制箱线图
axs[0].boxplot(data1)
axs[0].set_title('Reduce 99%')
axs[0].set_ylabel('Spearman Correlation')
axs[0].set_xticklabels(x_tick_labels, rotation=0, ha='center')

# 在第二个子图中绘制箱线图
axs[1].boxplot(data2)
axs[1].set_title('Reduce 98%')
axs[1].set_ylabel('Spearman Correlation')
axs[1].set_xticklabels(x_tick_labels, rotation=0, ha='center')

# 在第三个子图中绘制箱线图
axs[2].boxplot(data3)
axs[2].set_title('Reduce 95%')
axs[2].set_ylabel('Spearman Correlation')
axs[2].set_xticklabels(x_tick_labels, rotation=0, ha='center')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
# plt.show()
plt.savefig('fig2_redundancy.pdf', format='pdf', dpi=1000)