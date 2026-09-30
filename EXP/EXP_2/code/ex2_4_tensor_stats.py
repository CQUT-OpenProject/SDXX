"""实验 2-4：统计张量数值，并练习拼接和堆叠。"""

import torch


print("=" * 50)
print("张量统计与维度聚合")
print("=" * 50)

# 创建一个有 2 行 3 列的浮点数张量，作为后续统计的样例数据。
data_tensor = torch.tensor(
    [[1.0, 2.0, 3.0],
     [4.0, 5.0, 6.0]]
)
print("原始张量：\n", data_tensor)

# 不指定 dim 时，sum、mean 和 max 会对张量中的所有元素进行统计。
global_sum = data_tensor.sum().item()
global_mean = data_tensor.mean().item()
global_maximum = data_tensor.max().item()
print("所有元素的总和：", global_sum)
print("所有元素的平均值：", global_mean)
print("所有元素中的最大值：", global_maximum)

# dim=1 表示沿列方向计算，因此得到每一行的结果；dim=0 得到每一列的结果。
sum_of_each_row = data_tensor.sum(dim=1)
mean_of_each_column = data_tensor.mean(dim=0)
print("每一行的总和（dim=1）：", sum_of_each_row)
print("每一列的平均值（dim=0）：", mean_of_each_column)

# argmax(dim=1) 返回每一行最大元素所在的列索引；索引从 0 开始。
maximum_index_in_each_row = data_tensor.argmax(dim=1)
print("每一行最大值所在的列索引：", maximum_index_in_each_row)

# cat 沿着已有的一维方向连接数据；stack 会新增一个维度来放置两组数据。
first_vector = torch.tensor([1, 2, 3])
second_vector = torch.tensor([4, 5, 6])
concatenated_vector = torch.cat([first_vector, second_vector])
stacked_tensor = torch.stack([first_vector, second_vector])
print("\n拼接后的向量：", concatenated_vector)
print("堆叠后的张量：\n", stacked_tensor)
