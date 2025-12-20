def process_range(start: str, end: str):
    # print(f'Start: {int(start)}, End: {int(end)}')
    


def main():
    with open("inputs/d2.txt", "r") as file:
        content = file.read()
        ranges = content.split(",")

    for r in ranges:
        (start, end) = r.split("-")
        process_range(start, end)

if __name__ == "__main__":
    main()
