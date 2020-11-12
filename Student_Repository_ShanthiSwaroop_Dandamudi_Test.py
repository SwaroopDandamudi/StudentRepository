""" Name - Shanthi Swaroop Dandamudi
    CWID - 10452424
    Test cases to validate function that gives the date after three days for
    february in both leap year, non - leap year and number of days difference
    between two dates
    Testcases to validate a function which returns the contents of the file in
    a tuple
    Test cases to check a class which returns the number of classes, functions,
    characters,lines in a python file in a directory
"""
import unittest
import datetime
from Student_Repository_ShanthiSwaroop_Dandamudi import date_arithmetic, file_reader, FileAnalyzer

class DateArithmeticTest(unittest.TestCase):
    def test_date_arithmetic(self):
        """ test cases for date arithmetic """
        self.assertTupleEqual(
                                date_arithmetic(),
                                (datetime.datetime(2020, 3, 1, 0, 0),
                                datetime.datetime(2019, 3, 2, 0, 0), 241)
                                )
        self.assertNotEqual(
                                date_arithmetic(),
                                (datetime.datetime(2020, 4, 1, 0, 0),
                                datetime.datetime(2019, 3, 2, 0, 0), 303)
                                )
        self.assertNotEqual(date_arithmetic(), '')

class FileReaderTest(unittest.TestCase):
    def test_file_reader(self):
        """ test cases for file reader """
        self.assertEqual(
                            file_reader('C:/Users/shant/Desktop/Assignment/student_majors.txt',3,'|',True),
                            [['123', 'Jin He', 'Computer Science'],
                            ['234', 'Nanda Koka', 'Software Engineering'],
                            ['345', 'Benji Cai', 'Software Engineering']]
                            )
        self.assertNotEqual(
                                file_reader('C:/Users/shant/Desktop/Assignment/student_majors.txt',3,'|',False),
                                [['123', 'Jin He', 'Computer Science'],
                                ['234', 'Nanda Koka', 'Software Engineering'],
                                ['345', 'Benji Cai', 'Software Engineering']]
                                )
        with self.assertRaises(FileNotFoundError):
            file_reader('C:/Users/shant/Desktop/Assignment/student_majors_dummys.txt',3,'|',True)
        with self.assertRaises(ValueError):
            file_reader('C:/Users/shant/Desktop/Assignment/student_majors.txt',4,'|',True)

class FileAnalyzerTest(unittest.TestCase):
    def test_file_analyzer(self):
        """Test cases for file analyser"""
        file_analyzer = FileAnalyzer("C:/Users/shant/Downloads/test")
        self.assertEqual(
                            {'0_defs_in_this_file.py': {'class': 0, 'function': 0, 'line': 3, 'char': 53},
                            'file1.py': {'class': 2, 'function': 4, 'line': 25, 'char': 200},
                            'new.py':{'class': 1, 'function': 1, 'line': 3, 'char': 38}},
                            file_analyzer.files_summary
                            )
        with self.assertRaises(FileNotFoundError):
            file_analyzer = FileAnalyzer("C:/Users/shant/Downloads/teast")

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)