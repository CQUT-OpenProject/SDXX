"""实验 4-2：用 PyTorch 全连接神经网络对 MNIST 手写数字分类。"""

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def main():
    # 固定模型初始化和数据顺序，方便重复实验和比较结果。
    torch.manual_seed(7)

    # 使用 CPU 以保持 PyTorch 1.13.1 在 macOS、Windows 和 Linux 上的兼容性。
    device = torch.device("cpu")

    # MNIST 为 28×28 灰度图。张量转为 [0, 1] 后按数据集均值和标准差标准化。
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ]
    )
    training_dataset = datasets.MNIST(
        root="data", train=True, download=True, transform=transform
    )
    test_dataset = datasets.MNIST(
        root="data", train=False, download=True, transform=transform
    )
    training_loader = DataLoader(
        training_dataset, batch_size=64, shuffle=True, num_workers=0
    )
    test_loader = DataLoader(
        test_dataset, batch_size=1000, shuffle=False, num_workers=0
    )

    # 将 28×28 图像展平为 784 个特征，经隐藏层映射到 10 个数字类别。
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 128),
        nn.ReLU(),
        nn.Linear(128, 10),
    ).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    number_of_epochs = 3

    print("实验 4-2：MNIST 手写数字分类")
    print("PyTorch 版本：", torch.__version__)
    print("计算设备：", device)
    print(
        "训练样本数：{}；测试样本数：{}；批量大小：64；训练轮数：{}".format(
            len(training_dataset), len(test_dataset), number_of_epochs
        )
    )

    for epoch_number in range(1, number_of_epochs + 1):
        model.train()
        total_loss = 0.0
        for images, labels in training_loader:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            class_scores = model(images)
            loss = criterion(class_scores, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * labels.size(0)

        average_loss = total_loss / len(training_dataset)
        print(
            "第 {} 轮训练损失：{:.4f}".format(epoch_number, average_loss)
        )

    # 在测试集上评估分类准确率；评估阶段不计算梯度。
    model.eval()
    correct_count = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)
            predicted_labels = model(images).argmax(dim=1)
            correct_count += (predicted_labels == labels).sum().item()

    accuracy = 100.0 * correct_count / len(test_dataset)
    print(
        "测试集正确数：{} / {}；准确率：{:.2f}%".format(
            correct_count, len(test_dataset), accuracy
        )
    )


if __name__ == "__main__":
    main()
