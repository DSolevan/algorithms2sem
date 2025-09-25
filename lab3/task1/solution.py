from collections import deque

def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        n, m = map(int, f.readline().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, f.readline().split())
            adj[a].append(b)
            adj[b].append(a)
        u, v = map(int, f.readline().split())

    visited = [False] * (n + 1)
    q = deque([u])
    visited[u] = True
    while q:
        x = q.popleft()
        if x == v:
            break
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("1" if visited[v] else "0")

    return visited[v]


if __name__ == "__main__":
    main()
