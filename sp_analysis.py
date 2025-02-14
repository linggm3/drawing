import matplotlib.pyplot as plt
import numpy as np

student_ids = np.arange(1, 21)  
subject_A_scores = [0.2101999854550489, 0.21268209502997593, 0.08120119475393249, 0.2062971742531755, 0.2273136644756251, 0.15459917576625234, 0.225832423907837, 0.24515735901948565, 0.10203351185881578, 0.2759836190781045, 0.08416112838594728, 0.3314595217035219, 0.15980806889994684, 0.27324820611537926, 0.2234290236887504, 0.24045668496494813, 0.20406877580547567, 0.2823808472497241, 0.18073196769496808, 0.2017394154780495] 
subject_B_scores = [0.23716772362547042, 0.2613334477569412, 0.07699343611576148, 0.26263998793875126, 0.26303756557583124, 0.1871249256416201, 0.2784309005247569, 0.30548133974501934, 0.09537918976983138, 0.309609844587386, 0.08506932851987377, 0.35326214847044907, 0.19673688477227325, 0.3261900410501645, 0.24934554740466114, 0.2733612818861521, 0.2371293677246716, 0.33545057847147386, 0.21488308667264422, 0.24057992779406767]

group1_indices = [[] for i in range(10)]
group2_indices = [[] for i in range(10)]

# 好
group1_indices[0] = [17, 14, 11, 7, 4, 19, 2, 18]
group2_indices[0] =  [3, 6, 8, 19, 9, 18, 12, 11]
# 好
group1_indices[1] = [2, 5, 14, 18, 10, 12, 4, 9]
group2_indices[1] =  [13, 0, 16, 4, 15, 11, 1, 18]
# 好
group1_indices[2] = [2, 18, 7, 13, 19, 11, 16, 5]
group2_indices[2] =  [7, 14, 9, 8, 18, 11, 5, 0]


# 较好
group1_indices[3] = [14, 7, 12, 10, 19, 4, 8, 11]
group2_indices[3] =  [0, 16, 15, 9, 8, 3, 11, 4]
# 较好
group1_indices[4] = [10, 18, 0, 12, 7, 19, 15, 13]
group2_indices[4] =  [5, 13, 18, 19, 3, 4, 1, 10]
# 较好
group1_indices[5] = [1, 17, 7, 19, 13, 2, 12, 14]
group2_indices[5] =  [8, 11, 6, 1, 5, 3, 13, 12]

# 较差
group1_indices[6] = [6, 15, 2, 3, 11, 14, 7, 18]
group2_indices[6] =  [16, 7, 19, 13, 18, 9, 4, 17]
# 较差
group1_indices[7] = [2, 12, 11, 9, 3, 1, 13, 8]
group2_indices[7] =  [11, 14, 10, 12, 8, 17, 3, 0]

# 差
group1_indices[8] = [2, 10, 19, 6, 4, 16, 12, 0]
group2_indices[8] =  [6, 19, 1, 15, 2, 3, 12, 5]
# 差
group1_indices[9] = [6, 19, 1, 15, 2, 3, 12, 5]
group2_indices[9] =  [0, 6, 17, 18, 4, 1, 5, 14]


GROUP_NUM = 8
group1_indices = group1_indices[GROUP_NUM]
group2_indices = group2_indices[GROUP_NUM]

# np.random.seed(1010101)
# all_indices = np.arange(len(student_ids))
# group1_indices = np.random.choice(all_indices, 8, replace=False)
# group2_indices = np.random.choice(all_indices, 8, replace=False)
# print(list(group1_indices))
# print(list(group2_indices))

group1_student_ids = student_ids[group1_indices]
group1_subject_A_scores = np.array(subject_A_scores)[group1_indices]
group1_subject_B_scores = np.array(subject_B_scores)[group1_indices]

group2_student_ids = student_ids[group2_indices]
group2_subject_A_scores = np.array(subject_A_scores)[group2_indices]
group2_subject_B_scores = np.array(subject_B_scores)[group2_indices]

group1_subject_A_rank = np.argsort(np.argsort(group1_subject_A_scores)) + 1
group1_subject_B_rank = np.argsort(np.argsort(group1_subject_B_scores)) + 1
sorted_group1_indices = np.argsort(group1_subject_A_scores)
sorted_group1_student_ids = group1_student_ids[sorted_group1_indices]
sorted_group1_subject_A_rank = group1_subject_A_rank[sorted_group1_indices]
sorted_group1_subject_B_rank = group1_subject_B_rank[sorted_group1_indices]

group2_subject_A_rank = np.argsort(np.argsort(group2_subject_A_scores)) + 1
group2_subject_B_rank = np.argsort(np.argsort(group2_subject_B_scores)) + 1
sorted_group2_indices = np.argsort(group2_subject_A_scores)
sorted_group2_student_ids = group2_student_ids[sorted_group2_indices]
sorted_group2_subject_A_rank = group2_subject_A_rank[sorted_group2_indices]
sorted_group2_subject_B_rank = group2_subject_B_rank[sorted_group2_indices]


fig, axs = plt.subplots(1, 2, figsize=(10, 4))

bar_width = 0.35  
index = np.arange(len(sorted_group1_subject_A_rank)) 


axs[0].bar(index, sorted_group1_subject_A_rank, bar_width, label='MiniLongBench', alpha=0.7)
axs[0].bar(index + bar_width, sorted_group1_subject_B_rank, bar_width, label='LongBench', alpha=0.7)


axs[0].set_title('Ranking of Group 1 LLMs in Two Benchmarks')
axs[0].set_xlabel('LLM ID')
axs[0].set_ylabel('Rank')
axs[0].set_xticks(index + bar_width / 2)
axs[0].set_xticklabels(sorted_group1_student_ids)
axs[0].legend()


index = np.arange(len(sorted_group2_subject_A_rank))  


axs[1].bar(index, sorted_group2_subject_A_rank, bar_width, label='MiniLongBench', alpha=0.7)
axs[1].bar(index + bar_width, sorted_group2_subject_B_rank, bar_width, label='LongBench', alpha=0.7)


axs[1].set_title('Ranking of Group 2 LLMs in Two Benchmarks')
axs[1].set_xlabel('LLM ID')
axs[1].set_ylabel('Rank')
axs[1].set_xticks(index + bar_width / 2)
axs[1].set_xticklabels(sorted_group2_student_ids)
axs[1].legend()


plt.tight_layout()
plt.show()