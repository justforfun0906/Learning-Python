import pygame
import sys
import random

# === 一些常數設定 ===
GRID_SIZE = 4             # 4x4 棋盤
TILE_SIZE = 100           # 每個方塊的大小 (px)
TILE_MARGIN = 10          # 方塊間距 (px)
WINDOW_SIZE = 800      # 遊戲視窗寬度 & 高度 (可依需求調整)
BG_COLOR = (187, 173, 160)  # 背景色
EMPTY_COLOR = (205, 193, 180)

# 標題字體大小、預設字體大小
TITLE_FONT_SIZE = 40
SCORE_FONT_SIZE = 24

# 顏色配置，可依需求自行修改
TILE_COLORS = {
    0:    (205, 193, 180),
    2:    (238, 228, 218),
    4:    (237, 224, 200),
    8:    (242, 177, 121),
    16:   (245, 149, 99),
    32:   (246, 124, 95),
    64:   (246, 94, 59),
    128:  (237, 207, 114),
    256:  (237, 204, 97),
    512:  (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    # 更大的數字可以自行新增
}

# 數字字體顏色：當數字比較小時使用較深色，大數字使用淺色
FONT_COLORS = {
    2:    (119, 110, 101),
    4:    (119, 110, 101),
    8:    (249, 246, 242),
    16:   (249, 246, 242),
    32:   (249, 246, 242),
    64:   (249, 246, 242),
    128:  (249, 246, 242),
    256:  (249, 246, 242),
    512:  (249, 246, 242),
    1024: (249, 246, 242),
    2048: (249, 246, 242),
    # 以上可根據實際需要增補
}


def create_grid():
    """
    建立 4x4 空棋盤 (值為 0)。
    """
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]


def add_new_tile(board):
    """
    在空位上隨機產生數字 2 或 4。
    """
    empty_cells = [
        (r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0
    ]
    if not empty_cells:
        return

    r, c = random.choice(empty_cells)
    board[r][c] = 4 if random.random() < 0.1 else 2  # 大約 90% 機率產生 2，10% 機率產生 4


def init_board():
    """
    初始化棋盤，隨機產生兩個數字。
    """
    board = create_grid()
    add_new_tile(board)
    add_new_tile(board)
    return board


def compress_line(line):
    """
    移動及合併前，先將一整行的空格 (0) 壓縮，返回新行。
    例如 [2, 0, 2, 4] 會先壓縮為 [2, 2, 4, 0] 以後再做合併。
    """
    new_line = [num for num in line if num != 0]
    new_line += [0] * (GRID_SIZE - len(new_line))
    return new_line


def merge_line(line):
    """
    合併一行，返回合併後的新行以及該行合併產生的分數。
    例如 [2, 2, 4, 0] => [4, 4, 0, 0]，分數增加 4。
    """
    merged_line = []
    score_gain = 0
    skip = False

    for i in range(GRID_SIZE):
        if skip:
            skip = False
            continue

        if i < GRID_SIZE - 1 and line[i] == line[i + 1] and line[i] != 0:
            merged_value = line[i] * 2
            merged_line.append(merged_value)
            score_gain += merged_value
            skip = True
        else:
            merged_line.append(line[i])

    # 補上多餘的 0
    merged_line += [0] * (GRID_SIZE - len(merged_line))
    return merged_line, score_gain


def move_left(board):
    """
    整個棋盤向左移動並合併，並回傳移動後的新棋盤和分數增量。
    """
    new_board = []
    score_gain = 0
    for row in board:
        compressed = compress_line(row)            # 壓縮
        merged, gained = merge_line(compressed)    # 合併
        final_line = compress_line(merged)         # 再壓縮一次 (若合併後出現空格)
        new_board.append(final_line)
        score_gain += gained
    return new_board, score_gain


def move_right(board):
    """
    整個棋盤向右移動並合併。
    先將行反轉，使用 move_left，最後再反轉回去。
    """
    reversed_board = [row[::-1] for row in board]
    moved, score_gain = move_left(reversed_board)
    final_board = [row[::-1] for row in moved]
    return final_board, score_gain


def move_up(board):
    """
    整個棋盤向上移動並合併。
    先做轉置，使用 move_left，最後再轉置回去。
    """
    transposed_board = [list(row) for row in zip(*board)]
    moved, score_gain = move_left(transposed_board)
    final_board = [list(row) for row in zip(*moved)]
    return final_board, score_gain


def move_down(board):
    """
    整個棋盤向下移動並合併。
    先做轉置，使用 move_right，最後再轉置回去。
    """
    transposed_board = [list(row) for row in zip(*board)]
    moved, score_gain = move_right(transposed_board)
    final_board = [list(row) for row in zip(*moved)]
    return final_board, score_gain


def check_game_over(board):
    """
    檢查遊戲是否結束：
    1. 若有空格，未結束。
    2. 若可合併(任何一個鄰近值相等)，未結束。
    3. 否則結束。
    """
    # 1. 檢查是否還有空格
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                return False

    # 2. 檢查可否合併：與右方、下方比較
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if c < GRID_SIZE - 1 and board[r][c] == board[r][c + 1]:
                return False
            if r < GRID_SIZE - 1 and board[r][c] == board[r + 1][c]:
                return False

    # 3. 若都不行，遊戲結束
    return True


def draw_board(screen, board, score, font, title_font):
    """
    將整個棋盤繪製到畫面上。
    """
    screen.fill(BG_COLOR)

    # 繪製標題
    title_surface = title_font.render("2048", True, (119, 110, 101))
    screen.blit(title_surface, (10, 10))

    # 繪製分數
    score_surface = font.render(f"Score: {score}", True, (119, 110, 101))
    screen.blit(score_surface, (10, 60))

    # 繪製方塊
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = board[r][c]
            color = TILE_COLORS.get(value, TILE_COLORS[2048])  # 超過 2048 統一使用同色
            rect_x = c * (TILE_SIZE + TILE_MARGIN) + 10
            rect_y = r * (TILE_SIZE + TILE_MARGIN) + 110
            pygame.draw.rect(screen, color, (rect_x, rect_y, TILE_SIZE, TILE_SIZE), border_radius=5)

            if value > 0:
                text_color = FONT_COLORS.get(value, (249, 246, 242))
                tile_font = pygame.font.SysFont("arial", 32)
                text_surface = tile_font.render(str(value), True, text_color)
                text_rect = text_surface.get_rect(center=(rect_x + TILE_SIZE / 2, rect_y + TILE_SIZE / 2))
                screen.blit(text_surface, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("2048 with Pygame")

    clock = pygame.time.Clock()

    # 設定字體
    score_font = pygame.font.SysFont("arial", SCORE_FONT_SIZE, bold=True)
    title_font = pygame.font.SysFont("arial", TITLE_FONT_SIZE, bold=True)

    board = init_board()
    score = 0

    running = True
    while running:
        clock.tick(60)  # 每秒 60 帧

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                moved = False
                # 記錄下 move 之前的棋盤，用來比較是否有變化
                temp_board = [row[:] for row in board]

                if event.key == pygame.K_LEFT:
                    board, gained = move_left(board)
                    score += gained
                elif event.key == pygame.K_RIGHT:
                    board, gained = move_right(board)
                    score += gained
                elif event.key == pygame.K_UP:
                    board, gained = move_up(board)
                    score += gained
                elif event.key == pygame.K_DOWN:
                    board, gained = move_down(board)
                    score += gained
                else:
                    gained = 0  # 若按下非方向鍵，不做任何處理

                # 檢查是否有實際移動
                if board != temp_board:
                    add_new_tile(board)

        draw_board(screen, board, score, score_font, title_font)
        pygame.display.flip()

        if check_game_over(board):
            print("Game Over!")
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()