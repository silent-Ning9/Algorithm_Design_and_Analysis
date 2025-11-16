import numpy as np
import matplotlib.pyplot as plt


class ChessBoardCover:
    def __init__(self, k):
        """
        初始化棋盘
        k: 棋盘大小为 2^k × 2^k
        """
        self.size = 2 ** k
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.tile_count = 1  # 从1开始计数，0表示未覆盖

    def cover_board(self, tr, tc, dr, dc, size):
        """
        分治法覆盖棋盘
        tr, tc: 当前棋盘左上角坐标
        dr, dc: 特殊方格坐标
        size: 当前棋盘大小
        """
        if size == 1:
            return

        # 将棋盘分成4个子棋盘
        half_size = size // 2
        current_tile = self.tile_count
        self.tile_count += 1

        # 判断特殊方格在哪个子棋盘
        # 1: 左上子棋盘
        if dr < tr + half_size and dc < tc + half_size:
            self.cover_board(tr, tc, dr, dc, half_size)
        else:
            # 在左上子棋盘的右下角放置骨牌
            self.board[tr + half_size - 1][tc + half_size - 1] = current_tile
            self.cover_board(tr, tc, tr + half_size - 1, tc + half_size - 1, half_size)

        # 2: 右上子棋盘
        if dr < tr + half_size and dc >= tc + half_size:
            self.cover_board(tr, tc + half_size, dr, dc, half_size)
        else:
            # 在右上子棋盘的左下角放置骨牌
            self.board[tr + half_size - 1][tc + half_size] = current_tile
            self.cover_board(tr, tc + half_size, tr + half_size - 1, tc + half_size, half_size)

        # 3: 左下子棋盘
        if dr >= tr + half_size and dc < tc + half_size:
            self.cover_board(tr + half_size, tc, dr, dc, half_size)
        else:
            # 在左下子棋盘的右上角放置骨牌
            self.board[tr + half_size][tc + half_size - 1] = current_tile
            self.cover_board(tr + half_size, tc, tr + half_size, tc + half_size - 1, half_size)

        # 4: 右下子棋盘
        if dr >= tr + half_size and dc >= tc + half_size:
            self.cover_board(tr + half_size, tc + half_size, dr, dc, half_size)
        else:
            # 在右下子棋盘的左上角放置骨牌
            self.board[tr + half_size][tc + half_size] = current_tile
            self.cover_board(tr + half_size, tc + half_size, tr + half_size, tc + half_size, half_size)

    def set_special_cell(self, row, col):
        """设置特殊方格位置"""
        self.board[row][col] = -1  # 用-1表示特殊方格

    def solve(self, special_row, special_col):
        """解决棋盘覆盖问题"""
        self.set_special_cell(special_row, special_col)
        self.cover_board(0, 0, special_row, special_col, self.size)
        return self.board

    def visualize(self):
        """可视化棋盘覆盖结果"""
        fig, ax = plt.subplots(figsize=(10, 10))

        # 创建颜色映射
        colors = plt.cm.tab20(np.linspace(0, 1, self.tile_count + 2))

        # 绘制棋盘
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -1:  # 特殊方格
                    color = 'blue'
                elif self.board[i][j] == 0:  # 未覆盖的方格
                    color = 'white'
                else:
                    color = colors[self.board[i][j] % len(colors)]

                rect = plt.Rectangle((j, self.size - 1 - i), 1, 1,
                                     facecolor=color, edgecolor='black', linewidth=2)
                ax.add_patch(rect)

                # 添加数字标签
                if self.board[i][j] == -1:
                    ax.text(j + 0.5, self.size - 1 - i + 0.5, 'S',
                            ha='center', va='center', fontsize=14, fontweight='bold', color='white')
                elif self.board[i][j] > 0:
                    ax.text(j + 0.5, self.size - 1 - i + 0.5, str(self.board[i][j]),
                            ha='center', va='center', fontsize=10, fontweight='bold')

        ax.set_xlim(0, self.size)
        ax.set_ylim(0, self.size)
        ax.set_aspect('equal')
        ax.set_xticks(range(self.size + 1))
        ax.set_yticks(range(self.size + 1))
        ax.grid(True, color='black', linewidth=1)
        ax.set_title(f'Chess Board Cover (Size: {self.size}×{self.size})', fontsize=16, pad=20)
        ax.set_xlabel('Column', fontsize=12)
        ax.set_ylabel('Row', fontsize=12)

        # 添加图例
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='blue', label='Special Cell'),
            Patch(facecolor='lightgray', label='L-shaped Tiles')
        ]
        ax.legend(handles=legend_elements, loc='upper right')

        plt.tight_layout()
        plt.show()


def print_board_info(board):
    """打印棋盘信息"""
    unique_tiles = np.unique(board)
    tile_count = len(unique_tiles) - 1 if -1 in unique_tiles else len(unique_tiles)
    print(f"棋盘大小: {board.shape[0]}×{board.shape[1]}")
    print(f"使用的骨牌数量: {tile_count}")
    print(f"特殊方格标记: -1")
    print("棋盘布局:")
    print(board)


def main():
    # 测试示例
    # k = 3  # 棋盘大小为 8×8
    # special_row, special_col = 2, 3  # 特殊方格位置

    k = int(input("请输入棋盘的大小 k（2^k × 2^k）: "))
    special_row = int(input("请输入特殊方格的行位置（从0开始）: "))
    special_col = int(input("请输入特殊方格的列位置（从0开始）: "))

    print("=== 棋盘覆盖问题解决方案 ===")
    print(f"棋盘大小: 2^{k} × 2^{k} = {2 ** k} × {2 ** k}")
    print(f"特殊方格位置: ({special_row}, {special_col})")
    print()

    # 创建并解决问题
    solver = ChessBoardCover(k)
    result = solver.solve(special_row, special_col)

    # 打印结果信息
    print_board_info(result)
    print()

    # 计算理论骨牌数量
    total_cells = 2 ** k * 2 ** k
    theoretical_tiles = (total_cells - 1) // 3
    print(f"理论骨牌数量: {theoretical_tiles} (每个L型骨牌覆盖3个方格)")

    # 可视化结果
    print("\n生成可视化图表...")
    solver.visualize()


# 测试不同大小的棋盘
def test_different_sizes():
    """测试不同大小的棋盘"""
    test_cases = [
        (2, 1, 1),  # 4×4棋盘，特殊方格在(1,1)
        (3, 2, 3),  # 8×8棋盘，特殊方格在(2,3)
        (3, 5, 6),  # 8×8棋盘，特殊方格在(5,6)
    ]

    for k, sr, sc in test_cases:
        print(f"\n{'=' * 50}")
        print(f"测试 {2 ** k}×{2 ** k} 棋盘，特殊方格在({sr},{sc})")
        print('=' * 50)

        solver = ChessBoardCover(k)
        result = solver.solve(sr, sc)
        print_board_info(result)


if __name__ == "__main__":
    main()

    # 取消注释下面的行来测试不同大小的棋盘
    # test_different_sizes()