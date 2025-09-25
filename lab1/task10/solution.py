def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        N, S = map(int, f.readline().split())
        apples = []
        for i in range(1, N + 1):
            a, b = map(int, f.readline().split())
            apples.append((a, b, i))

    afford = [x for x in apples if x[1] >= x[0]]
    withdraw = [x for x in apples if x[1] < x[0]]

    afford.sort(key=lambda x: (x[0], -x[1]))
    withdraw.sort(key=lambda x: x[1], reverse=True)

    answer = []
    ok = True

    # Съедаем "неубыточные"
    for a, b, i in afford:
        if S <= a:
            ok = False
            break
        S = S - a + b
        answer.append(str(i))

    # Съедаем "убыточные"
    if ok:
        for a, b, i in withdraw:
            if S <= a:
                ok = False
                break
            S = S - a + b
            answer.append(str(i))

    with open(output_path, "w", encoding="utf-8") as f:
        if not ok or len(answer) != N:
            f.write("-1")
        else:
            f.write(" ".join(answer))

    return ok, answer

if __name__ == "__main__":
    main()

    
