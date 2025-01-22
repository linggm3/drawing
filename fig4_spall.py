import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
from scipy.stats import pearsonr

with open('pickle_data/whole_sub_pred_score.pkl', 'rb') as f:
    whole_sub_pred_score = pickle.load(f)
with open('pickle_data/whole_sub_score.pkl', 'rb') as f:
    whole_sub_score = pickle.load(f)
with open('pickle_data/test_sub_pred_score.pkl', 'rb') as f:
    test_sub_pred_score = pickle.load(f)
with open('pickle_data/test_sub_score.pkl', 'rb') as f:
    test_sub_score = pickle.load(f)
with open('pickle_data/train_sub_pred_score.pkl', 'rb') as f:
    train_sub_pred_score = pickle.load(f)
with open('pickle_data/train_sub_score.pkl', 'rb') as f:
    train_sub_score = pickle.load(f)
with open('pickle_data/whole_sub_sp.pkl', 'rb') as f:
    whole_sub_sp = pickle.load(f)
with open('pickle_data/test_sub_sp.pkl', 'rb') as f:
    test_sub_sp = pickle.load(f)
with open('pickle_data/train_sub_sp.pkl', 'rb') as f:
    train_sub_sp = pickle.load(f)
    
sub_scenarios = ['Single-Document QA', 'Multi-Document QA', 'Summarization', 'Few-shot Learning', 'Code Completion', 'Synthetic Task']
fig, axs = plt.subplots(2, 3, figsize=(10, 6))

# 在每个子图中绘制散点图及回归线
for i in range(2):
    for j in range(3):
        idx = i * 3 + j
        # 计算线性相关性
        whole_corr, _ = pearsonr(whole_sub_pred_score[idx][0], whole_sub_score[idx][0])
        test_corr, _ = pearsonr(test_sub_pred_score[idx][0], test_sub_score[idx][0])
        train_corr, _ = pearsonr(train_sub_pred_score[idx][0], train_sub_score[idx][0])
        
        sns.regplot(x=whole_sub_pred_score[idx], y=whole_sub_score[idx], ax=axs[i, j], label=f'all, sp = {round(whole_sub_sp[i*3+j][0], 4)}, r = {round(whole_corr, 4)}', scatter_kws={'s': 20}, line_kws={'lw': 1})
        sns.regplot(x=test_sub_pred_score[idx], y=test_sub_score[idx], ax=axs[i, j], label=f'test, sp = {round(test_sub_sp[i*3+j][0], 4)}, r = {round(test_corr, 4)}', scatter_kws={'s': 20}, line_kws={'lw': 1})
        sns.regplot(x=train_sub_pred_score[idx], y=train_sub_score[idx], ax=axs[i, j], label=f'train, sp = {round(train_sub_sp[i*3+j][0], 4)}, r = {round(train_corr, 4)}', scatter_kws={'s': 20}, line_kws={'lw': 1})
        axs[i, j].set_xlabel('MiniLongBench scores')
        axs[i, j].set_ylabel('LongBench scores')
        axs[i, j].set_title(sub_scenarios[idx])
        axs[i, j].grid()
        axs[i, j].legend(loc='upper left', prop={'size': 7})
        axs[i, j].tick_params(labelsize=8)

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
# plt.show()
plt.savefig('fig4_spall.pdf', format='pdf', dpi=1000)