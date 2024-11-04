import pandas as pd

# 读取NLR基因位置信息 (基因ID, 染色体, 起始位置, 结束位置)
nlr_data = pd.read_csv('Darmor_NLR_genes.csv')

# 按染色体和起始位置排序
nlr_data = nlr_data.sort_values(['chromosome', 'start'])

cluster_list = []
current_cluster = []
max_distance = 200000  # 设置最大距离阈值

# 遍历NLR基因，识别簇
for i, row in nlr_data.iterrows():
    if not current_cluster:
        current_cluster.append(row)
    else:
        prev_gene = current_cluster[-1]
        if row['chromosome'] == prev_gene['chromosome'] and row['start'] - prev_gene['end'] <= max_distance:
            current_cluster.append(row)
        else:
            cluster_list.append(current_cluster)
            current_cluster = [row]

if current_cluster:
    cluster_list.append(current_cluster)

# 输出簇信息
for cluster in cluster_list:
    print(f"NLR Cluster: {len(cluster)} genes, Chromosome: {cluster[0]['chromosome']}, Start: {cluster[0]['start']}, End: {cluster[-1]['end']}")
