import os
import unittest
import tempfile
from solution import main

class TestLectures(unittest.TestCase):
    def test_samples(self):
        cases = [
            ("1\n5 10\n", "1"),
            ("3\n1 5\n2 3\n3 4\n", "2"),
            ("3\n0 1\n1 2\n2 3\n", "3"),
        ]
        for input_text, expected_output in cases:
            with self.subTest(input=input_text):
                with tempfile.TemporaryDirectory() as tmp:
                    in_path = os.path.join(tmp, "input.txt")
                    out_path = os.path.join(tmp, "output.txt")

                    with open(in_path, "w", encoding="utf-8") as f:
                        f.write(input_text)

                    main(in_path, out_path)

                    with open(out_path, "r", encoding="utf-8") as f:
                        got = f.read().strip()

                    self.assertEqual(got, expected_output)

if __name__ == "__main__":
    unittest.main()
