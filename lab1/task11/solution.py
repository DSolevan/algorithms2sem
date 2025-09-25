def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        W, n = map(int, f.readline().split())
        weights = list(map(int, f.readline().split()))

    weights = [w for w in weights if w <= W]

    sums = {0}
    for w in weights:
        new_sums = {s + w for s in sums if s + w <= W}
        sums.update(new_sums)

    ans = max(sums)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(ans))

    return ans

if __name__ == "__main__":
    main()

