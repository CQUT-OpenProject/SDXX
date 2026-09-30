"""实验 3-1：训练并展示一个单变量线性回归模型。"""

from pathlib import Path

import matplotlib

# 使用无窗口绘图后端，运行脚本时直接把图保存到文件，不弹出绘图窗口。
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn, optim

# 优先使用系统中的中文字体，避免图表里的汉字显示成方框。
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Hiragino Sans GB",
    "Arial Unicode MS",
    "Songti SC",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False


def main():
    # 固定随机种子，让模型每次运行时都从相同的初始参数开始，便于复现实验。
    torch.manual_seed(7)

    # 训练数据：每个样本包含一个输入值和对应的目标值。
    # 嵌套列表形成二维数组，形状为（样本数，特征数），符合 nn.Linear 的输入要求。
    training_input_values = np.array(
        [[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], [9.779], [6.182],
         [7.59], [2.167], [7.042], [10.791], [5.313], [7.997], [3.1]],
        dtype=np.float32,
    )
    training_target_values = np.array(
        [[1.7], [2.86], [2.09], [3.19], [1.694], [1.573], [3.366], [2.596],
         [2.53], [1.221], [2.827], [3.465], [1.65], [2.904], [1.3]],
        dtype=np.float32,
    )
    test_input_values = np.array(
        [[3.0], [4.0], [5.0], [6.0], [7.0], [8.0]], dtype=np.float32
    )
    test_target_values = np.array(
        [[1.5], [2.1], [2.0], [2.5], [2.3], [3.2]], dtype=np.float32
    )

    # 把 NumPy 数组转换为 PyTorch 张量，供模型和损失函数计算使用。
    training_input_tensor = torch.from_numpy(training_input_values)
    training_target_tensor = torch.from_numpy(training_target_values)
    test_input_tensor = torch.from_numpy(test_input_values)

    # nn.Linear(1, 1) 表示输入 1 个特征、输出 1 个预测值，即 y = wx + b。
    linear_model = nn.Linear(1, 1)
    loss_function = nn.MSELoss()  # 均方误差：预测值与真实值之差的平方平均值。
    learning_rate = 0.001
    optimizer = optim.SGD(linear_model.parameters(), lr=learning_rate)

    number_of_epochs = 2000
    training_loss_history = []  # 保存每轮训练的损失，用于绘制损失变化曲线。
    for epoch_number in range(number_of_epochs):
        # 前向计算：根据当前的权重和偏置，计算模型预测值。
        predicted_training_values = linear_model(training_input_tensor)
        training_loss = loss_function(
            predicted_training_values, training_target_tensor
        )

        # 梯度下降的标准步骤：清空旧梯度、计算新梯度、更新参数。
        optimizer.zero_grad()
        training_loss.backward()
        optimizer.step()

        # .item() 把只有一个数值的张量转换成普通 Python 数字，方便保存和打印。
        training_loss_history.append(training_loss.item())

    # eval() 切换到评估状态；no_grad() 表示预测时不再计算训练用的梯度。
    linear_model.eval()
    with torch.no_grad():
        test_prediction_tensor = linear_model(test_input_tensor)
        final_training_loss = loss_function(
            linear_model(training_input_tensor), training_target_tensor
        ).item()

    # 线性层只有一个权重和一个偏置；item() 将它们转换为普通数字。
    model_weight = linear_model.weight.item()
    model_bias = linear_model.bias.item()
    bias_sign = "+" if model_bias >= 0 else "-"
    print("实验 3-1：单变量线性回归")
    print(
        f"训练样本数：{len(training_input_values)}；"
        f"迭代次数：{number_of_epochs}；学习率：{learning_rate}"
    )
    print(
        f"拟合方程：预测值 = {model_weight:.6f} × 输入值 "
        f"{bias_sign} {abs(model_bias):.6f}"
    )
    print(f"训练集 MSE：{final_training_loss:.6f}")
    print("测试集预测结果：")
    for input_value, actual_value, predicted_value in zip(
        test_input_values[:, 0],
        test_target_values[:, 0],
        test_prediction_tensor[:, 0],
    ):
        print(
            f"  输入值={input_value:.1f}，真实值={actual_value:.3f}，"
            f"预测值={predicted_value.item():.3f}"
        )

    # 把图表保存在 EXP_3/assets 目录；目录不存在时自动创建。
    output_directory = Path(__file__).resolve().parents[1] / "assets"
    output_directory.mkdir(parents=True, exist_ok=True)

    # 左图显示每轮训练损失；右图显示样本点和模型拟合出的直线。
    figure, plot_axes = plt.subplots(1, 2, figsize=(10, 4))
    epoch_numbers = np.arange(1, number_of_epochs + 1)
    plot_axes[0].plot(epoch_numbers, training_loss_history, color="#285f9e")
    plot_axes[0].set(
        title="训练损失", xlabel="迭代轮数", ylabel="均方误差"
    )
    plot_axes[0].grid(alpha=0.25)

    plot_axes[1].scatter(
        training_input_values[:, 0],
        training_target_values[:, 0],
        label="训练数据",
        color="#285f9e",
    )
    plot_axes[1].scatter(
        test_input_values[:, 0],
        test_target_values[:, 0],
        label="测试数据",
        color="#d66a3a",
        marker="x",
    )
    line_input_values = np.linspace(
        min(training_input_values[:, 0].min(), test_input_values[:, 0].min()),
        max(training_input_values[:, 0].max(), test_input_values[:, 0].max()),
        100,
    )
    line_prediction_values = model_weight * line_input_values + model_bias
    plot_axes[1].plot(
        line_input_values,
        line_prediction_values,
        label="拟合直线",
        color="#31835b",
    )
    plot_axes[1].set(
        title="线性回归拟合结果", xlabel="输入值", ylabel="目标值"
    )
    plot_axes[1].legend()
    plot_axes[1].grid(alpha=0.25)
    figure.tight_layout()
    figure.savefig(output_directory / "ex3_1_regression.png", dpi=180)
    plt.close(figure)
    print("图表：EXP/EXP_3/assets/ex3_1_regression.png")


if __name__ == "__main__":
    main()
