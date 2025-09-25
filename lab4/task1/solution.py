def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        pattern = f.readline().rstrip("\n")
        text = f.readline().rstrip("\n")

    n = len(pattern)
    m = len(text)
    positions = []


    for i in range(m - n + 1):
        if text.startswith(pattern, i):
            positions.append(str(i + 1))  # индексация с 1

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(len(positions)) + "\n")
        if positions:
            f.write(" ".join(positions))

    return positions


if __name__ == "__main__":
    main()
