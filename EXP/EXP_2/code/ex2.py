import torch

print("=" * 50)
print("PyTorch 安装检验")
print("=" * 50)
print("PyTorch 版本:", torch.__version__)
print("Python 绑定正常: 是")
mps_available = hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
print("MPS 是否可用:", mps_available)
if mps_available:
    print("当前加速设备: Apple MPS (Metal)")
else:
    print("当前设备: CPU")
# elseif:
# 设备是 cuda 的自己加上哦

# 基本张量运算验证
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
print("\n向量 a:", a)
print("向量 b:", b)
print("a + b =", a + b)
print("a * b =", a * b)
print("点积 a·b =", torch.dot(a, b).item())
print("\nPyTorch 安装验证成功！")
