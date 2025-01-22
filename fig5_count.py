import matplotlib.pyplot as plt
import numpy as np
import pickle

with open(r"pickle_data/orig_ch_len.pkl", 'rb') as f:
    orig_ch_len = pickle.load(f)
with open(r"pickle_data/orig_en_len.pkl", 'rb') as f:
    orig_en_len = pickle.load(f)
with open(r"pickle_data/anchor_ch_len.pkl", 'rb') as f:
    anchor_ch_len = pickle.load(f)
with open(r"pickle_data/anchor_en_len.pkl", 'rb') as f:
    anchor_en_len = pickle.load(f)


data1 = anchor_ch_len  
data2 = orig_ch_len   
data3 = anchor_en_len
data4 = orig_en_len  


data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))  

# 绘制第一个子图（data1和data2）
ax1.hist([data1, data2], bins=17, label=['MiniLongBench', 'LongBench'], color=['#1f77b4', '#ff7f0e'], 
         stacked=True, density=False, alpha=0.7)
ax1.set_title('Chinese', fontsize=14)
ax1.set_xlabel('Length', fontsize=12)
ax1.set_ylabel('Count', fontsize=12)
ax1.legend()
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# 绘制第二个子图（data3和data4）
ax2.hist([data3, data4], bins=17, label=['MiniLongBench', 'LongBench'], color=['#1f77b4', '#ff7f0e'], 
         stacked=True, density=False, alpha=0.7)
ax2.set_title('English', fontsize=14)
ax2.set_xlabel('Length', fontsize=12)
ax2.set_ylabel('Count', fontsize=12)
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.7)


plt.tight_layout()
plt.savefig('fig5_count.pdf', format='pdf', dpi=1000)