#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : knap.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 18:26
@Desc       : 
'''


def knap(m, n, weights):
    """
    0/1背包问题的递归解法

    参数:
    m: 当前背包剩余容量
    n: 当前考虑的物品编号(从1开始)
    weights: 物品重量列表
    """
    # 获取第n个物品的重量(注意索引从0开始)
    m_n = weights[n - 1]

    # 情况1: 当前物品正好装满背包
    if m - m_n == 0:
        return True

    # 情况2: 当前物品可以放入背包
    elif m - m_n > 0:
        if n > 1:
            # 尝试放入当前物品，递归检查剩余容量和剩余物品
            if knap(m - m_n, n - 1, weights):
                return True
            else:
                # 如果不放入当前物品，检查剩余物品
                return knap(m, n - 1, weights)
        else:
            # 没有更多物品可以尝试
            return False

    # 情况3: 当前物品太重，无法放入
    else:  # m - m_n < 0
        if n > 1:
            # 跳过当前物品，检查剩余物品
            return knap(m, n - 1, weights)
        else:
            # 没有更多物品可以尝试
            return False


# 使用示例
def solve_knapsack(target_weight, weights):
    """
    解决0/1背包问题的包装函数

    参数:
    target_weight: 目标背包容量
    weights: 物品重量列表
    """
    n = len(weights)
    return knap(target_weight, n, weights)


# 测试示例
if __name__ == "__main__":
    # 示例1
    weights1 = [3, 5, 8, 9, 10]
    target1 = 20
    result1 = solve_knapsack(target1, weights1)
    print(f"目标重量 {target1}, 物品重量 {weights1}: {result1}")

    # 示例2
    weights2 = [1, 4, 6, 8]
    target2 = 12
    result2 = solve_knapsack(target2, weights2)
    print(f"目标重量 {target2}, 物品重量 {weights2}: {result2}")

    # 示例3 - 无解情况
    weights3 = [3, 5, 7]
    target3 = 2
    result3 = solve_knapsack(target3, weights3)
    print(f"目标重量 {target3}, 物品重量 {weights3}: {result3}")