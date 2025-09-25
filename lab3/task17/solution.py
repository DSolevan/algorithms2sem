def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        N, M = map(int, f.readline().split())

        INF = 10**9

        plan = [[INF] * N for _ in range(N)]
        for i in range(N):
            plan[i][i] = 0

        edges_dir = set()
        for _ in range(M):
            x, y = map(int, f.readline().split())
            x -= 1
            y -= 1
            edges_dir.add((x, y))
            plan[x][y] = 0

        for (x, y) in list(edges_dir):
            if plan[y][x] > 1:
                plan[y][x] = 1

        for k in range(N):
            pk = plan[k]
            for i in range(N):
                if plan[i][k] == INF:
                    continue
                pik = plan[i][k]
                pi = plan[i]
                for j in range(N):
                    v = pk[j]
                    if v == INF:
                        continue
                    s = pik + v
                    if pi[j] > s:
                        pi[j] = s
        answer = 0
        for row in plan:
            best = max(row)
            if best > answer:
                answer = best
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(answer))

    return answer
if __name__ == "__main__":
    main()
