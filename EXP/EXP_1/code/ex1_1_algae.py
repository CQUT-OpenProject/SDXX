"""实验 1-1：用循环计算池塘中的水藻数量。"""

# 实验开始时（第 1 周）池塘中有 1 颗水藻。
algae_count = 1

# 每颗水藻每周长出 3 颗新水藻，因此下一周的总数是本周的 4 倍。
weekly_growth_factor = 4
last_week_number = 10

# 第 1 周的数量已知，从第 2 周开始逐周计算，直到第 10 周。
for week_number in range(2, last_week_number + 1):
    algae_count = algae_count * weekly_growth_factor
    print(f"第 {week_number} 周的水藻数量：{algae_count}")

# 循环结束后，algae_count 保存第 10 周的水藻数量。
print(f"十周后，池塘中有 {algae_count} 颗水藻。")
