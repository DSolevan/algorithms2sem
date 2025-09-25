import os
import unittest
import tempfile
from solution import main

class TestPathExists(unittest.TestCase):
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
            "4 4\n1 2\n3 2\n4 3\n1 4\n1 4\n",
            "1"
        )

    def test_sample_2(self):
        self.run_case(
            "4 2\n1 2\n3 2\n1 4\n",
            "0"
        )

    def test_single_edge(self):
        self.run_case(
            "2 1\n1 2\n1 2\n",
            "1"
        )

    def test_disconnected(self):
        self.run_case(
            "5 2\n1 2\n4 5\n1 5\n",
            "0"
        )

if __name__ == "__main__":
    unittest.main()
