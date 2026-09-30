"""实验 3-2：根据气温数据训练模型并预测小花数量。"""

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
    # 固定随机数种子，使每次训练都从相同参数开始，结果便于复现。
    torch.manual_seed(7)

    # 原始训练样本：气温是模型输入，小花数量是模型需要预测的目标。
    # reshape(-1, 1) 将一维列表转为“样本数行、每行一个特征”的二维数组。
    training_temperatures = np.array(
        [15, 20, 25, 30, 35, 40], dtype=np.float32
    ).reshape(-1, 1)
    training_flower_counts = np.array(
        [136, 140, 155, 160, 157, 175], dtype=np.float32
    ).reshape(-1, 1)
    test_temperatures = np.array([18, 22, 33], dtype=np.float32).reshape(-1, 1)

    # 对气温做标准化，让输入数值处于更合适的范围，有助于梯度下降训练。
    temperature_mean = float(training_temperatures.mean())
    temperature_standard_deviation = float(training_temperatures.std())
    normalized_training_temperatures = (
        training_temperatures - temperature_mean
    ) / temperature_standard_deviation
    normalized_test_temperatures = (
        test_temperatures - temperature_mean
    ) / temperature_standard_deviation

    training_input_tensor = torch.from_numpy(normalized_training_temperatures)
    training_target_tensor = torch.from_numpy(training_flower_counts)
    test_input_tensor = torch.from_numpy(normalized_test_temperatures)

    # 线性模型学习“标准化后的气温”与小花数量之间的关系。
    linear_model = nn.Linear(1, 1)
    loss_function = nn.MSELoss()
    learning_rate = 0.05
    optimizer = optim.SGD(linear_model.parameters(), lr=learning_rate)
    number_of_epochs = 2000
    training_loss_history = []

    # 每轮依次计算预测值、损失和梯度，再由优化器更新权重与偏置。
    for epoch_number in range(number_of_epochs):
        predicted_training_counts = linear_model(training_input_tensor)
        training_loss = loss_function(
            predicted_training_counts, training_target_tensor
        )
        optimizer.zero_grad()
        training_loss.backward()
        optimizer.step()
        training_loss_history.append(training_loss.item())

    # 训练完成后计算测试预测值和训练集损失；此时不再需要计算梯度。
    linear_model.eval()
    with torch.no_grad():
        test_prediction_tensor = linear_model(test_input_tensor)
        predicted_test_counts = test_prediction_tensor.numpy().reshape(-1)
        fitted_training_counts = linear_model(training_input_tensor)
        final_training_mse = loss_function(
            fitted_training_counts, training_target_tensor
        ).item()

    # 模型权重对应“标准化后的气温”。下面把权重和偏置换算回摄氏度单位，
    # 这样输出的方程可以直接用原始气温计算小花数量。
    normalized_model_weight = linear_model.weight.item()
    model_weight = normalized_model_weight / temperature_standard_deviation
    model_bias = linear_model.bias.item() - model_weight * temperature_mean

    # R² 衡量拟合效果：1 表示完全拟合；接近 0 表示与直接预测平均值相近。
    residual_sum_of_squares = float(
        ((fitted_training_counts - training_target_tensor) ** 2).sum().item()
    )
    total_sum_of_squares = float(
        ((training_target_tensor - training_target_tensor.mean()) ** 2).sum().item()
    )
    r_squared = 1.0 - residual_sum_of_squares / total_sum_of_squares

    print("实验 3-2：温度与小花数量线性回归")
    print(
        f"训练样本数：{len(training_temperatures)}；"
        f"迭代次数：{number_of_epochs}；学习率：{learning_rate}"
    )
    print(
        f"拟合方程：小花数量 = {model_weight:.6f} × 温度 "
        f"+ {model_bias:.6f}"
    )
    print(f"训练集 MSE：{final_training_mse:.6f}；R²：{r_squared:.6f}")
    print("测试气温预测结果：")
    for temperature, flower_count in zip(
        test_temperatures[:, 0], predicted_test_counts
    ):
        print(f"  {int(temperature)} °C -> {flower_count:.2f} 朵")

    # 把图表保存到当前实验的 assets 目录中。
    output_directory = Path(__file__).resolve().parents[1] / "assets"
    output_directory.mkdir(parents=True, exist_ok=True)

    # 左图显示训练损失；右图显示样本、拟合直线和模型对测试气温的预测。
    figure, plot_axes = plt.subplots(1, 2, figsize=(10, 4))
    epoch_numbers = np.arange(1, number_of_epochs + 1)
    plot_axes[0].plot(epoch_numbers, training_loss_history, color="#285f9e")
    plot_axes[0].set(
        title="训练损失", xlabel="迭代轮数", ylabel="均方误差"
    )
    plot_axes[0].grid(alpha=0.25)

    line_temperature_values = np.linspace(
        training_temperatures.min(), training_temperatures.max(), 100
    )
    plot_axes[1].scatter(
        training_temperatures[:, 0],
        training_flower_counts[:, 0],
        label="训练数据",
        color="#285f9e",
    )
    line_flower_count_values = (
        model_weight * line_temperature_values + model_bias
    )
    plot_axes[1].plot(
        line_temperature_values,
        line_flower_count_values,
        label="拟合直线",
        color="#31835b",
    )
    plot_axes[1].scatter(
        test_temperatures[:, 0],
        predicted_test_counts,
        label="预测值",
        color="#d66a3a",
        marker="x",
    )
    for temperature, flower_count in zip(
        test_temperatures[:, 0], predicted_test_counts
    ):
        plot_axes[1].annotate(
            f"{flower_count:.1f}",
            (temperature, flower_count),
            xytext=(4, 5),
            textcoords="offset points",
        )
    plot_axes[1].set(
        title="小花数量预测",
        xlabel="温度（°C）",
        ylabel="小花数量",
    )
    plot_axes[1].legend()
    plot_axes[1].grid(alpha=0.25)
    figure.tight_layout()
    figure.savefig(output_directory / "ex3_2_flower_prediction.png", dpi=180)
    plt.close(figure)
    print("图表：EXP/EXP_3/assets/ex3_2_flower_prediction.png")


if __name__ == "__main__":
    main()
