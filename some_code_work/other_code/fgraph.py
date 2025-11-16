#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : fgraph.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 20:36
@Desc       : 
'''


def fgraph(E, k, n):
    """
    多段图的向前处理算法

    参数:
    E: 边集，字典形式，E[(i,j)]表示边<i,j>的成本
    k: 段数
    n: 结点总数

    返回:
    cost: 各结点到终点的最小成本
    D: 决策数组，记录每个结点的下一个结点
    P: 最小成本路径
    min_cost: 最小成本
    """

    # 初始化
    COST = [float('inf')] * (n + 1)  # 成本数组，索引从1开始
    D = [0] * (n + 1)  # 决策数组，记录每个结点的下一个结点

    # 终点成本为0
    COST[n] = 0

    # 从n-1到1逆序计算每个结点的最小成本
    for j in range(n - 1, 0, -1):
        min_cost = float('inf')
        best_r = -1

        # 寻找使c(j,r) + COST(r)最小的结点r
        for r in range(j + 1, n + 1):
            if (j, r) in E:  # 如果边<j,r>存在
                current_cost = E[(j, r)] + COST[r]
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_r = r

        if best_r != -1:  # 如果找到合适的后继结点
            COST[j] = min_cost
            D[j] = best_r

    # 构建最小成本路径
    P = [0] * (k + 1)  # 路径数组，索引从1开始
    P[1] = 1  # 起点
    P[k] = n  # 终点

    # 填充中间结点
    for j in range(2, k):
        P[j] = D[P[j - 1]]

    return COST, D, P, COST[1]


# 测试示例
def test_fgraph():
    """
    测试多段图算法
    """
    # 示例多段图：4段，8个结点
    # 边集定义
    E = {
        (1, 2): 2, (1, 3): 3, (1, 4): 1,
        (2, 5): 2, (2, 6): 3,
        (3, 5): 1, (3, 6): 2, (3, 7): 4,
        (4, 6): 2, (4, 7): 5,
        (5, 8): 2,
        (6, 8): 3,
        (7, 8): 4
    }

    k = 4  # 4段
    n = 8  # 8个结点

    COST, D, P, min_cost = fgraph(E, k, n)

    print("多段图向前处理算法结果:")
    print(f"最小成本: {min_cost}")
    print(f"成本数组 COST: {COST[1:]}")
    print(f"决策数组 D: {D[1:]}")
    print(f"最小成本路径 P: {P[1:]}")

    # 验证路径成本
    path_cost = 0
    for i in range(1, k):
        path_cost += E[(P[i], P[i + 1])]
    print(f"路径验证成本: {path_cost}")


# 运行测试
if __name__ == "__main__":
    test_fgraph()