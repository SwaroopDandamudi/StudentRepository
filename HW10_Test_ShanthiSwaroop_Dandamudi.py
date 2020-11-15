""" Test cases for student, major, instructor classes to check if the values
    are populated correctly
"""
import unittest
from HW10_ShanthiSwaroop_Dandamudi import Student, Instructor, Major,\
                                          University


class StudentTest(unittest.TestCase):
    """ Class test for Student"""
    def test_student(self):
        student = Student("10452424", "Swaroop", "ComputerScience")
        self.assertEqual(student.name, "Swaroop")
        self.assertEqual(student.cwid, "10452424")
        self.assertEqual(student.major, "ComputerScience")


class InstructorTest(unittest.TestCase):
    """ Class test for Instructor"""
    def test_instructor(self):
        instructor = Instructor("10452424", "Swaroop", "ComputerScience")
        self.assertEqual(instructor.name, "Swaroop")
        self.assertEqual(instructor.cwid, "10452424")
        self.assertEqual(instructor.dept, "ComputerScience")


class MajorTest(unittest.TestCase):
    """ Class test for Major"""
    def test_major(self):
        major = Major("ComputerScience", "R", "CS513")
        self.assertEqual(major.dept, "ComputerScience")


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
