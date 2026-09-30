## 深度学习（双语）

> [!NOTE]
> 1. 由于 conda 库体积较大，推荐安装 [Miniconda](https://docs.anaconda.com/miniconda/)，本仓库同样使用 Miniconda 管理实验环境
> 2. 实验报告及部分工程使用智能体辅助编写，可能存在不准确的情况，所有内容仅供参考

## 目录导航

| 目录或文件 | 内容 |
| --- | --- |
| [`EXP/EXP_1/`](EXP/EXP_1/) | Python 环境搭建与初步应用 |
| [`EXP/EXP_2/`](EXP/EXP_2/) | PyTorch 环境搭建与初步应用 |
| [`EXP/EXP_3/`](EXP/EXP_3/) | 线性回归算法实现及应用 |
| [`EXP/report(template)/`](<EXP/report(template)/>) | LaTeX 报告模板、示例代码与素材 |
| [`environment.yml`](environment.yml) | Conda 环境依赖 |

## 创建环境

```bash
cd /path/to/SDXX

# Apple Silicon 需指定 x86_64 平台，才能安装 Python 3.7.5
CONDA_SUBDIR=osx-64 conda create -y -p .conda/dl --file environment.yml
conda config --prefix .conda/dl --set subdir osx-64
```

可在 `~/.condarc` 配置清华源（已配置则跳过）：

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
```
