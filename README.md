## 深度学习（双语）

## 目录导航

| 目录或文件 | 内容 |
| --- | --- |
| [`EXP/EXP_1/`](EXP/EXP_1/) | Python 环境搭建与初步应用 |
| [`EXP/EXP_2/`](EXP/EXP_2/) | PyTorch 环境搭建与初步应用 |
| [`EXP/report(template)/`](<EXP/report(template)/>) | LaTeX 报告模板、示例代码与素材 |
| [`environment.yml`](environment.yml) | Conda 环境依赖 |

## 环境与运行

> [!NOTE]
> 1. 由于 conda 库体积较大，推荐安装 [Miniconda](https://docs.anaconda.com/miniconda/)，本仓库同样使用 Miniconda 管理实验环境

在仓库根目录执行（`cd` 到本仓库）：

### 首次创建环境

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

### 激活 / 退出

```bash
conda activate "$(pwd)/.conda/dl"   # 激活 dl 环境
conda deactivate                    # 退出当前环境
conda env list                      # 查看所有环境
```

### 运行实验代码

```bash
conda activate "$(pwd)/.conda/dl"

python "EXP/report(template)/code/ex3_algae.py"
python "EXP/report(template)/code/ex4_newton.py"
```

### 安装 / 更新依赖

```bash
conda activate "$(pwd)/.conda/dl"

# 用 conda 安装（优先）
conda install <package>

# 或用 pip
pip install <package>
```

### 启动 Jupyter / Spyder

```bash
conda activate "$(pwd)/.conda/dl"

jupyter notebook    # 浏览器打开 Notebook
spyder              # 启动 Spyder IDE
```

### 导出环境（修改依赖后）

```bash
conda activate "$(pwd)/.conda/dl"
conda env export --prefix .conda/dl > environment.yml
```

### 删除并重建环境

```bash
conda deactivate
conda remove -p .conda/dl --all -y

CONDA_SUBDIR=osx-64 conda create -y -p .conda/dl --file environment.yml
conda config --prefix .conda/dl --set subdir osx-64
```
