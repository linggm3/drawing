import matplotlib.pyplot as plt
import numpy as np

student_ids = np.arange(1, 21)  
subject_A_scores = [0.27160699202784655, 0.29498313258090075, 0.09554201574536583, 0.2743913413128675, 0.3214810347127226, 0.1933871160036439, 0.29826680356829743, 0.3187484712342869, 0.13564027821891425, 0.3850058254702481, 0.10043323037050249, 0.45242928162246804, 0.21305107592046607, 0.3838707380568383, 0.30003522727211873, 0.2951971556717281, 0.2867716914874046, 0.3727910846195893, 0.24774917012455736, 0.27768916325208726]
subject_B_scores = [0.23716772362547042, 0.2613334477569412, 0.07699343611576148, 0.26263998793875126, 0.26303756557583124, 0.1871249256416201, 0.2784309005247569, 0.30548133974501934, 0.09537918976983138, 0.309609844587386, 0.08506932851987377, 0.35326214847044907, 0.19673688477227325, 0.3261900410501645, 0.24934554740466114, 0.2733612818861521, 0.2371293677246716, 0.33545057847147386, 0.21488308667264422, 0.24057992779406767]

# 好
group1_indices = [ 0,  1,  2,  4,  5,  8, 9, 10]
group2_indices =  [ 3,  6,  7, 11, 12, 13, 15, 16]
# 较好
group1_indices = [ 10,  8,  19,  16,  14,  7, 13, 9]
group2_indices =  [ 10,  5,  18, 19, 15, 17, 9, 11]
# 较差
group1_indices = [ 10,  5,  3,  19,  15,  6, 14, 9]
group2_indices =  [ 10,  8,  12, 18, 16, 1, 14, 4]
# 差
group1_indices = [ 2,  16,  1,  6,  14,  7, 4, 17]
group2_indices =  [ 0,  19,  16, 6, 7, 4, 9, 11]


# np.random.seed(1010101)
# all_indices = np.arange(len(student_ids))
# group1_indices = np.random.choice(all_indices, 8, replace=False)
# group2_indices = np.random.choice(all_indices, 8, replace=False)


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