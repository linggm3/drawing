import pickle
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return np.array(data)

# 加载数据并检查形状
yyy = load_data(r'pickle_data/change_d.pkl')
spsp = load_data(r'pickle_data/change_d_sp.pkl')

sub_scenarios = ['Single-Document QA', 'Multi-Document QA', 'Summarization', 'Few-shot Learning', 'Code Completion', 'Synthetic Task']

# 绘制直方图
plt.figure(figsize=(15, 7))  # 设置整体图像大小
for i in range(spsp.shape[2]):  # 遍历第三个维度
    plt.subplot(2, 3, i + 1)  # 创建2行3列的子图
    plt.hist(spsp[0, :, i], bins=30, density=True, alpha=0.7, color='#1f77b4', edgecolor='black')
    plt.title(sub_scenarios[i])
    plt.xlabel('Spearman Correlation')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加网格线
plt.tight_layout()  # 自动调整子图布局
# plt.suptitle("Frequency Distribution Histograms", fontsize=16)  # 添加总标题
# plt.show()
plt.savefig('fig8_select.pdf', format='pdf', dpi=1000)