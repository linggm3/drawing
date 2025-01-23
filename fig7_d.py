import matplotlib.pyplot as plt
import pickle

with open(r'pickle_data/change_d.pkl', 'rb') as f:
    yyy = pickle.load(f)

x = [5, 10, 15, 20, 25, 30, 50, 70, 100]

plt.figure(figsize=(10, 4))

# 绘制折线图并标点
plt.plot(x, yyy[1], marker='o', markersize=8, linestyle='-', color='blue', label='Train')  
plt.plot(x, yyy[0], marker='s', markersize=8, linestyle='--', color='red', label='Test') 
plt.plot(x, yyy[2], marker='^', markersize=8, linestyle='-.', color='green', label='All') 

# 添加标题和标签
# plt.title('Spearman Correlation vs D', fontsize=14) 
plt.xlabel('D', fontsize=12)
plt.ylabel('Spearman Correlation', fontsize=12)

# 添加图例
plt.legend(loc='upper right', fontsize=10) 

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6, color='gray')

# 设置刻度字体大小
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 显示图形
plt.tight_layout()  
# plt.show()

plt.savefig('fig7_d.pdf', dpi=1000, bbox_inches='tight')