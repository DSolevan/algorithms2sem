import os
import unittest
import tempfile
from solution import main

class TestGold(unittest.TestCase):
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
        self.run_case("10 3\n1 4 8\n", "9")

    def test_exact_fit(self):
        self.run_case("15 4\n7 3 5 9\n", "15")

    def test_all_too_heavy(self):
        self.run_case("5 3\n6 7 8\n", "0")

    def test_zeros(self):
        self.run_case("5 5\n0 0 5 0 0\n", "5")

    def test_many_small(self):
        self.run_case("12 6\n2 2 3 3 5 9\n", "12")

if __name__ == "__main__":
    unittest.main()


