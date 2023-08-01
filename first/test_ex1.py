import unittest
from Ex1 import deduplicate, deduplicate_new

class TestDeduplicate(unittest.TestCase):
    def test_deduplicate(self):
        input = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d",1]
        duplicated = deduplicate(input)
        expected_duplicated =["a", "c", "d"]
        self.assertEqual(duplicated, expected_duplicated)
    def test_deduplicate_new(self):
        input = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d",1]
        duplicated = deduplicate_new(input)
        expected_duplicated =["a", "c", "d"]
        self.assertEqual(duplicated, expected_duplicated)
        pass
    

if __name__ == "__main__":
    unittest.main()