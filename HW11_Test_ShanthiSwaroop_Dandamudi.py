""" Test cases for student, major, instructor classes to check if the values
    are populated correctly
"""
import unittest
import sqlite3
from HW11_ShanthiSwaroop_Dandamudi import Student, Instructor, Major,\
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


class UniversityMajorTest(unittest.TestCase):
    "Class test for University.student_grades_table"
    def test_student_grades_Table_db(self) -> None:
        filename: str = "C:/Users/shant/Desktop/810_startup.db"
        u = University("C:/Users/shant/Desktop/Assignment")
        u.student_grades_table_db(filename)
        db: sqlite3.Connection = sqlite3.connect(filename)
        output = [('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                  ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
                  ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
                  ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                  ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                  ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                  ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                  ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                  ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]
        expected = []
        for row in db.execute("select s.Name as Name, s.CWID as CWID,\
                              g.Course as Course, g.Grade as Grade,\
                              i.Name as Name from students s join grades g\
                              on s.CWID = g.StudentCWID join instructors i\
                              on g.InstructorCWID = i.CWID order by s.Name"):
            expected.append(row)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
