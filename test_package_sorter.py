import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    
    def test_standard_packages(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        self.assertEqual(sort(99, 99, 99, 15), "STANDARD")
    
    def test_bulky_packages(self):
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 150, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        self.assertEqual(sort(149, 149, 149, 19), "SPECIAL")
    
    def test_heavy_packages(self):
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        self.assertEqual(sort(99, 99, 99, 30), "SPECIAL")
    
    def test_rejected_packages(self):
        self.assertEqual(sort(150, 50, 50, 20), "REJECTED")
        self.assertEqual(sort(50, 150, 50, 25), "REJECTED")
        self.assertEqual(sort(50, 50, 150, 30), "REJECTED")
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
    
    def test_edge_cases(self):
        self.assertEqual(sort(149, 149, 149, 19), "SPECIAL")
        self.assertEqual(sort(150, 149, 149, 19), "SPECIAL")
        self.assertEqual(sort(149, 150, 149, 19), "SPECIAL")
        self.assertEqual(sort(149, 149, 150, 19), "SPECIAL")
        self.assertEqual(sort(149, 149, 149, 20), "REJECTED")
        self.assertEqual(sort(150, 149, 149, 20), "REJECTED")
        self.assertEqual(sort(149, 150, 149, 20), "REJECTED")
        self.assertEqual(sort(149, 149, 150, 20), "REJECTED")
    
    def test_volume_edge_cases(self):
        self.assertEqual(sort(100, 100, 99, 19), "STANDARD")
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")

if __name__ == '__main__':
    unittest.main() 