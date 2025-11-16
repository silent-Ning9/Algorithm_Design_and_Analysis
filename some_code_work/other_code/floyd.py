#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : floyd.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 20:53
@Desc       : 
'''


def all_paths(cost, n):
    """
    计算每对结点之间的最短路径长度

    参数:
    cost: n x n 的成本邻接矩阵，cost[i][i] = 0
    n: 结点数量

    返回:
    A: n x n 的最短路径成本矩阵
    """
    # 初始化距离矩阵
    A = [[0] * n for _ in range(n)]

    # 用cost矩阵对A初始化
    for i in range(n):
        for j in range(n):
            A[i][j] = cost[i][j]

    # Floyd-Warshall算法核心
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 如果通过中间节点k的路径更短，则更新
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

    return A


# 示例用法
if __name__ == "__main__":
    # 示例成本矩阵 (4个节点)
    # 节点到自身的距离为0，不可达的用一个大数表示(如float('inf'))
    INF = float('inf')
    # cost_matrix = [
    #     [0, 3, INF, 5],
    #     [2, 0, INF, 4],
    #     [INF, 1, 0, INF],
    #     [INF, INF, 2, 0]
    # ]

    # cost_matrix = [
    #     [0, INF, INF, INF, 1, INF],
    #     [1, 0, INF, 2, INF, INF],
    #     [INF, 2, 0, INF, INF, 8],
    #     [4, INF, INF, 0, 3, INF],
    #     [INF, 7, INF, INF, 0, INF],
    #     [INF, 5, 10, INF, INF, 0],
    # ]

    cost_matrix = [
        [0, 0, 0, 0, INF, INF, INF],
        [INF, 0, INF, INF, INF, 4, INF],
        [INF, INF, 0, INF, 5, 4, INF],
        [INF, INF, INF, 0, 6, 3, INF],
        [INF, -2, INF, INF, 0, INF, 3],
        [INF, INF, INF, INF, INF, 0, 12],
        [INF, INF, INF, INF, -3, INF, 0],
    ]

    n_nodes = 7
    result = all_paths(cost_matrix, n_nodes)

    print("最短路径成本矩阵:")
    for row in result:
        print([f"{x:d}" if x != INF else "INF" for x in row])