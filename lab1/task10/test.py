import os
import unittest
import tempfile
from solution import main

class TestApples(unittest.TestCase):
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

    def test_sample_ok(self):
        self.run_case(
            "3 5\n2 3\n10 5\n5 10\n",
            "1 3 2"
        )

    def test_sample_impossible(self):
        self.run_case(
            "3 5\n2 3\n10 5\n5 6\n",
            "-1"
        )

    def test_trivial_one(self):
        self.run_case(
            "1 3\n3 100\n",
            "-1"
        )

    def test_simple_possible(self):
        self.run_case(
            "2 3\n1 1\n2 1\n",
            "1 2"
        )

if __name__ == "__main__":
    unittest.main()

