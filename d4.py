def execute(grid: list[list[str]]) -> list[tuple[int, int]]:
    to_remove: list[tuple[int, int]] = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                if can_remove(grid, r, c):
                    to_remove.append((r, c))
    return to_remove


def process_grid(grid: list[list[str]]):
    changes: list[tuple[int, int]] = []
    rolls_removed = 0

    while True:
        changes = execute(grid)
        count_to_remove = len(changes) 

        if count_to_remove == 0:
            break
        rolls_removed += count_to_remove
        grid = remove_rolls(grid, changes)

    return rolls_removed

def remove_rolls(grid: list[list[str]], coordinates: list[tuple[int, int]]):
    for x, y in coordinates:
        grid[x][y] = '.'
    return grid

def can_remove(grid: list[list[str]], r: int, c:int):
    if get_roll_count(grid, r, c) < 4:
        return True
    return False

def get_roll_count(grid: list[list[str]], r: int, c:int) -> int:
    row_len = len(grid)
    col_height = len(grid[0])

    # print(f"Iteration r = {r}, c = {c}")

    roll_count = 0
    for sr in range(r-1, r+2):
        if sr < 0:
            continue
        for sc in range(c-1, c+2):
            # print(f'sr = {sr}, sc = {sc}')
            if sc < 0:
                # print('0!')
                continue
            if sr > row_len - 1:
                # print('1!')
                continue
            if sc > col_height - 1:
                # print('2!')
                continue
            if (sr == r) and (sc == c):
                # print('3!')
                continue
            # print(f"grid[sr][sc] = {grid[sr][sc]}")
            if grid[sr][sc] == '@':
                roll_count += 1

    print(f"Roll count = {roll_count}")
    return roll_count

def test():
    print("hi")
    test_content = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    grid: list[list[str]] = [list(line) for line in test_content.splitlines()]
    print(grid)
    sum = execute(grid)
    print(sum)

def lines_to_grid(lines):
    grid: list[list[str]] = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid

def main():
    grid: list[list[str]] = []
    with open("inputs/d4.txt", "r") as file:
        rows = file.readlines()
        for row in rows:
            grid.append(list(row.strip()))
    print(process_grid(grid))


if __name__ == "__main__":
    main()
