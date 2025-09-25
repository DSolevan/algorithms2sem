import os
import unittest
import tempfile
from solution import main

class TestHeight(unittest.TestCase):
    def run_case(self, input_text: str, expected: str):
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "input.txt")
            out_path = os.path.join(tmp, "output.txt")
            with open(in_path, "w", encoding="utf-8") as f:
                f.write(input_text)
            main(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                got = f.read().strip()
            self.assertEqual(got, expected)

    def test_empty(self):
        self.run_case("0\n", "0")

    def test_example(self):
        self.run_case(
            "6\n-2 0 2\n8 4 3\n9 0 0\n0 3 5\n6 0 1\n0 0 0\n",
            "4"
        )

    def test_chain_left(self):
        self.run_case(
            "4\n1 2 0\n2 3 0\n3 4 0\n4 0 0\n",
            "4"
        )

    def test_balanced(self):
        self.run_case(
            "7\n10 2 3\n5 4 5\n15 6 7\n1 0 0\n7 0 0\n12 0 0\n20 0 0\n",
            "3"
        )

if __name__ == "__main__":
    unittest.main()
