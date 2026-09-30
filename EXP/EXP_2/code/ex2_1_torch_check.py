"""实验 2-1：检查 PyTorch 安装，并进行简单张量运算。"""

import torch


# 能成功导入 torch，就说明当前 Python 环境可以找到 PyTorch。
print("=" * 50)
print("PyTorch 安装检验")
print("=" * 50)
print("PyTorch 版本：", torch.__version__)
print("Python 绑定正常：是")

# MPS 是苹果设备上的 GPU 运算后端。先检查接口是否存在，再检查是否可用。
mps_is_available = (
    hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
)
print("MPS 是否可用：", mps_is_available)
if mps_is_available:
    print("当前加速设备：Apple MPS（Metal）")
else:
    print("当前设备：CPU")

# 创建两个一维张量（向量），每个向量都包含 3 个浮点数。
first_vector = torch.tensor([1.0, 2.0, 3.0])
second_vector = torch.tensor([4.0, 5.0, 6.0])

# 验证逐元素加法、逐元素乘法和向量点积。
print("\n向量 a：", first_vector)
print("向量 b：", second_vector)
print("a + b =", first_vector + second_vector)
print("a * b =", first_vector * second_vector)
print("点积 a·b =", torch.dot(first_vector, second_vector).item())
print("\nPyTorch 安装与基本运算验证成功！")
