x = 1  # 初始条件：第 1 周有 1 颗水藻
for week in range(2, 11):  # 从第 2 周迭代到第 10 周
    x = x * 4  # 迭代关系式
    print(f"第{week}周的水藻数量：{x}")
print(f"十周后，池塘中有 {x} 颗水藻。")
