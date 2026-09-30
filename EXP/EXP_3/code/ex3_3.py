"""实验 3-3：比较不同学习率对线性回归训练的影响。"""

import math
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
    # 使用实验 3-1 中的相同训练样本，便于比较不同学习率的影响。
    training_input_tensor = torch.tensor(
        [[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], [9.779], [6.182],
         [7.59], [2.167], [7.042], [10.791], [5.313], [7.997], [3.1]],
        dtype=torch.float32,
    )
    training_target_tensor = torch.tensor(
        [[1.7], [2.86], [2.09], [3.19], [1.694], [1.573], [3.366], [2.596],
         [2.53], [1.221], [2.827], [3.465], [1.65], [2.904], [1.3]],
        dtype=torch.float32,
    )

    # 三种学习率分别偏大、合适和偏小，训练时使用相同数据和初始参数。
    learning_rate_settings = [
        ("较大学习率", 0.03),
        ("合适学习率", 0.01),
        ("较小学习率", 0.0001),
    ]
    number_of_epochs = 2000
    loss_function = nn.MSELoss()
    line_colors = {
        "较大学习率": "#d66a3a",
        "合适学习率": "#31835b",
        "较小学习率": "#285f9e",
    }

    # 字典分别保存每种学习率的损失曲线和最终训练结果，方便之后打印与绘图。
    loss_histories = {}
    training_results = {}

    for learning_rate_description, learning_rate in learning_rate_settings:
        # 每次都重设随机种子，确保新建的线性层具有完全相同的初始参数。
        torch.manual_seed(7)
        linear_model = nn.Linear(1, 1)
        optimizer = optim.SGD(linear_model.parameters(), lr=learning_rate)
        loss_history = []
        divergence_iteration = None

        # 用同样的训练次数训练模型，只改变学习率。
        for epoch_index in range(number_of_epochs):
            predicted_values = linear_model(training_input_tensor)
            training_loss = loss_function(predicted_values, training_target_tensor)
            loss_value = training_loss.item()

            # 学习率过大时损失可能变成无穷大或非数值，发现后停止这一组训练。
            if not math.isfinite(loss_value):
                divergence_iteration = epoch_index + 1
                break

            loss_history.append(loss_value)
            optimizer.zero_grad()
            training_loss.backward()
            optimizer.step()

        # 记录训练结束时（或发散后）的 MSE，便于观察训练结果。
        with torch.no_grad():
            final_training_loss = loss_function(
                linear_model(training_input_tensor), training_target_tensor
            ).item()

        loss_histories[learning_rate_description] = loss_history
        training_results[learning_rate_description] = {
            "learning_rate": learning_rate,
            "final_loss": final_training_loss,
            "divergence_iteration": divergence_iteration,
        }

    print(
        f"实验 3-3：不同学习率的训练结果 "
        f"（相同数据、相同初始参数，最多迭代 {number_of_epochs} 次）"
    )
    for learning_rate_description, learning_rate in learning_rate_settings:
        result = training_results[learning_rate_description]
        divergence_iteration = result["divergence_iteration"]
        if divergence_iteration is None:
            print(
                f"  {learning_rate_description}（lr={learning_rate:g}）："
                f"最终 MSE={result['final_loss']:.6f}"
            )
        else:
            print(
                f"  {learning_rate_description}（lr={learning_rate:g}）："
                f"第 {divergence_iteration} 次迭代出现非有限损失；"
                f"最终 MSE={result['final_loss']}"
            )

    # 绘图文件保存在实验目录的 assets 子目录中。
    output_directory = Path(__file__).resolve().parents[1] / "assets"
    output_directory.mkdir(parents=True, exist_ok=True)
    figure, plot_axis = plt.subplots(figsize=(7, 4.5))

    # 对数坐标便于同时观察差异很大的损失值。
    for learning_rate_description, learning_rate in learning_rate_settings:
        loss_history = loss_histories[learning_rate_description]
        if loss_history:
            epoch_numbers = np.arange(1, len(loss_history) + 1)
            plot_axis.plot(
                epoch_numbers,
                loss_history,
                label=f"{learning_rate_description}（lr={learning_rate:g}）",
                color=line_colors[learning_rate_description],
            )

    plot_axis.set_yscale("log")
    plot_axis.set(
        title="不同学习率对训练的影响",
        xlabel="迭代轮数",
        ylabel="均方误差（对数坐标）",
    )
    plot_axis.legend()
    plot_axis.grid(alpha=0.25, which="both")
    figure.tight_layout()
    figure.savefig(output_directory / "ex3_3_learning_rate.png", dpi=180)
    plt.close(figure)
    print("图表：EXP/EXP_3/assets/ex3_3_learning_rate.png")


if __name__ == "__main__":
    main()
