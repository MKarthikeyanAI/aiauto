class Teacher:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)


class Subject:
    def __init__(self, name):
        self.name = name


def generate_time_table(teachers, subjects, classroom_availability):
    timetable = {}
    for day in classroom_availability:
        timetable[day] = {}
        for period in classroom_availability[day]:
            for teacher in teachers:
                for subject in teacher.subjects:
                    if period not in timetable[day]:
                        timetable[day][period] = (teacher.name, subject.name)
                        break
    return timetable


def display_time_table(timetable):
    for day, periods in timetable.items():
        print(f"Day: {day}")
        for period, assignment in periods.items():
            teacher, subject = assignment
            print(f"  Period: {period} - Teacher: {teacher}, Subject: {subject}")
        print()


# Input Data
teachers = []
subjects = []

num_teachers = int(input("Enter number of teachers: "))
for _ in range(num_teachers):
    teacher_name = input("Enter teacher's name: ")
    teacher = Teacher(teacher_name)
    num_subjects = int(input(f"Enter number of subjects for {teacher_name}: "))
    for _ in range(num_subjects):
        subject_name = input("Enter subject name: ")
        subject = Subject(subject_name)
        teacher.add_subject(subject)
        subjects.append(subject)
    teachers.append(teacher)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = ["Morning", "Afternoon"]
classroom_availability = {day: periods for day in days}

# Generate and display timetable
timetable = generate_time_table(teachers, subjects, classroom_availability)
display_time_table(timetable)
