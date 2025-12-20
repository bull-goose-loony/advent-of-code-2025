## 
def process_range(start: int, end: int):
    print("-----------")
    print(f'Start: {int(start)}, End: {int(end)}')

    start_length = len(str(start))
    end_length = len(str(end))
    size_dif = end_length - start_length
    print(f'Size Difference: {size_dif}')
    print(f'Numeric Difference: {end - start}')

    new_start = get_first_half(start)
    new_end = get_first_half(end)

    print(f'New start: {new_start}')
    print(f'New end: {new_end}')


    
    
def is_odd_length(num: int):
    return len(str(num)) % 2 != 0

# convert to string
# get first half of string, taking larger portion if odd length e.g. "12345" -> "123"
def get_first_half(s: int) -> int:
    str_s = str(s)
    n = len(str_s)

    mid = (n + 1) // 2
    return int(str_s[0:mid])

def halfsize(num: int):
    num_to_str = str(num)
    length = len(num_to_str)
    print(f'Half the size of {num} is {num_to_str[0:int(length/2)]}')

def test():
    # process_range(1, 22)
    halfsize(1)
    halfsize(12)
    halfsize(123)
    halfsize(1234)
    halfsize(12345)

def execute(content: str):
    ranges = content.split(",")
    for r in ranges:
        (start, end) = map(int, r.split("-"))
        process_range(start, end)


def main():
    with open("inputs/d2.txt", "r") as file:
        content = file.read()
    # test()
    execute(content)


if __name__ == "__main__":
    main()
