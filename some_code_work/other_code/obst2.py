def calculate_obst_matrix(P, Q):
    n = len(P)
    # 初始化矩阵
    W = [[0] * (n + 1) for _ in range(n + 1)]
    C = [[0] * (n + 1) for _ in range(n + 1)]
    R = [[0] * (n + 1) for _ in range(n + 1)]

    # 初始化对角线元素 (j-i = 0)
    for i in range(n + 1):
        W[i][i] = Q[i]
        C[i][i] = 0
        R[i][i] = 0

    # 计算不同长度的子树 (j-i = 1, 2, ..., n)
    for length in range(1, n + 1):
        for i in range(0, n - length + 1):
            j = i + length

            # 计算 W(i,j)
            W[i][j] = W[i][j - 1] + P[j - 1] + Q[j]

            # 寻找最优的根节点 k
            min_cost = float('inf')
            best_k = -1

            # 在可能的范围内寻找最优 k
            for k in range(i + 1, j + 1):
                current_cost = C[i][k - 1] + C[k][j]
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_k = k

            # 计算 C(i,j) 和 R(i,j)
            C[i][j] = min_cost + W[i][j]
            R[i][j] = best_k

    return W, C, R


def print_obst_matrix_by_difference(W, C, R, n):
    # 创建矩阵用于显示 - 行索引为 j-i，列索引为 i
    matrix = [["" for _ in range(n + 1)] for _ in range(n + 1)]

    # 填充矩阵
    for d in range(n + 1):  # d = j-i
        for i in range(0, n + 1 - d):  # i 从 0 到 n-d
            j = i + d
            matrix[d][i] = (W[i][j], C[i][j], R[i][j])

    # 打印矩阵
    print("最优二分检索树矩阵 (j-i 为行, i 为列):")
    print("     " + "   ".join([f"i={i}" for i in range(n + 1)]))
    print("     " + "-" * (8 * (n + 1)))

    for d in range(n + 1):
        row_str = f"j-i={d} |"
        for i in range(n + 1):
            if i <= n - d:  # 只显示有效的单元格
                w, c, r = matrix[d][i]
                row_str += f" ({w:2d},{c:2d},{r})".center(8)
            else:
                row_str += " " * 8
        print(row_str)


def print_tree_structure(R, i, j):
    """递归打印树结构"""
    if i == j:
        return f"d{i}"

    k = R[i][j]
    left = print_tree_structure(R, i, k - 1)
    right = print_tree_structure(R, k, j)
    return f"a{k}({left},{right})"


# 使用示例数据
if __name__ == "__main__":
    # 示例数据
    # P = [3, 3, 1, 1]  # 成功检索概率 P[1]到P[4]
    # Q = [2, 3, 1, 1, 1]  # 不成功检索概率 Q[0]到Q[4]

    # P = [3, 3, 1, 4]  # 成功检索概率 P[1]到P[4]
    # Q = [1, 3, 2, 1, 1]  # 不成功检索概率 Q[0]到Q[4]

    P = [15, 25, 15, 5]  # 成功检索概率 P[1]到P[4]
    Q = [10, 3, 4, 3, 20]  # 不成功检索概率 Q[0]到Q[4]

    # 计算矩阵
    W, C, R = calculate_obst_matrix(P, Q)
    n = len(P)

    # 打印矩阵
    print_obst_matrix_by_difference(W, C, R, n)

    # 打印树结构
    print(f"\n最优二分检索树的结构:")
    print(f"根节点: a{R[0][n]}")
    print(f"总成本: {C[0][n]}")
    tree_structure = print_tree_structure(R, 0, n)
    print(f"树结构: {tree_structure}")

    # 验证计算过程
    print("\n计算过程验证:")
    print(f"W(0,4) = W(0,3) + P(4) + Q(4) = {W[0][3]} + {P[3]} + {Q[4]} = {W[0][4]}")
    print(f"C(0,4) = W(0,4) + min{{C(0,0)+C(1,4), C(0,1)+C(2,4), C(0,2)+C(3,4), C(0,3)+C(4,4)}}")
    print(
        f"       = {W[0][4]} + min{{{C[0][0]}+{C[1][4]}, {C[0][1]}+{C[2][4]}, {C[0][2]}+{C[3][4]}, {C[0][3]}+{C[4][4]}}}")
    print(
        f"       = {W[0][4]} + min{{{C[0][0] + C[1][4]}, {C[0][1] + C[2][4]}, {C[0][2] + C[3][4]}, {C[0][3] + C[4][4]}}}")
    print(f"       = {W[0][4]} + {min(C[0][0] + C[1][4], C[0][1] + C[2][4], C[0][2] + C[3][4], C[0][3] + C[4][4])}")
    print(f"       = {C[0][4]}")
    print(f"R(0,4) = {R[0][4]}")