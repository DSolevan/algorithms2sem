import os
import unittest
import tempfile
from solution import main

class TestTraversals(unittest.TestCase):
    def run_case(self, input_text: str, expected_lines: list[str]):
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "input.txt")
            out_path = os.path.join(tmp, "output.txt")
            with open(in_path, "w", encoding="utf-8") as f:
                f.write(input_text)
            main(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                got_lines = [line.rstrip("\n") for line in f.readlines()]
            self.assertEqual(got_lines, expected_lines)

    def test_single_node(self):
        self.run_case(
            "1\n42 -1 -1\n",
            ["42", "42", "42"],
        )

    def test_small_tree(self):
        self.run_case(
            "5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1\n",
            ["1 2 3 4 5", "4 2 1 3 5", "1 3 2 5 4"],
        )

    def test_right_chain(self):
        self.run_case(
            "4\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 -1\n",
            ["1 2 3 4", "1 2 3 4", "4 3 2 1"],
        )

if __name__ == "__main__":
    unittest.main()


