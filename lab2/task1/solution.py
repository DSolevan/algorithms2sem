from typing import List

def inorder(root: int, keys: List[int], left: List[int], right: List[int]) -> List[int]:
    result = []
    stack = []
    current = root
    while stack or current != -1:
        while current != -1:
            stack.append(current)
            current = left[current]
        current = stack.pop()
        result.append(keys[current])
        current = right[current]
    return result


def preorder(root: int, keys: List[int], left: List[int], right: List[int]) -> List[int]:
    result = []
    stack = [root]
    while stack:
        v = stack.pop()
        result.append(keys[v])
        r = right[v]
        l = left[v]
        if r != -1:
            stack.append(r)
        if l != -1:
            stack.append(l)
    return result


def postorder(root: int, keys: List[int], left: List[int], right: List[int]) -> List[int]:
    result = []
    s1 = [root]
    s2 = []
    while s1:
        v = s1.pop()
        s2.append(v)
        if left[v] != -1:
            s1.append(left[v])
        if right[v] != -1:
            s1.append(right[v])
    while s2:
        result.append(keys[s2.pop()])
    return result


def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        N = int(f.readline())
        data = f.read().split()

    idx = 0
    keys, left, right = [0] * N, [0] * N, [0] * N
    for i in range(N):
        keys[i] = int(data[idx])
        left[i] = int(data[idx + 1])
        right[i] = int(data[idx + 2])
        idx += 3

    root = 0
    tree_in = inorder(root, keys, left, right)
    tree_pre = preorder(root, keys, left, right)
    tree_post = postorder(root, keys, left, right)

    ans_lines = [
        " ".join(map(str, tree_in)),
        " ".join(map(str, tree_pre)),
        " ".join(map(str, tree_post)),
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        for line in ans_lines:
            f.write(line + "\n")

    return ans_lines


if __name__ == "__main__":
    main()

