def execute(grid: list[list[str]]):
    roll_count = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                sub_grid = get_surrounding_cells(grid, r, c)
                # check 8 surrounding cells.
                if get_roll_count(grid, r, c) < 4:
                    roll_count += 1 

    return roll_count

def get_surrounding_cells(grid: list[list[str]], r: int, c:int):
    # TODO return a 3x3 grid of surrounding cells
    # remember: current cell (r, c) should appear empty
    return 0
    
def get_roll_count(grid: list[list[str]], r: int, c:int) -> int:
    # loop from r-1 c-1 to r+1 c+1
    return 0


def test():
    print("hi")
    test_content = """
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@.
    """
    grid = lines_to_grid(test_content)

def lines_to_grid(lines):
    grid: list[list[str]] = []
    rows = lines.readlines()
    for row in rows:
        grid.append(list(row.strip()))
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
