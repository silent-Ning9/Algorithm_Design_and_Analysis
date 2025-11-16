#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : bfs.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 19:22
@Desc       : 
'''

from collections import deque


def BFS(graph, start_node):
    """
    广度优先搜索算法

    参数:
    graph: 字典，表示图的邻接表，格式为 {节点: [邻居节点列表]}
    start_node: 开始搜索的节点

    返回:
    visited: 访问过的节点列表，按访问顺序排列
    """
    # 初始化访问标记字典
    VISITED = {}
    for node in graph:
        VISITED[node] = 0

    # 初始化队列
    Q = deque()

    # 标记起始节点为已访问
    VISITED[start_node] = 1
    u = start_node

    # 记录访问顺序
    visited_order = [start_node]

    while True:
        # 遍历u的所有邻居节点
        for w in graph.get(u, []):
            if VISITED[w] == 0:  # 如果w未被访问
                Q.append(w)  # 将w加入队列
                VISITED[w] = 1  # 标记w为已访问
                visited_order.append(w)

        # 如果队列为空，则结束搜索
        if not Q:
            return visited_order

        # 从队列中取出下一个节点
        u = Q.popleft()


# 测试示例
if __name__ == "__main__":
    # 示例图 (无向图)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("图的邻接表:", graph)

    # 从节点'A'开始BFS
    result = BFS(graph, 'A')
    print("BFS访问顺序:", result)

    # 另一个测试用例
    graph2 = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }

    print("\n图的邻接表:", graph2)
    result2 = BFS(graph2, 0)
    print("BFS访问顺序:", result2)