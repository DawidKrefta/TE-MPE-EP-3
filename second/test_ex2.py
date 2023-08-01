import unittest
from Ex2 import make_graph

class TestDependencyGraph(unittest.TestCase):
    def test_make_graph(self):
        file_path = "C:\\Users\\dawid\\OneDrive\\Pulpit\\Dawid\\Stypendia\\CERN_2023\\TE-MPE-EP-3\\second\\deps.json"
        graph = make_graph(file_path)
        expected_graph = {
            "pkg1": ["pkg2", "pkg3"],
            "pkg2": ["pkg3"],
            "pkg3": []
        }
        self.assertEqual(graph, expected_graph)

if __name__ == "__main__":
    unittest.main()