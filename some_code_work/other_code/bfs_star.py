#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : bfs_star.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 19:27
@Desc       : 
'''

from collections import deque
from typing import List, Tuple, Set, Dict, Any


def bfs_star(graph: Dict[Any, List[Any]], start: Any) -> Tuple[Set[Tuple[Any, Any]], List[Any]]:
    """
    广度优先搜索算法实现

    参数:
        graph: 图的邻接表表示，字典形式，键为节点，值为相邻节点列表
        start: 起始节点

    返回:
        T: 生成树的边集合
        visited_order: 节点的访问顺序列表
    """
    # 初始化访问标记字典
    visited = {node: 0 for node in graph}

    # 初始化生成树边集合
    T = set()

    # 初始化访问顺序列表
    visited_order = []

    # 初始化队列
    Q = deque()

    # 标记起始节点为已访问，并加入队列
    visited[start] = 1
    u = start
    visited_order.append(start)

    while True:
        # 遍历u的所有邻接节点w
        for w in graph.get(u, []):
            if visited.get(w, 0) == 0:  # w未被访问
                # 添加边(u, w)到生成树
                T.add((u, w))
                # 将w加入队列
                Q.append(w)
                # 标记w为已访问
                visited[w] = 1
                visited_order.append(w)

        # 如果队列为空，算法结束
        if not Q:
            break

        # 从队列中取出下一个节点
        u = Q.popleft()

    return T, visited_order


def bfs_star_with_trace(graph: Dict[Any, List[Any]], start: Any) -> Tuple[Set[Tuple[Any, Any]], List[Any]]:
    """
    带追踪信息的BFS实现，用于演示算法执行过程
    """
    visited = {node: 0 for node in graph}
    T = set()
    visited_order = []
    Q = deque()

    visited[start] = 1
    u = start
    visited_order.append(start)

    print(f"开始BFS，起始节点: {start}")
    print(f"初始状态: u = {u}, Q = {list(Q)}, T = {T}")

    step = 1

    while True:
        print(f"\n步骤 {step}: 处理节点 u = {u}")

        # 遍历u的所有邻接节点w
        for w in graph.get(u, []):
            print(f"  检查边 ({u}, {w}) - VISITED[{w}] = {visited.get(w, 0)}")
            if visited.get(w, 0) == 0:
                T.add((u, w))
                Q.append(w)
                visited[w] = 1
                visited_order.append(w)
                print(f"    → 添加边 ({u}, {w}) 到 T")
                print(f"    → 将 {w} 加入队列 Q")
                print(f"    → 标记 {w} 为已访问")

        print(f"  当前状态: Q = {list(Q)}, T = {T}")

        if not Q:
            print("\n队列为空，BFS结束")
            break

        u = Q.popleft()
        print(f"  从队列取出下一个节点: u = {u}")
        step += 1

    return T, visited_order


# 测试示例
if __name__ == "__main__":
    # 示例图
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("=== BFS算法实现 ===")
    print("图结构:", graph)

    # 使用带追踪的版本演示
    T, visited_order = bfs_star_with_trace(graph, 'A')

    print(f"\n=== 最终结果 ===")
    print(f"生成树边集合 T: {T}")
    print(f"节点访问顺序: {visited_order}")

    # 使用标准版本
    print(f"\n=== 标准版本结果 ===")
    T_std, order_std = bfs_star(graph, 'A')
    print(f"生成树边集合 T: {T_std}")
    print(f"节点访问顺序: {order_std}")