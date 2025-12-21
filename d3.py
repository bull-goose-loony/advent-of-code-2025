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
        largest_bat = process_bank(bank.strip())
        total_sum += largest_bat
    print(f"Result: {total_sum}")


def test():
    process_bank("1234")
    process_bank("4321")
    process_bank("987654321111111")
    process_bank("811111111111119")
    process_bank("234234234234278")
    process_bank("818181911112111")
    process_bank("3422625438535318655835453462742236454559673365563575346236243542284435538452836574856662875273434662")

def main():
    with open("inputs/d3.txt", "r") as file:
        banks = file.readlines()
    execute(banks)
    # test()
    # 16287 is too low
    # 16924 didn't work either.

if __name__ == "__main__":
    main()
