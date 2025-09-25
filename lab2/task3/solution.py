class Node:
    __slots__ = ("value", "left", "right")
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def bst_insert(root: Node | None, x: int) -> Node:
    if root is None:
        return Node(x)
    cur = root
    while True:
        if x < cur.value:
            if cur.left is None:
                cur.left = Node(x)
                break
            cur = cur.left
        elif x > cur.value:
            if cur.right is None:
                cur.right = Node(x)
                break
            cur = cur.right
        else:
            break
    return root


def bst_successor(root: Node | None, x: int) -> int:
    ans = 0
    cur = root
    while cur is not None:
        if x < cur.value:
            ans = cur.value
            cur = cur.left
        else:
            cur = cur.right
    return ans


def main(input_path: str = "input.txt", output_path: str = "output.txt"):
    root = None
    out_lines: list[str] = []

    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            op, val = line.split()
            x = int(val)
            if op == '+':
                root = bst_insert(root, x)
            elif op == '>':
                out_lines.append(str(bst_successor(root, x)))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))

    return out_lines

if __name__ == "__main__":
    main()

