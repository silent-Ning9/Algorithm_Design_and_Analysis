#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : dfs.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 19:41
@Desc       : 
'''


def dfs(graph, start_node):
    """
    图的深度优先搜索算法

    参数:
    graph: 图的邻接表表示，字典形式，例如 {0: [1, 2], 1: [0, 3], ...}
    start_node: 开始搜索的节点

    返回:
    visited: 访问顺序列表
    """
    n = len(graph)
    visited = [0] * n  # 访问标记数组，0表示未访问，1表示已访问
    result = []  # 存储访问顺序

    def dfs_recursive(v):
        # 标记当前节点为已访问
        visited[v] = 1
        result.append(v)

        # 遍历所有邻接节点
        for w in graph.get(v, []):
            if visited[w] == 0:
                dfs_recursive(w)

    # 从起始节点开始DFS
    dfs_recursive(start_node)
    return result


def dfs_iterative(graph, start_node):
    """
    图的深度优先搜索算法（迭代版本，避免递归深度限制）

    参数:
    graph: 图的邻接表表示
    start_node: 开始搜索的节点

    返回:
    visited_order: 访问顺序列表
    """
    n = len(graph)
    visited = [0] * n  # 访问标记数组
    stack = []  # 栈用于DFS
    result = []  # 存储访问顺序

    # 将起始节点入栈
    stack.append(start_node)

    while stack:
        v = stack.pop()

        # 如果该节点未被访问
        if visited[v] == 0:
            visited[v] = 1
            result.append(v)

            # 将邻接节点按逆序入栈（保证访问顺序与递归版本一致）
            for w in reversed(graph.get(v, [])):
                if visited[w] == 0:
                    stack.append(w)

    return result


# 测试代码
if __name__ == "__main__":
    # 示例图 (无向图)
    # 0 - 1 - 3
    # |   |
    # 2   4
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1]
    }

    print("图的邻接表表示:")
    for node, neighbors in graph.items():
        print(f"节点 {node} 的邻居: {neighbors}")

    print("\n递归DFS遍历结果:")
    result_recursive = dfs(graph, 0)
    print(f"访问顺序: {result_recursive}")

    print("\n迭代DFS遍历结果:")
    result_iterative = dfs_iterative(graph, 0)
    print(f"访问顺序: {result_iterative}")

    # 验证两种方法结果是否一致
    print(f"\n两种方法结果一致: {result_recursive == result_iterative}")