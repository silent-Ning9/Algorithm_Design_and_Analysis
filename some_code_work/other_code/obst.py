def OBST_detailed(P, Q, n):
    # 初始化二维数组
    C = [[0.0] * (n + 1) for _ in range(n + 1)]
    W = [[0.0] * (n + 1) for _ in range(n + 1)]
    R = [[0] * (n + 1) for _ in range(n + 1)]

    print("初始化:")
    # 初始化
    for i in range(n):
        # 空树的情况
        W[i][i] = Q[i]
        R[i][i] = 0
        C[i][i] = 0

        # 只有一个结点的情况
        W[i][i + 1] = Q[i] + Q[i + 1] + P[i]
        R[i][i + 1] = i + 1
        C[i][i + 1] = Q[i] + Q[i + 1] + P[i]

    # 处理最后一个对角线元素
    W[n][n] = Q[n]
    R[n][n] = 0
    C[n][n] = 0

    print(f"m=0 (j-i=0):")
    print_matrix(W, C, R, n)

    print(f"m=1 (j-i=1):")
    print_matrix(W, C, R, n)

    # 找有m个结点的最优树
    for m in range(2, n + 1):
        print(f"\n处理 m={m} (j-i={m}):")

        for i in range(0, n - m + 1):
            j = i + m

            # 计算W(i,j)
            W[i][j] = W[i][j - 1] + P[j - 1] + Q[j]

            # 在区间[R(i,j-1), R(i+1,j)]中寻找最优的k
            min_val = float('inf')
            best_k = -1

            # 确定搜索范围
            start_k = R[i][j - 1]
            end_k = R[i + 1][j] if i + 1 <= n else j

            print(f"  计算 C[{i}][{j}]: i={i}, j={j}")
            print(
                f"    W[{i}][{j}] = W[{i}][{j - 1}] + P[{j - 1}] + Q[{j}] = {W[i][j - 1]:.2f} + {P[j - 1]:.2f} + {Q[j]:.2f} = {W[i][j]:.2f}")

            print(f"    在范围 k ∈ [{start_k}, {end_k}] 中寻找最小值:")

            for k in range(start_k, end_k + 1):
                if k < 1 or k > n:
                    continue

                current_val = C[i][k - 1] + C[k][j]
                print(
                    f"      k={k}: C[{i}][{k - 1}] + C[{k}][{j}] = {C[i][k - 1]:.2f} + {C[k][j]:.2f} = {current_val:.2f}")

                if current_val < min_val:
                    min_val = current_val
                    best_k = k

            # 更新C和R
            C[i][j] = W[i][j] + min_val
            R[i][j] = best_k

            print(f"    最小值: {min_val:.2f} (k={best_k})")
            print(f"    C[{i}][{j}] = W[{i}][{j}] + min_val = {W[i][j]:.2f} + {min_val:.2f} = {C[i][j]:.2f}")
            print(f"    R[{i}][{j}] = {best_k}")

        print(f"\n当前矩阵状态 (m={m}):")
        print_matrix(W, C, R, n)

    return C, W, R


def print_matrix(W, C, R, n):
    print("W矩阵:")
    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            if j >= i:
                row.append(f"{W[i][j]:.2f}")
            else:
                row.append(" - ")
        print(f"  {row}")

    print("C矩阵:")
    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            if j >= i:
                row.append(f"{C[i][j]:.2f}")
            else:
                row.append(" - ")
        print(f"  {row}")

    print("R矩阵:")
    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            if j >= i:
                row.append(f"{R[i][j]:2d}")
            else:
                row.append(" -")
        print(f"  {row}")


# 示例使用
if __name__ == "__main__":
    # 示例数据
    # n = 3
    # P = [0.1, 0.2, 0.3]  # 成功检索概率
    # Q = [0.05, 0.1, 0.15, 0.1]  # 不成功检索概率

    # n = 4
    # P = [3, 3, 1, 1]  # 成功检索概率
    # Q = [2, 3, 1, 1, 1]  # 不成功检索概率

    n = 4
    P = [3, 3, 1, 4]  # 成功检索概率
    Q = [1, 3, 2, 1, 1]  # 不成功检索概率

    print("输入数据:")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"n = {n}")
    print()

    C, W, R = OBST_detailed(P, Q, n)

    print("\n最终结果:")
    print_matrix(W, C, R, n)

    print(f"\n最优二分检索树的成本: {C[0][n]:.2f}")
    print(f"根节点: a{R[0][n]}")