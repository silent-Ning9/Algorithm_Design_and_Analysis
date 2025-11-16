#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : kruskal.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 18:56
@Desc       : 
'''

import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    """
    Kruskal算法实现

    参数:
    n: 节点数量
    edges: 边列表，每个元素为 (cost, u, v)

    返回:
    T: 最小生成树的边列表
    mincost: 最小生成树的总成本
    """
    # 构建最小堆
    heap = []
    for cost, u, v in edges:
        heapq.heappush(heap, (cost, u, v))

    uf = UnionFind(n)
    T = []  # 最小生成树的边集
    mincost = 0
    i = 0

    while i < n - 1 and heap:
        cost, u, v = heapq.heappop(heap)

        if uf.find(u) != uf.find(v):
            i += 1
            T.append((u, v))
            mincost += cost
            uf.union(u, v)

    if i != n - 1:
        print('no spanning tree')
        return None, None

    return T, mincost


# 测试示例
def main():
    # 示例: 6个节点的图
    n = 6
    edges = [
        (1, 0, 1), (3, 0, 2), (4, 1, 2),
        (2, 1, 3), (5, 2, 3), (4, 2, 4),
        (6, 3, 4), (7, 3, 5), (3, 4, 5)
    ]

    T, mincost = kruskal(n, edges)

    if T is not None:
        print("最小生成树的边:")
        for u, v in T:
            print(f"({u}, {v})")
        print(f"最小成本: {mincost}")


if __name__ == "__main__":
    main()