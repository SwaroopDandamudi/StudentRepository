""" The program illustrates how we can create a table and load data into the
    table on a new webpage using Flask, templates, Jinja2 variables and sqlite3
"""
from flask import Flask, render_template
from typing import Dict
import sqlite3


app: Flask = Flask(__name__)


@app.route('/Hello')
def hello() -> str:
    """ Static Method """
    return "Hello world! This is Flask!"


@app.route('/pretty')
def student_summary_grades() -> str:
    """ This function gets the data from db and then uploads that data onto
        website based on the template specified
    """
    query = """select s.CWID as CWID, s.Name as Name,\
               g.Course as Course, g.Grade as Grade,\
               i.Name as IName from students s join grades g\
               on s.CWID = g.StudentCWID join instructors i\
               on g.InstructorCWID = i.CWID order by s.Name"""
    db: sqlite3.Connection = sqlite3.connect(
                            "C:/Users/shant/Desktop/810_startup.db")
    data: Dict[str, str] = \
        [{'cwid': CWID,
          'name': Name,
          'course': Course,
          'grade': Grade,
          'Iname': IName}
            for CWID, Name, Course, Grade, IName in db.execute(query)]
    db.close()
    return render_template('studentgradesprettytable.html',
                           title='Stevens Repository',
                           table_title='Student, Course, Grade,and Instructor',
                           students=data)


app.run(debug=True)
