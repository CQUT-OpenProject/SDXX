import torch

print("=" * 50)
print("张量创建与形状变换")
print("=" * 50)

# 1. 从不同数据源创建张量
lst = [1, 2, 3, 4]
t1 = torch.tensor(lst, dtype=torch.float32)
t2 = torch.zeros(2, 2)
t3 = torch.ones(3)
t4 = torch.arange(0, 10, 2)

print("从列表创建:", t1)
print("zeros(2,2):\n", t2)
print("ones(3):", t3)
print("arange(0,10,2):", t4)

# 2. 形状变换与索引
x = torch.arange(12).reshape(3, 4)
print("\nreshape(3,4):\n", x)
print("转置 x.T:\n", x.T)
print("展平 flatten:", x.flatten())
print("第 2 行:", x[1])
print("第 1 列:", x[:, 0])

# 3. 广播机制
row = torch.tensor([[1, 2, 3]])
col = torch.tensor([[1], [2], [3]])
print("\n广播相加 row + col:\n", row + col)
