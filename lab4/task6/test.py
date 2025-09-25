import os
import unittest
import tempfile
from solution import main

class TestZFunction(unittest.TestCase):
    def run_case(self, s: str, expected: str):
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "input.txt")
            out_path = os.path.join(tmp, "output.txt")
            with open(in_path, "w", encoding="utf-8") as f:
                f.write(s + "\n")
            main(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                got = f.read().strip()
            self.assertEqual(got, expected)

    def test_sample1(self):
        self.run_case("aaaAAA", "2 1 0 0 0")

    def test_sample2(self):
        self.run_case("abacaba", "0 1 0 3 0 1")

    def test_all_equal(self):
        self.run_case("aaaaa", "4 3 2 1")

    def test_no_match(self):
        self.run_case("abcde", "0 0 0 0")

if __name__ == "__main__":
    unittest.main()
