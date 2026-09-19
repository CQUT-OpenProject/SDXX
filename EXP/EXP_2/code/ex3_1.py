import torch

print("=" * 50)
print("张量统计与维度聚合")
print("=" * 50)

data = torch.tensor([[1.0, 2.0, 3.0],
                     [4.0, 5.0, 6.0]])
print("原始张量:\n", data)

print("全局求和:", data.sum().item())
print("全局均值:", data.mean().item())
print("全局最大值:", data.max().item())

print("按行求和 (dim=1):", data.sum(dim=1))
print("按列求均值 (dim=0):", data.mean(dim=0))
print("按行最大值索引:", data.argmax(dim=1))

# 拼接与堆叠
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
print("\n拼接 cat:", torch.cat([a, b]))
print("堆叠 stack:\n", torch.stack([a, b]))
