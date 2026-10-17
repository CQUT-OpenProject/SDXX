"""实验 4-1：用 PyTorch 自动求导训练一层全连接网络。"""

import torch
from torch import nn, optim


def main():
    # 固定随机数种子，让输入、目标和初始参数可复现。
    torch.manual_seed(7)

    # 10 个样本，每个样本有 3 个输入特征和 2 个目标值。
    x = torch.randn(10, 3)
    y = torch.randn(10, 2)

    # 全连接层把 3 维输入映射为 2 维输出：y_pred = xW^T + b。
    linear = nn.Linear(3, 2)
    print("权重 w：", linear.weight)
    print("偏置 b：", linear.bias)

    # 均方误差衡量预测值与目标值的差异；SGD 按学习率 0.01 更新参数。
    criterion = nn.MSELoss()
    optimizer = optim.SGD(linear.parameters(), lr=0.01)

    # 前向传播：根据当前权重和偏置计算 10 个样本的预测值。
    pred = linear(x)

    # 计算标量损失，然后由 autograd 反向传播得到参数梯度。
    loss = criterion(pred, y)
    print("更新前损失：", loss.item())
    optimizer.zero_grad()
    loss.backward()

    # 梯度分别与权重和偏置张量形状相同。
    print("dL/dw：", linear.weight.grad)
    print("dL/db：", linear.bias.grad)

    # 执行一次梯度下降。用 no_grad 避免把这次参数更新记录进计算图。
    optimizer.step()
    with torch.no_grad():
        updated_pred = linear(x)
        updated_loss = criterion(updated_pred, y)

    print("更新后损失：", updated_loss.item())


if __name__ == "__main__":
    main()
