#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project    : ADA
@File       : search.py
@IDE        : PyCharm
@Author     : silent
@Date       : 2025/11/14 19:39
@Desc       : 
'''


class TreeNode:
    def __init__(self, ident, left=None, right=None):
        self.ident = ident
        self.left = left
        self.right = right


def search_tree(root, x):
    """
    在二分检索树中搜索值x
    :param root: 树的根节点
    :param x: 要搜索的值
    :return: 如果找到返回节点，否则返回None
    """
    current = root
    while current is not None:
        if x < current.ident:
            current = current.left
        elif x == current.ident:
            return current
        else:  # x > current.ident
            current = current.right
    return None


# 使用示例
if __name__ == "__main__":
    # 构建示例树
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   2  4 6  8
    root = TreeNode(5,
                    TreeNode(3,
                             TreeNode(2),
                             TreeNode(4)),
                    TreeNode(7,
                             TreeNode(6),
                             TreeNode(8)))

    # 测试搜索
    test_values = [4, 6, 9]
    for val in test_values:
        result = search_tree(root, val)
        if result:
            print(f"找到值 {val}")
        else:
            print(f"值 {val} 未找到")