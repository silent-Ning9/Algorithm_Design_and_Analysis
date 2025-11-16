#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : knap_forward.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 20:14
@Desc       : 
'''


def knap01_forward(weights, profits, capacity):
    """
    使用向前处理法求解0/1背包问题

    参数:
        weights: 物品重量列表
        profits: 物品价值列表
        capacity: 背包容量

    返回:
        最大价值
    """
    n = len(weights)

    # 初始化g数组，g[i][X]表示从物品i+1到n，容量为X时的最大价值
    # 使用字典来避免处理负容量，更符合递推式中的-∞概念
    g = [{} for _ in range(n + 1)]

    # 初始化边界条件：g_n(X) = 0 (X>=0)
    for X in range(capacity + 1):
        g[n][X] = 0

    # 向前递推：从n-1到0
    for i in range(n - 1, -1, -1):
        for X in range(capacity + 1):
            # 不选第i+1个物品
            not_take = g[i + 1].get(X, float('-inf'))

            # 选第i+1个物品（如果容量允许）
            take = float('-inf')
            if X >= weights[i]:
                take = g[i + 1].get(X - weights[i], float('-inf')) + profits[i]

            # 取两种情况的最大值
            g[i][X] = max(not_take, take)

    # g_0(M)即为所求的最优解
    return g[0][capacity]


def knap01_forward_optimized(weights, profits, capacity):
    """
    优化版本的向前处理法，使用一维数组节省空间
    """
    n = len(weights)

    # 初始化：g[X]表示当前状态下容量为X时的最大价值
    g = [0] * (capacity + 1)

    # 从最后一个物品开始向前处理
    for i in range(n - 1, -1, -1):
        # 需要从后向前更新，避免覆盖
        new_g = [0] * (capacity + 1)

        for X in range(capacity + 1):
            # 不选当前物品
            not_take = g[X]

            # 选当前物品（如果容量允许）
            take = float('-inf')
            if X >= weights[i]:
                take = g[X - weights[i]] + profits[i]

            # 取两种情况的最大值
            new_g[X] = max(not_take, take)

        g = new_g

    return g[capacity]


# 测试示例
if __name__ == "__main__":
    # 示例1
    weights1 = [2, 3, 4, 5]
    profits1 = [3, 4, 5, 6]
    capacity1 = 5

    print("测试示例1:")
    print(f"物品重量: {weights1}")
    print(f"物品价值: {profits1}")
    print(f"背包容量: {capacity1}")

    result1 = knap01_forward(weights1, profits1, capacity1)
    result1_opt = knap01_forward_optimized(weights1, profits1, capacity1)

    print(f"标准方法最大价值: {result1}")
    print(f"优化方法最大价值: {result1_opt}")
    print()

    # 示例2
    weights2 = [1, 2, 3]
    profits2 = [6, 10, 12]
    capacity2 = 5

    print("测试示例2:")
    print(f"物品重量: {weights2}")
    print(f"物品价值: {profits2}")
    print(f"背包容量: {capacity2}")

    result2 = knap01_forward(weights2, profits2, capacity2)
    result2_opt = knap01_forward_optimized(weights2, profits2, capacity2)

    print(f"标准方法最大价值: {result2}")
    print(f"优化方法最大价值: {result2_opt}")