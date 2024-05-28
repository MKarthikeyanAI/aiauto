import random

class Teacher:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


def get_teachers():
    teachers = []
    num_teachers = int(input("Enter the number of teachers: "))
    for _ in range(num_teachers):
        teacher_name = input("Enter teacher's name: ")
        teacher = Teacher(teacher_name)
        teachers.append(teacher)
    return teachers


def get_subjects(teachers):
    subjects = []
    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject_name = input("Enter subject's name: ")
        teacher_name = input("Enter the name of the teacher who can teach this subject: ")
        teacher = next((t for t in teachers if t.name == teacher_name), None)
        if teacher:
            subject = Subject(subject_name, teacher)
            teacher.add_subject(subject)
            subjects.append(subject)
        else:
            print("Teacher not found.")
    return subjects


def get_classroom_availability():
    classroom_availability = {}
    #num_days = 5  # Monday to Friday
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['9:00 am', '10:00 am', '11:00 am', '2:00 pm', '3:00 pm']

    for day in days:
        classroom_availability[day] = {}
        for slot in time_slots:
            available_classrooms = int(input(f"Enter number of available classrooms for {day} at {slot}: "))
            classroom_availability[day][slot] = available_classrooms

    return classroom_availability


def generate_time_table(teachers, subjects, classroom_availability):
    timetable = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['9:00 am', '10:00 am', '11:00 am', '2:00 pm', '3:00 pm']

    for day in days:
        timetable[day] = {}
        for slot in time_slots:
            timetable[day][slot] = []

    for day in days:
        for slot in time_slots:
            available_classrooms = classroom_availability[day][slot]
            assigned_classrooms = 0

            # Shuffle subjects to assign different subjects to different time slots
            random.shuffle(subjects)

            for subject in subjects:
                if assigned_classrooms < available_classrooms:
                    timetable[day][slot].append((subject.name, subject.teacher.name))
                    assigned_classrooms += 1
                else:
                    break

    return timetable


def display_time_table(timetable):
    print("\nGenerated Timetable:")
    for day, slots in timetable.items():
        print(f"\n{day}:")
        for slot, classes in slots.items():
            print(f"  {slot}:")
            for subject, teacher in classes:
                print(f"    {subject} taught by {teacher}")


def main():
    # Collect data
    teachers = get_teachers()
    subjects = get_subjects(teachers)
    classroom_availability = get_classroom_availability()

    # Generate timetable
    timetable = generate_time_table(teachers, subjects, classroom_availability)

    # Display the generated timetable
    display_time_table(timetable)


if __name__ == "__main__":
    main()
