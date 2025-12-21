def process_bank(bank):
    ##TODO find the maximum 
    print(max(bank))
    ## gotcha, if the highest number is at the end, it can't be the first battery

def execute(banks):
    for bank in banks:
        process_bank(bank)

def test():
    print("hi")

def main():
    with open("inputs/d3.txt", "r") as file:
        banks = file.readlines()
    execute(banks)

if __name__ == "__main__":
    main()
