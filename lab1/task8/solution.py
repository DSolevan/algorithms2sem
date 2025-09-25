def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        N = int(f.readline())
        lectures = [tuple(map(int, f.readline().split())) for _ in range(N)]

    lectures.sort(key=lambda x: x[1])

    count, last = 0, 0
    for start, end in lectures:
        if start >= last:
            count += 1
            last = end

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(count))

    return count


if __name__ == "__main__":
    main()
