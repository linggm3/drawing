import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig = plt.figure(figsize=(8, 8))  # 整体画布大小
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1])

# 第一个子图：第一行合并两列
ax1 = fig.add_subplot(gs[0, :])  
categories1 = ['0.99', '0.98', '0.95', '0.9', '0.8', '0.7']
values1 = [0.805440901, 0.848217636, 0.963227017, 0.974296435, 0.978611632, 0.983114447]
# 绘制柱状图
ax1.bar(categories1, values1, color='skyblue', edgecolor='black', alpha=0.8)
# ax1.set_title('Spearman Correlation vs. p', fontsize=14, fontweight='bold')
ax1.set_xlabel('p', fontsize=12)
ax1.set_ylabel('Spearman Correlation', fontsize=12)
ax1.set_ylim(0.6, 1.0)
ax1.grid(axis='y', linestyle='--', alpha=0.7)


ax2 = fig.add_subplot(gs[1, 0])  
categories2 = ['Openai', 'Bert', 'Longformer']
values2 = [0.963227017, 0.969981238, 0.9622889305816135]
# 绘制柱状图
ax2.bar(categories2, values2, color='lightgreen', edgecolor='black', alpha=0.8)
# ax2.set_title('Spearman Correlation vs. Embedding Method', fontsize=14, fontweight='bold')
ax2.set_xlabel('Embedding Method', fontsize=12)
ax2.set_ylabel('Spearman Correlation', fontsize=12)
ax2.set_ylim(0.8, 1.0)
ax2.grid(axis='y', linestyle='--', alpha=0.7)


ax3 = fig.add_subplot(gs[1, 1])  
# 全 0 初始化，标准正态分布随机初始化，木有 beta
categories3 = ['0', 'random', 'no beta']  
values3 = [0.963227017, 0.954409006, 0.873733583]
# 绘制柱状图
ax3.bar(categories3, values3, color='salmon', edgecolor='black', alpha=0.8)
# ax3.set_title('Spearman Correlation vs. Initialization Method', fontsize=14, fontweight='bold')
ax3.set_xlabel('Initialization Method', fontsize=12)
ax3.set_ylabel('Spearman Correlation', fontsize=12)
ax3.set_ylim(0.8, 1.0)
ax3.grid(axis='y', linestyle='--', alpha=0.7)


plt.tight_layout()
plt.show()