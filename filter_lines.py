def filter_lines(input_file: str, keyword: str, output_file: str = "filtered.txt") -> None:
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    filtered = [
        line for line in lines if keyword in line
    ]

    with open(output_file, "w", encoding="utf-8") as out:
        out.writelines(filtered)


if __name__ == "__main__":
    filter_lines("input.txt", "apple")
