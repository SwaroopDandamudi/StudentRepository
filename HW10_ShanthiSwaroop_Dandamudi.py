""" The program has four classes where 3 classes are intialization classes for
    the data provided in 3 different files. The university class reads all the
    files and updates the values in students, majors, instructors and prints
    the summary tables of students, majors and instructors using pretty tables
    We import file_reader method from the HW08 to read the files
"""
from prettytable import PrettyTable
from collections import defaultdict
from HW08_ShanthiSwaroop_Dandamudi import file_reader
import os


class Student:
    """
        Need to know:
        -CWID
        -name
        -major
        -courses
    """
    def __init__(self, cwid: int, name: str, major: str) -> None:
        self.cwid = cwid
        self.name = name
        self.major = major
        self.courses = dict()

    def add_course(self, course: str, grade: str) -> None:
        if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
            self.courses[course] = grade
        elif grade == 'F':
            print(f"The student with CWID {self.cwid} has failed the course")
        else:
            print(f"The student with CWID {self.cwid} has no grade in record")


class Major:
    """Contains all the information about the Majors being offered, reqired and
       elective courses"""
    def __init__(self, dept, r_e, course) -> None:
        self.dept = dept
        self.required = set()
        self.elective = set()


class Instructor:
    """Contains all the information about the Instructor"""
    def __init__(self, cwid, name, dept) -> None:
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.courses = defaultdict(int)

    def get_student_no(self, course) -> None:
        self.courses[course] += 1


class University:
    """Contains data extracted files and creates pretty tables"""
    def __init__(self, directory: str) -> None:
        self. directory: str = directory
        self.students: Dict[str, str, str] = dict()
        self.instructors: Dict[str, str, str] = dict()
        self.majors: Dict[str, str, str] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        try:
            files = os. listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError("Directory not found")
            # Raise filenotfound error if the directory doesnt exist
        else:
            for file in files:
                if file.endswith(".txt"):
                    if file == "students.txt":
                        try:
                            for cwid, name, major in (
                                file_reader(os.path.join(self.directory, file),
                                            3, ';', True)):
                                self.students[cwid] = Student(cwid, name,
                                                              major)
                        except Exception:
                            print("There was an error trying to get student\
                                  details. Please check number of fields")
                    elif file == "instructors.txt":
                        try:
                            for cwid, name, dept in (
                                file_reader(os.path.join(self.directory, file),
                                            3, '|', True)):
                                self.instructors[cwid] = Instructor(cwid, name,
                                                                    dept)
                        except Exception:
                            print("There was an error trying to get instructor\
                                  details. Please check number of fields")
                    elif file == "grades.txt":
                        try:
                            a = (file_reader(os.path.join(self.directory,
                                                          file), 4, '|', True))
                        except Exception as e:
                            print(f"exception {e} has occured")
                    elif file == "majors.txt":
                        try:
                            for dept, r_e, course in (
                                file_reader(os.path.join(self.directory, file),
                                            3, '\t', True)):
                                if dept not in self.majors.keys():
                                    self.majors[dept] = Major(dept, r_e,
                                                              course)
                                if r_e.lower() == 'r':
                                    self.majors[dept].required.add(course)
                                elif r_e.lower() == 'e':
                                    self.majors[dept].elective.add(course)
                        except Exception:
                            print("There was an error trying to get major\
                                  details. Please check number of fields")

        for cwid, course, grade, instructor_cwid in a:
            if cwid in self.students.keys():
                self.students[cwid].add_course(course, grade)
            else:
                print(f"didnt find student {cwid} whose grade was mentioned")
            if instructor_cwid in self.instructors.keys():
                self.instructors[instructor_cwid].get_student_no(course)
            else:
                print(f"didnt find prof with cwid={cwid} whose course was\
                      mentioned")

    def pretty_print(self) -> None:
        """ This method tabulates the pretty table with the values
            from dictionary we created above"""
        pretty_table_student = PrettyTable(field_names=["CWID", "Name",
                                                        "Major",
                                                        "Completed Courses",
                                                        "Remaining Required",
                                                        "Remaining Electives"])
        pretty_table_instructor = PrettyTable(field_names=["CWID", "Name",
                                                           "Dept", "Course",
                                                           "Students"])
        pretty_table_majors = PrettyTable(field_names=["Major",
                                                       "Required Courses",
                                                       "Electives"])
        pretty_table_student.title = "Student Summary"
        pretty_table_instructor.title = "Instructor Summary"
        pretty_table_majors.title = "Majors Summary"
        for i in self.students.values():
            try:
                a = len((self.majors[i.major].elective)) -\
                    len(self.majors[i.major].elective-i.courses.keys())
                pretty_table_student.add_row([i.cwid, i.name, i.major,
                                              sorted(i.courses.keys()),
                                              sorted(
                                                  self.majors[i.major].required
                                                  - i.courses.keys()),
                                              [] if a > 0 else
                                              sorted(
                                                  self.majors[i.major].elective
                                                  - i.courses.keys())])
            except Exception as e:
                print(f"There was an error. Please check datafield with {e}")
        for j in self.majors.values():
            pretty_table_majors.add_row([j.dept, sorted(j.required),
                                        sorted(j.elective)])
        for k in self.instructors.values():
            for cour in k.courses:
                pretty_table_instructor.add_row([k.cwid, k.name, k.dept, cour,
                                                 k.courses[cour]])
        print(pretty_table_majors, pretty_table_student,
              pretty_table_instructor)
