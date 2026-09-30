"""实验 2-3：练习向量、矩阵运算，并比较 CPU 与 MPS 的速度。"""

import time

import torch


def measure_matrix_multiplication(first_matrix, second_matrix, device_name):
    """在指定设备上进行一次矩阵乘法，并返回用时（秒）。"""
    target_device = torch.device(device_name)

    # 将输入矩阵放到待测试的设备上。CPU 输入留在 CPU，MPS 输入复制到显卡。
    first_matrix_on_device = first_matrix.to(target_device)
    second_matrix_on_device = second_matrix.to(target_device)

    # 先做一次预热运算，减少首次调用初始化设备带来的额外时间。
    warm_up_result = torch.matmul(first_matrix_on_device, second_matrix_on_device)
    if target_device.type == "mps":
        # MPS 运算可能异步执行；取回 CPU 结果可以等待预热运算完成。
        warm_up_result.cpu()

    # 使用高精度计时器，只测量矩阵乘法，不把输入数据传输时间算进去。
    start_time = time.perf_counter()
    result = torch.matmul(first_matrix_on_device, second_matrix_on_device)
    if target_device.type == "mps":
        # 等待 GPU 运算结束后再读取结束时间，避免只测到任务提交时间。
        result.cpu()
    elapsed_seconds = time.perf_counter() - start_time
    return elapsed_seconds


print("=" * 50)
print("张量运算与 CPU/MPS 对比")
print("=" * 50)

# 一、向量运算：计算两个长度为 5 的随机向量的范数和点积。
first_vector = torch.randn(5)
second_vector = torch.randn(5)
print("随机向量 v1：", first_vector)
print("随机向量 v2：", second_vector)
print("向量 v1 的范数：", torch.norm(first_vector).item())
print("向量 v1 与 v2 的点积：", torch.dot(first_vector, second_vector).item())

# 二、矩阵乘法：两个 2 行 2 列矩阵相乘，结果仍为 2 行 2 列。
first_small_matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
second_small_matrix = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
product_matrix = torch.matmul(first_small_matrix, second_small_matrix)
print("\n矩阵 A：\n", first_small_matrix)
print("矩阵 B：\n", second_small_matrix)
print("矩阵 A 与 B 的乘积：\n", product_matrix)

# 三、用较大的矩阵比较设备速度。矩阵大小可以按电脑性能适当调整。
matrix_size = 2000
first_large_matrix = torch.randn(matrix_size, matrix_size)
second_large_matrix = torch.randn(matrix_size, matrix_size)

cpu_seconds = measure_matrix_multiplication(
    first_large_matrix, second_large_matrix, "cpu"
)
print(f"\nCPU 矩阵乘法（{matrix_size}×{matrix_size}）：{cpu_seconds:.4f} 秒")

# MPS 只在支持它的 PyTorch 和苹果设备上可用，所以运行前先检查。
mps_is_available = (
    hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
)
if mps_is_available:
    mps_seconds = measure_matrix_multiplication(
        first_large_matrix, second_large_matrix, "mps"
    )
    print(f"MPS 矩阵乘法（{matrix_size}×{matrix_size}）：{mps_seconds:.4f} 秒")

    # 加速倍数 = CPU 耗时 ÷ MPS 耗时；数值越大表示 MPS 用时相对越短。
    if mps_seconds > 0:
        speedup = cpu_seconds / mps_seconds
        print(f"MPS 相对 CPU 的加速倍数：{speedup:.2f} 倍")
    print("MPS 是苹果设备上用于 GPU 运算的后端。")
else:
    print("本机没有可用的 MPS，仅完成 CPU 测试。")
