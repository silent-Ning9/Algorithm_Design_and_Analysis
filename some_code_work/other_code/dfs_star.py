#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : dfs_star.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 19:45
@Desc       : 
'''


def dfs_spanning_tree(graph, start_node):
    """
    深度优先生成树算法

    参数:
    graph: 图的邻接表表示，字典形式，例如 {0: [1, 2], 1: [0, 3], ...}
    start_node: 开始搜索的节点

    返回:
    tree_edges: 生成树的边集合
    visited_order: 访问顺序列表
    """
    n = len(graph)
    visited = [0] * n  # 访问标记数组，0表示未访问，1表示已访问
    tree_edges = []  # 生成树的边集合
    visited_order = []  # 访问顺序

    def dfs_recursive(v):
        # 标记当前节点为已访问
        visited[v] = 1
        visited_order.append(v)

        # 遍历所有邻接节点
        for w in graph.get(v, []):
            if visited[w] == 0:
                # 将边(v,w)添加到生成树中
                tree_edges.append((v, w))
                dfs_recursive(w)

    # 从起始节点开始DFS
    dfs_recursive(start_node)
    return tree_edges, visited_order


def dfs_spanning_tree_iterative(graph, start_node):
    """
    深度优先生成树算法（迭代版本）

    参数:
    graph: 图的邻接表表示
    start_node: 开始搜索的节点

    返回:
    tree_edges: 生成树的边集合
    visited_order: 访问顺序列表
    """
    n = len(graph)
    visited = [0] * n  # 访问标记数组
    tree_edges = []  # 生成树的边集合
    visited_order = []  # 访问顺序
    stack = []  # 栈用于DFS
    parent = [-1] * n  # 记录每个节点的父节点

    # 将起始节点入栈
    stack.append(start_node)
    parent[start_node] = -1  # 起始节点没有父节点

    while stack:
        v = stack.pop()

        # 如果该节点未被访问
        if visited[v] == 0:
            visited[v] = 1
            visited_order.append(v)

            # 如果有父节点，将边(父节点,当前节点)添加到生成树
            if parent[v] != -1:
                tree_edges.append((parent[v], v))

            # 将邻接节点按逆序入栈（保证访问顺序与递归版本一致）
            for w in reversed(graph.get(v, [])):
                if visited[w] == 0:
                    stack.append(w)
                    # 记录父节点信息
                    if parent[w] == -1:  # 避免重复设置父节点
                        parent[w] = v

    return tree_edges, visited_order


def print_spanning_tree(tree_edges, visited_order, graph):
    """
    打印生成树信息
    """
    print("深度优先生成树:")
    print(f"访问顺序: {visited_order}")
    print("生成树边集合:")
    for edge in tree_edges:
        print(f"  {edge[0]} -- {edge[1]}")

    # 验证生成树性质
    n = len(graph)
    print(f"\n生成树验证:")
    print(f"原图节点数: {n}")
    print(f"生成树边数: {len(tree_edges)}")
    print(f"生成树是否包含所有节点: {len(visited_order) == n}")
    print(f"生成树边数 = 节点数 - 1: {len(tree_edges) == len(visited_order) - 1}")


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

    print("\n" + "=" * 50)
    print("递归版本深度优先生成树:")
    tree_edges_recursive, visited_recursive = dfs_spanning_tree(graph, 0)
    print_spanning_tree(tree_edges_recursive, visited_recursive, graph)

    print("\n" + "=" * 50)
    print("迭代版本深度优先生成树:")
    tree_edges_iterative, visited_iterative = dfs_spanning_tree_iterative(graph, 0)
    print_spanning_tree(tree_edges_iterative, visited_iterative, graph)

    # 测试不连通图
    print("\n" + "=" * 50)
    print("测试不连通图:")

    # 不连通图示例
    # 组件1: 0-1-2  组件2: 3-4
    disconnected_graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }

    print("不连通图的邻接表表示:")
    for node, neighbors in disconnected_graph.items():
        print(f"节点 {node} 的邻居: {neighbors}")

    print("\n从节点0开始的生成树（只包含连通分量）:")
    tree_edges_disconnected, visited_disconnected = dfs_spanning_tree(disconnected_graph, 0)
    print_spanning_tree(tree_edges_disconnected, visited_disconnected, disconnected_graph)