import math

def f(x):
    return x**3 + (math.exp(x) / 2) + 5*x - 6

def df(x):
    return 3*x**2 + (math.exp(x) / 2) + 5

def newton_method(initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            print(f"迭代 {i+1} 次后收敛到解: x = {x_new}")
            return x_new
        x = x_new
    print("未收敛，请尝试调整初始值或增加迭代次数。")
    return None

# 选择一个初始猜测值（例如 x0 = 1）
solution = newton_method(initial_guess=1.0)
print(f"方程的近似解为: {solution}")
