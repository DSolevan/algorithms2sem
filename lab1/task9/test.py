import os
import unittest
import tempfile
from solution import main

class TestPrintCosts(unittest.TestCase):
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
            "980\n1\n9\n90\n900\n1000\n10000\n10000\n",
            "882"
        )

    def test_sample_2(self):
        self.run_case(
            "980\n1\n10\n100\n1000\n900\n10000\n10000\n",
            "900"
        )

    def test_n_equals_1_allows_big_pack(self):
        self.run_case(
            "1\n50\n60\n70\n80\n90\n100\n40\n",
            "40"
        )

    def test_overbuy_single_pack_beats_exact(self):
        self.run_case(
            "20\n10\n500\n150\n100000\n100000\n100000\n100000\n",
            "150"
        )

if __name__ == "__main__":
    unittest.main()
