def prefix_function(s: str) -> list[int]:
    n = len(s)
    p = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p


def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        s = f.readline().strip()

    pi = prefix_function(s)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, pi)))

    return pi


if __name__ == "__main__":
    main()

