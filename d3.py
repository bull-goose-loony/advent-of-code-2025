# Input: a string of numbers
# Output: the maximum 12 digit number selected from string 
def process_bank_2(bank: str) -> int: 
    bank_length = len(bank)
    print(f'processing bank: {bank}')
    result_str = ''
    start_idx = 0
    end_idx = bank_length - 12

    for i in range(12):
        max_idx = select_max(bank, start_idx, end_idx)
        result_str += bank[max_idx]
        start_idx = max_idx + 1
        end_idx += 1

    result = int(result_str)
    # print(f'Result: {result}')
    return result

# Take a bank str, start_idx, end_idx, return the index of the largest
# number within that range
def select_max(bank: str, start_idx: int, end_idx: int) -> int:
    index = -1
    max = 0
    # print(f'selecting from range {bank[start_idx:end_idx + 1]}')
    for i in range(start_idx, end_idx + 1):
        if int(bank[i]) > max:
            index = i
            max = int(bank[i])
    # print(f'Selected {max} at index {index}')
    return index

    

def process_bank(bank: str):
    ##TODO find the maximum 
    ## gotcha, if the highest number is at the end, it can't be the first battery
    largest_digit_index = get_largest_digit_index(bank)
    largest_digit = bank[largest_digit_index]

    print(f'----------------------------------')
    print(f'Largetst Digit: {largest_digit}')
    print(f'Index: {largest_digit_index}')
    print(f'length of bank: {len(bank)}')

    battery1 = ''
    battery2 = ''
    if largest_digit_index == len(bank) - 1:
        # Need the largest digit that's not at the end
        battery2 = largest_digit
        sub_bank = bank[0:largest_digit_index] 
        battery1 = max(sub_bank)
    else:
        battery1 = largest_digit
        sub_bank = bank[largest_digit_index + 1:]
        battery2 = max(sub_bank)


    solution = int(battery1 + battery2)

    print(f'Bank = {bank}')
    print(f'Selected: first:{battery1}, second:{battery2}')

    return(solution)

def get_largest_digit_index(bank: str):
    index = 0
    max = 0
    for i in range(len(bank)):
        # print(f"i = {i}, bank[i] = {bank[i]}")
        numeric = int(bank[i])
        if numeric > max:
            max = numeric
            index = i
    return(index)

def execute(banks):
    total_sum = 0
    for bank in banks:
        largest_bat = process_bank_2(bank.strip())
        total_sum += largest_bat
    print(f"Result: {total_sum}")


def test():
    # length = 12
    process_bank_2("987654321111111")
    process_bank_2("811111111111119")
    process_bank_2("234234234234278")

def main():
    with open("inputs/d3.txt", "r") as file:
        banks = file.readlines()
    execute(banks)
    # test()

if __name__ == "__main__":
    main()
