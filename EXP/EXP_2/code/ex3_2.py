import time

import torch


def benchmark_mm(a, b, device):
    """在指定设备上执行矩阵乘法并返回耗时（秒）。"""
    if device == "mps":
        a_dev = a.to("mps")
        b_dev = b.to("mps")
    else:
        a_dev, b_dev = a, b

    # 预热，避免首次调用开销影响计时
    warmup = torch.mm(a_dev, b_dev)
    if device == "mps":
        warmup.cpu()

    start = time.time()
    result = torch.mm(a_dev, b_dev)
    if device == "mps":
        result.cpu()
    return time.time() - start


print("=" * 50)
print("张量运算与 CPU/MPS 对比")
print("=" * 50)

# 1. 向量运算
v1 = torch.randn(5)
v2 = torch.randn(5)
print("随机向量 v1:", v1)
print("随机向量 v2:", v2)
print("向量范数 ||v1||:", torch.norm(v1).item())
print("点积 v1·v2:", torch.dot(v1, v2).item())

# 2. 矩阵乘法
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
B = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
C = torch.mm(A, B)
print("\n矩阵 A:\n", A)
print("矩阵 B:\n", B)
print("A @ B:\n", C)

# 3. CPU 与 MPS 运算耗时对比
size = 2000
a = torch.randn(size, size)
b = torch.randn(size, size)

cpu_time = benchmark_mm(a, b, "cpu")
print(f"\nCPU 矩阵乘法 ({size}x{size}): {cpu_time:.4f} 秒")

if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
    mps_time = benchmark_mm(a, b, "mps")
    print(f"MPS 矩阵乘法 ({size}x{size}): {mps_time:.4f} 秒")
    print(f"加速比 (MPS/CPU): {cpu_time / mps_time:.2f}x")
    print("说明: MPS 是 Apple Silicon 上的 GPU 加速后端。")
else:
    print("本机未启用 MPS，仅完成 CPU 测试。")
