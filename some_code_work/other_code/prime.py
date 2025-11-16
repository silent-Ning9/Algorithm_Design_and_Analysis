#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : prime.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 18:41
@Desc       : 
'''

import sys


def prim(E, COST, n):
    """
    Prim最小生成树算法实现

    参数:
    E: 图的边集 (这里实际上未直接使用，因为使用邻接矩阵COST)
    COST: n*n的成本邻接矩阵，COST[i][j]表示边(i,j)的成本，无边时为float('inf')
    n: 结点数量

    返回:
    T: 最小生成树的边列表，每个元素为(起点, 终点)
    mincost: 最小生成树的总成本
    """
    # 初始化
    T = []  # 存储最小生成树的边
    mincost = 0
    NEAR = [0] * n  # 记录每个顶点距离最小生成树最近的顶点

    # 步骤3-5: 找到初始最小成本边
    min_edge = None
    min_cost_val = float('inf')

    # 遍历所有可能的边找到最小成本边
    for i in range(n):
        for j in range(i + 1, n):  # 避免重复和自环
            if COST[i][j] < min_cost_val:
                min_cost_val = COST[i][j]
                min_edge = (i, j)

    if min_edge is None:
        print('no spanning tree')
        return [], float('inf')

    k, l = min_edge
    mincost = min_cost_val
    T.append((k, l))

    # 步骤6-10: 初始化NEAR数组
    for i in range(n):
        if i == k or i == l:
            continue
        if COST[i][l] < COST[i][k]:
            NEAR[i] = l
        else:
            NEAR[i] = k

    # 步骤11: 将k和l标记为已加入最小生成树
    NEAR[k] = -1  # 使用-1表示已加入最小生成树
    NEAR[l] = -1

    # 步骤12-20: 寻找剩余的n-2条边
    for _ in range(2, n):  # 还需要找n-2条边
        # 找到NEAR中不为-1且COST最小的顶点
        min_cost_val = float('inf')
        j = -1

        for i in range(n):
            if NEAR[i] != -1 and COST[i][NEAR[i]] < min_cost_val:
                min_cost_val = COST[i][NEAR[i]]
                j = i

        if j == -1:  # 没有找到合适的边
            print('no spanning tree')
            return [], float('inf')

        # 将边(j, NEAR[j])加入最小生成树
        T.append((j, NEAR[j]))
        mincost += min_cost_val
        NEAR[j] = -1  # 标记j为已加入

        # 更新NEAR数组
        for k in range(n):
            if NEAR[k] != -1 and COST[k][NEAR[k]] > COST[k][j]:
                NEAR[k] = j

    if mincost > float('inf') / 2:  # 处理浮点数无穷大的比较
        print('no spanning tree')
        return [], float('inf')

    return T, mincost


# 测试示例
def test_prim():
    # 示例1: 简单的连通图
    n = 4
    COST = [
        [float('inf'), 2, 3, float('inf')],
        [2, float('inf'), 1, 4],
        [3, 1, float('inf'), 5],
        [float('inf'), 4, 5, float('inf')]
    ]

    T, mincost = prim([], COST, n)
    print("最小生成树的边:", T)
    print("总成本:", mincost)

    # 示例2: 不连通图
    print("\n测试不连通图:")
    n = 4
    COST = [
        [float('inf'), 2, float('inf'), float('inf')],
        [2, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), 1],
        [float('inf'), float('inf'), 1, float('inf')]
    ]

    T, mincost = prim([], COST, n)
    print("最小生成树的边:", T)
    print("总成本:", mincost)


if __name__ == "__main__":
    test_prim()