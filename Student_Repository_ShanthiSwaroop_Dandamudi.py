""" Program which has function which returns 3 days after Feb 27 in 2019, 2020
    and Number of days between Sep30,2019 and Feb 01,2019.
    It also contains a function which reads the file in given location if it
    exists and returns the contents of the file in a tuple based on the
    delimiter
    Program contains a class which reads all the files with .py extension in the
    given directory and returns the number of classes,functions,lines and
    characters in each file if those exists.
    The class also makes a pretty table from the above details
"""
from typing import Iterator, List, Tuple
from prettytable import PrettyTable
import datetime
import os

def date_arithmetic()-> [datetime, datetime, int]:
    """ Function that gives the date after three days for february in both leap
        year,non - leap year and number of days difference between two dates """
    three_days_after_02272020: datetime = (
                                            datetime.datetime.strptime("Feb 27, 2020","%b %d, %Y"))\
                                            + (datetime.timedelta(days=3)
                                            )
    three_days_after_02272019: datetime = (
                                            datetime.datetime.strptime("Feb 27, 2019","%b %d, %Y"))\
                                            + (datetime.timedelta(days=3)
                                            )
    days_passed_02012019_09302019: int = (
                                            ((datetime.datetime.strptime("Sep 30, 2019","%b %d, %Y"))\
                                            - (datetime.datetime.strptime("Feb 01, 2019","%b %d, %Y"))).days
                                            )
    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019

def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[Tuple[str]]:
    """ Function which returns the contents of the file in a tuple """
    try:
        fp:IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} doesnt exist") #Raise filenotfound error if the file doesnt exist
    else:
        a = list()
        with fp:
            if header:
                next(fp)
            for linenumber, line in enumerate(fp):
                b = line.strip().split(sep)
                if len(b) != fields:
                    raise ValueError(
                                        f"{path[(path.rfind('/'))+1:]} has {len(b)} fields on line\
                                        {linenumber+1} but expected {fields} "
                                        )
                a.append(line.strip().split(sep))
    return a

class FileAnalyzer:
    """ class which returns the number of classes, functions, characters, lines
        in a python file in a directory and make a pretty table with the details
    """
    def __init__(self,directory : str) -> None:
        self. directory: str = directory
        self. files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """ This method opens the file if it exists and returns the content of 
            the file into a dictionary """
        try:
            files = os. listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError("Directory not found") #Raise filenotfound error if the directory doesnt exist
        else:
            for file in files:
                if file.endswith(".py"):
                    try:
                        fp = open(os.path.join(self.directory, file), "r")
                    except FileNotFoundError:      #Raise filenotfound error if file doent have permissions
                        raise FileNotFoundError("Specified file cannot be opened for reading")
                    else:
                        with fp:
                            classes_num, functions_num, lines_num, characters_num = 0,0,0,0
                            filename_0 = file
                            for line in fp:
                                line  = line.strip()
                                lines_num += 1
                                characters_num += len(line)
                                if line.startswith("def") and line.endswith(":"):
                                    functions_num += 1
                                elif line.startswith("class") and line.endswith(":"):
                                    classes_num += 1
                        self.files_summary[filename_0] = {
                                                            "class" : classes_num,
                                                            "function" : functions_num,
                                                            "line" : lines_num,
                                                            "char" : characters_num
                                                            }
        return self.files_summary

    def pretty_print(self) -> None:
        """ This method tabulates the pretty table with the values 
            from dictionary """
        pretty_table = PrettyTable(field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"])
        for file_name in self.files_summary:
            pretty_table.add_row(
                                    [file_name,
                                    self.files_summary[file_name]["class"],
                                    self.files_summary[file_name]["function"],
                                    self.files_summary[file_name]["line"],
                                    self.files_summary[file_name]["char"]]
                                    )
        return pretty_table

if __name__ == "__main__":
    print(file_reader("C:/Users/shant/Documents/GitHub/StudentRepository/students.txt",3,';',True))
    print(file_reader("C:/Users/shant/Documents/GitHub/StudentRepository/instructors.txt",3,'|',True))
    print(file_reader("C:/Users/shant/Documents/GitHub/StudentRepository/grades.txt",4,'|',True))
    print(file_reader("C:/Users/shant/Documents/GitHub/StudentRepository/majors.txt",3,'\t',True))