"""实验 2-2：练习创建张量、改变形状、索引和广播。"""

import torch


print("=" * 50)
print("张量创建与形状变换")
print("=" * 50)

# 一、从不同数据来源创建张量。
number_list = [1, 2, 3, 4]
tensor_from_list = torch.tensor(number_list, dtype=torch.float32)
zero_tensor = torch.zeros(2, 2)  # 创建 2 行 2 列、元素全为 0 的张量。
one_tensor = torch.ones(3)  # 创建长度为 3、元素全为 1 的一维张量。
even_number_tensor = torch.arange(0, 10, 2)  # 从 0 开始，每次加 2，直到小于 10。

print("从列表创建的张量：", tensor_from_list)
print("2 行 2 列的零张量：\n", zero_tensor)
print("长度为 3 的一张量：", one_tensor)
print("从 0 到 10（不含 10）、间隔为 2：", even_number_tensor)

# 二、改变张量形状并访问其中的元素。
# 0 到 11 共 12 个数，可以排成 3 行 4 列，所以这里重塑为 (3, 4)。
sample_tensor = torch.arange(12).reshape(3, 4)
print("\n重塑为 3 行 4 列：\n", sample_tensor)

# 转置会交换行和列；flatten 会按顺序把多维张量展平成一维。
print("转置后的张量：\n", sample_tensor.T)
print("展平后的张量：", sample_tensor.flatten())

# Python 和 PyTorch 的索引都从 0 开始，因此索引 1 表示第 2 行。
print("第 2 行（索引 1）：", sample_tensor[1])
print("第 1 列（索引 0）：", sample_tensor[:, 0])

# 三、广播：形状为 (1, 3) 的行张量和形状为 (3, 1) 的列张量相加。
# PyTorch 会自动扩展两个张量的形状，逐项相加得到 3 行 3 列的结果。
row_tensor = torch.tensor([[1, 2, 3]])
column_tensor = torch.tensor([[1], [2], [3]])
print("\n广播相加的结果：\n", row_tensor + column_tensor)
