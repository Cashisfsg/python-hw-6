from datetime import date, datetime, timedelta
from university import Course, Mentor, Teacher, Student, University

python_course = Course("Python", datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=30))
js_course = Course("JavaScript", datetime.now() + timedelta(days=1), datetime.now() + timedelta(days=60))
java = Course("Java", datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=60))

alex_student = Student("Alex", "Stp", date(1995, 7, 8))
nik_student = Student("Nik", "Fial", date(1998, 10, 22))

bred_teacher = Teacher("Bred", "Cmp", date(1974, 6, 25), 2000, python_course)

koli_mentor = Mentor("Koli", "Key", date(1987, 3, 13), 1200, [python_course, js_course])

harvard_university = University(
    name="Harvard",
    courses=[python_course, js_course],
    employees=[bred_teacher, koli_mentor],
    students=[alex_student, nik_student],
)

# nik_student.add_mark(12)
# nik_student.add_mark(13)
# nik_student.add_mark(3)
# nik_student.add_mark(2)
# nik_student.add_mark(2)
# nik_student.add_mark(2)

# alex_student.add_mark(10)
# alex_student.add_mark(10)
# alex_student.add_mark(10)



if __name__ == '__main__':
    print(bred_teacher.get_yearly_salary())
    print(str(bred_teacher))
    print(bred_teacher.change_course(course=js_course))
    print('Question:', bred_teacher.answer_question(course=python_course, question='pytHon'))

    print(nik_student._marks)
    print(nik_student.get_all_marks())
    print(nik_student.get_avarage_mark())
    print(nik_student.get_average_by_last_n_marks(n=-1))
    print(nik_student.get_average_from_date(from_date=date(2022, 8, 3)))
    print(str(nik_student))

    print(str(koli_mentor))
    # koli_mentor.change_courses(courses=[])
    print(str(koli_mentor))
    print(koli_mentor.answer_question(course=python_course, question='123'))
    print(koli_mentor.answer_question(course=python_course, question='123'))
    print(koli_mentor.answer_question(course=python_course, question='123'))
    print(koli_mentor.answer_question(course=js_course, question='123'))
    print(koli_mentor.answer_question(course=js_course, question='123'))
    print(koli_mentor.answer_question(course=js_course, question='123'))
    print(koli_mentor.answer_question(course=python_course, question='345'))
    print(koli_mentor.answer_question(course=js_course, question='345'))
    print(koli_mentor.answer_question(course=js_course, question='345'))
    print(koli_mentor.answer_question(course=python_course, question='789'))
    print(koli_mentor.questions)



    print(harvard_university.get_average_salary())
    print(harvard_university.get_average_mark())
    print(harvard_university.get_active_courses())