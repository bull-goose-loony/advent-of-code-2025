def execute(grid: list[list[str]]):
    roll_count = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                if get_roll_count(grid, r, c) < 4:
                    roll_count += 1 
    return roll_count

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
    print(execute(grid))


if __name__ == "__main__":
    main()
