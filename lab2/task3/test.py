import os
import unittest
import tempfile
from solution import main

class TestBSTSuccessor(unittest.TestCase):
    def run_case(self, input_text: str, expected_output: str):
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "input.txt")
            out_path = os.path.join(tmp, "output.txt")
            with open(in_path, "w", encoding="utf-8") as f:
                f.write(input_text)
            main(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                got = f.read().strip()
            self.assertEqual(got, expected_output)

    def test_sample(self):
        self.run_case(
            "+ 1\n+ 3\n+ 3\n+ 0\n> 1\n> 2\n> 3\n+ 3\n> 1\n",
            "3\n3\n0\n3"
        )

    def test_duplicates_ignored(self):
        self.run_case(
            "+ 5\n+ 5\n+ 5\n> 4\n> 5\n> 6\n",
            "5\n0\n0"
        )

    def test_increasing_chain(self):
        ops = []
        for x in range(1, 2000):
            ops.append(f"+ {x}")
        ops += ["> 0", "> 1500", "> 1999", "> 2000"]
        expected = "\n".join(["1", "1501", "0", "0"])
        self.run_case("\n".join(ops) + "\n", expected)

if __name__ == "__main__":
    unittest.main()

