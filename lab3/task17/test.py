import os
import unittest
import tempfile
from solution import main

class TestWeakKConnectivity(unittest.TestCase):
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

    def test_sample_1(self):
        self.run_case(
            "3 2\n1 2\n1 3\n",
            "1"
        )

    def test_sample_2(self):
        self.run_case(
            "4 4\n2 4\n4 2\n3 1\n4 3\n",
            "0"
        )

    def test_bidirectional_all(self):
        self.run_case(
            "3 6\n1 2\n2 1\n2 3\n3 2\n1 3\n3 1\n",
            "0"
        )

    def test_line_one_direction(self):
        self.run_case(
            "4 3\n1 2\n2 3\n3 4\n",
            "3"
        )

if __name__ == "__main__":
    unittest.main()
