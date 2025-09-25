def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        n = int(f.readline())
        if n == 0:
            height = 0
        else:
            nodes = [None] * (n + 1)
            for i in range(1, n + 1):
                k, l, r = map(int, f.readline().split())
                nodes[i] = (l, r)

            stack = [(1, 1)]
            height = 0
            while stack:
                v, d = stack.pop()
                if d > height:
                    height = d
                left, right = nodes[v]
                if left != 0:
                    stack.append((left, d + 1))
                if right != 0:
                    stack.append((right, d + 1))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(height))

    return height


if __name__ == "__main__":
    main()
