def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        N = int(f.readline())
        prices = []
        for _ in range(7):
            prices.append(int(f.readline()))

    sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]

    best = [0] * 7
    best[0] = prices[0]
    for i in range(1, 7):
        best[i] = min(prices[i], best[i - 1] * 10)
    r = N
    cost_exact = 0
    for i in range(6, -1, -1):
        if r >= sizes[i]:
            amount = r // sizes[i]
            cost_exact += amount * best[i]
            r -= amount * sizes[i]

    bigger_candidates = [prices[i] for i in range(7) if sizes[i] >= N]
    if bigger_candidates:
        cost_single = min(bigger_candidates)
        answer = min(cost_exact, cost_single)
    else:
        answer = cost_exact

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(answer))

    return answer


if __name__ == "__main__":
    main()
