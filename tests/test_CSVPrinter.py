import sys
sys.path.append("../SpecialLecture")

import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read1(self):
        printer = CSVPrinter("tests/sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter("tests/sample.csv")
        lines = printer.read()
        print(lines)
        self.assertEqual("value2B", lines[1][1])
    
    def test_read3(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("tests/nosample.csv")
            printer.read()
            