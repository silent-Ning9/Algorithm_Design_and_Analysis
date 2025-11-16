#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : chess_move.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/7 17:35
@Desc       : 
'''

"""
有2n个棋子(n≥4)排成一行，白子用0表示，黑子用1表示，
例如n=5时初始状态为：0000011111__（后面至少有两个空位）

要求通过棋子移动最终成为：0101010101

移动规则：
① 每次同时移动相邻两个棋子，颜色不限，移动方向不限
② 每次移动必须跳过若干棋子
③ 不能调换两个棋子的位置

"""



def chess(n):
    """
    实现Chess递归过程
    参数n: 当前处理的数字
    """
    moves = []  # 存储移动步骤

    def record_move(from_pos, to_pos):
        """记录移动步骤的辅助函数"""
        moves.append((from_pos, to_pos))
        print(f"move {from_pos} → {to_pos}")

    if n == 4:
        # 递归出口：n=4时的固定移动序列
        record_move((4, 5), (9, 10))
        record_move((8, 9), (4, 5))
        record_move((2, 3), (8, 9))
        record_move((7, 8), (2, 3))
        record_move((1, 2), (7, 8))
    else:
        # 递归情况
        record_move((n, n + 1), (2 * n + 1, 2 * n + 2))
        record_move((2 * n - 1, 2 * n), (n, n + 1))

        # 递归调用
        print(f"调用 Chess({n - 1})")
        chess(n - 1)

    return moves


# 测试函数
def test_chess():
    print("=== 测试 Chess(4) ===")
    moves_4 = chess(4)
    print(f"总共 {len(moves_4)} 步移动")

    print("\n=== 测试 Chess(5) ===")
    moves_5 = chess(5)
    print(f"总共 {len(moves_5)} 步移动")

    print("\n=== 测试 Chess(6) ===")
    moves_6 = chess(6)
    print(f"总共 {len(moves_6)} 步移动")


# 运行测试
if __name__ == "__main__":
    test_chess()