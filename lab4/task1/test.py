import os
import unittest
import tempfile
from solution import main

class TestFindSubstringStartwith(unittest.TestCase):
    def run_case(self, input_text: str, expected_text: str):
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "input.txt")
            out_path = os.path.join(tmp, "output.txt")
            with open(in_path, "w", encoding="utf-8") as f:
                f.write(input_text)
            main(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                got = f.read().strip()
            self.assertEqual(got, expected_text.strip())

    def test_sample(self):
        self.run_case(
            "aba\nabaCaba\n",
            "2\n1 5"
        )

    def test_overlapping(self):
        # "aa" в "aaaa" -> позиции 1,2,3
        self.run_case(
            "aa\naaaa\n",
            "3\n1 2 3"
        )

    def test_no_match(self):
        self.run_case(
            "xyz\nabcabc\n",
            "0"
        )

    def test_full_match(self):
        self.run_case(
            "hello\nhello\n",
            "1\n1"
        )

if __name__ == "__main__":
    unittest.main()
