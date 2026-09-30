"""实验 1-2：用牛顿迭代法求方程的近似根。"""

import math


def calculate_function_value(x_value):
    """计算 f(x) = x^3 + e^x / 2 + 5x - 6。"""
    return x_value**3 + math.exp(x_value) / 2 + 5 * x_value - 6


def calculate_derivative_value(x_value):
    """计算上面函数的导数 f'(x) = 3x^2 + e^x / 2 + 5。"""
    return 3 * x_value**2 + math.exp(x_value) / 2 + 5


def find_root_by_newton(initial_guess, tolerance=0.0001, max_iterations=100):
    """从初始值出发，反复使用牛顿公式寻找方程的近似根。

    当相邻两次得到的 x 值之差小于 tolerance 时，认为结果已经收敛。
    """
    current_x = initial_guess

    # 最多迭代 max_iterations 次，避免在无法收敛时无限循环。
    for iteration_number in range(1, max_iterations + 1):
        function_value = calculate_function_value(current_x)
        derivative_value = calculate_derivative_value(current_x)

        # 牛顿公式需要除以导数；导数为 0 时无法继续计算。
        if derivative_value == 0:
            print("当前点的导数为 0，牛顿迭代无法继续。")
            return None

        # 牛顿迭代公式：下一个近似值 = 当前值 - f(当前值) / f'(当前值)。
        next_x = current_x - function_value / derivative_value

        # 实验要求以相邻两次近似值的差小于 0.0001 作为结束条件。
        if abs(next_x - current_x) < tolerance:
            print(f"迭代 {iteration_number} 次后收敛到近似根：x = {next_x}")
            return next_x

        # 本次还未达到精度要求，把新值作为下一轮的当前值。
        current_x = next_x

    print("达到最大迭代次数仍未收敛，请尝试更换初始值。")
    return None


if __name__ == "__main__":
    # 初始猜测值可以影响牛顿法的收敛过程；本实验从 x = 1 开始。
    initial_guess = 1.0
    approximate_root = find_root_by_newton(initial_guess)
    print(f"方程的近似解为：{approximate_root}")
