#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : dijkstra.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 19:02
@Desc       : 
'''

import sys


def SHORTEST_PATHS(v, COST, n):
    """
    Dijkstra算法实现 - 单源最短路径

    参数:
    v: 起始节点索引(从0开始)
    COST: 成本邻接矩阵，COST[i][j]表示从节点i到节点j的成本
    n: 节点数量

    返回:
    DIST: 从起始节点v到所有其他节点的最短距离列表
    """
    # 初始化
    S = [0] * n  # 记录节点是否已确定最短路径
    DIST = [0] * n  # 记录从v到各节点的最短距离

    # 初始化DIST数组为从v到各节点的直接成本
    for i in range(n):
        DIST[i] = COST[v][i]

    # 起始节点v加入集合S
    S[v] = 1
    DIST[v] = 0

    print(f"初始状态: DIST = {DIST}")

    # 处理剩余的n-1个节点
    for num in range(2, n):  # 从2到n-1，共n-2次循环
        # 找到当前DIST最小的未访问节点
        min_dist = sys.maxsize
        u = -1

        for w in range(n):
            if S[w] == 0 and DIST[w] < min_dist:
                min_dist = DIST[w]
                u = w

        if u == -1:  # 如果没有找到可达节点，提前结束
            break

        # 将节点u加入集合S
        S[u] = 1
        print(f"第{num - 1}步: 选择节点{u}, DIST[{u}] = {DIST[u]}")

        # 更新所有未访问节点的距离
        for w in range(n):
            if S[w] == 0:
                new_dist = DIST[u] + COST[u][w]
                if new_dist < DIST[w]:
                    DIST[w] = new_dist
                    print(f"  更新节点{w}: {DIST[u]} + {COST[u][w]} = {new_dist}")

        print(f"  当前DIST: {DIST}")

    return DIST


# 测试示例
def test_shortest_paths():
    # 定义无穷大，表示不可达
    INF = sys.maxsize

    # 示例图的成本邻接矩阵
    # 节点: 0, 1, 2, 3
    # COST = [
    #     [0, 10, INF, 30, 100],  # 从节点0出发
    #     [INF, 0, 50, INF, 30],  # 从节点1出发
    #     [1, INF, 0, INF, 10],  # 从节点2出发
    #     [INF, 5, 20, 0, 60],  # 从节点3出发
    #     [INF, INF, 10, INF, 0]  # 从节点4出发
    # ]

    COST = [
        [0, 3, INF, 5, INF],  # 从节点0出发
        [INF, 0, 6, 2, INF],  # 从节点1出发
        [INF, INF, 0, INF, 2],  # 从节点2出发
        [INF, 1, 4, 0, 6],  # 从节点3出发
        [3, INF, 7, INF, 0]  # 从节点4出发
    ]

    n = 5  # 节点数量
    start_node = 4  # 起始节点

    print("图的可达性矩阵:")
    for i in range(n):
        for j in range(n):
            if COST[i][j] == INF:
                print("INF", end="\t")
            else:
                print(COST[i][j], end="\t")
        print()

    print(f"\n从节点{start_node}出发的最短路径计算:")
    result = SHORTEST_PATHS(start_node, COST, n)

    print(f"\n最终结果 - 从节点{start_node}到各节点的最短距离:")
    for i in range(n):
        if result[i] == INF:
            print(f"到节点{i}: 不可达")
        else:
            print(f"到节点{i}: {result[i]}")


if __name__ == "__main__":
    test_shortest_paths()
