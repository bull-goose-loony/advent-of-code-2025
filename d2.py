def process_range(start: int, end: int):
    result_set: set[int] = set()
    print("-----------")
    print(f'Start: {int(start)}, End: {int(end)}')

    start_length = len(str(start))
    end_length = len(str(end))
    size_dif = end_length - start_length
    print(f'Size Difference: {size_dif}')

    for i in range(start, end + 1):
        if check_series(i):
            result_set.add(i)
    return result_set
            
def check_series(num: int):
    first_half = split_num(num)

    num_length = len(str(num))
    if num_length < 2:
        return False
    for i in range(1, len(first_half) + 1):
        substr = first_half[:i]
        if repeat(substr, num_length) == num:
            return True
    return False

def repeat(s: str, length: int):
    n = s
    while len(n) < length:
        n += s
    return int(n)
    
# get first half of string, taking larger portion if odd length e.g. "12345" -> "123"
def split_num(s: int) -> str:
    str_s = str(s)
    n = len(str_s)
    mid = (n + 1) // 2
    return  str_s[:mid]

def execute(content: str):
    ranges = content.split(",")
    total_sum = 0
    for r in ranges:
        (start, end) = map(int, r.split("-"))
        result_set = process_range(start, end)
        total_sum += sum(result_set)

    print(f'Total sum is: {total_sum}')

def main():
    with open("inputs/d2.txt", "r") as file:
        content = file.read()
    # test()
    execute(content)

def test():
    x = 121212
    print(f'{x} is a series: {check_series(x)}')

    x = 123123
    print(f'{x} is a series: {check_series(x)}')

    x = 121212
    print(f'{x} is a series: {check_series(x)}')

    x = 111111
    print(f'{x} is a series: {check_series(x)}')

    x = 111
    print(f'{x} is a series: {check_series(x)}')

    x = 123
    print(f'{x} is a series: {check_series(x)}')

    x = 12312
    print(f'{x} is a series: {check_series(x)}')

    x = 1231231
    print(f'{x} is a series: {check_series(x)}')

    print(process_range(1, 25))

    print(process_range(11, 22))
    print(process_range(95, 115))
    print(process_range(998, 1012))
    print(process_range(1188511880, 1188511890))
    print(process_range(222220, 222224))
    print(process_range(1698522, 1698528))
    print(process_range(446443, 446449))
    print(process_range(38593856, 38593862))
    print(process_range(565653, 565659))
    print(process_range(824824821, 824824827))
    print(process_range(2121212118, 2121212124))

if __name__ == "__main__":
    main()

