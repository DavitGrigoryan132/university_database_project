import random
from faker import Faker
from models import Subject, Lecturer
from schema import SubjectCreate, LessonCreate, LecturerCreate
from api.lecturer import post_lecturer
from api.lesson import post_lesson
from api.subject import post_subject
from models import Session

fake = Faker()

# Function to generate random data for subjects
subject_names_set = set()


# Function to generate random data for subjects with unique names
def generate_subject_data():
    exam_types = [
        "Final Exam",
        "Midterm Exam",
        "Quiz",
        "Project",
        "Paper",
        "Presentation",
        "Lab Exam",
        "Oral Exam",
        "Practical Exam",
        "Open-book Exam",
        "Closed-book Exam",
        "Take-home Exam",
        "Group Project",
        "Thesis",
        "Dissertation",
        "Portfolio Assessment",
        "Peer Review",
        "Case Study",
        "Simulation",
        "Problem Set",
        "Research Paper",
        "Practicum",
        "Fieldwork",
        "Viva Voce",
    ]

    while True:
        subject_name = fake.catch_phrase()
        if subject_name not in subject_names_set:
            subject_names_set.add(subject_name)
            return {
                "name": subject_name,
                "exam_type": random.choice(exam_types),
                "hours": fake.random_int(min=1, max=100),
                "required": fake.pybool(),
            }


lesson_datetime_set = set()


# Function to generate random data for lessons with unique date-time pairs
def generate_lesson_data(lecturer_id, subject_name):
    while True:
        lesson_date = fake.date_between(start_date="-50d", end_date="+50d")
        lesson_time = fake.time()
        lesson_datetime_pair = (lesson_date, lesson_time)

        class_types = [
            "Lecture",
            "Seminar",
            "Lab",
            "Workshop",
            "Discussion",
            "Tutorial",
            "Studio",
            "Recitation",
            "Field Trip",
            "Independent Study",
            "Capstone Project",
            "Internship",
            "Thesis",
            "Dissertation",
            "Online Course",
            "Hybrid Course",
            "Project-Based Learning",
            "Group Project",
            "Presentation",
            "Examination",
            "Research",
            "Practicum",
            "Honors Course",
        ]

        if lesson_datetime_pair not in lesson_datetime_set:
            lesson_datetime_set.add(lesson_datetime_pair)
            return {
                "date": lesson_date,
                "time": lesson_time,
                "classroom": f"Room{random.choice(range(100, 999))}",
                "type": random.choice(class_types),
                "group": f"Group {random.randint(1, 999):03}",
                "lecturer_id": lecturer_id,
                "subject_name": subject_name,
            }


# Function to generate random data for lecturers with unique full names
def generate_lecturer_data():
    lecturer_positions = [
        "Professor",
        "Associate Professor",
        "Assistant Professor",
        "Lecturer",
        "Senior Lecturer",
        "Adjunct Professor",
        "Visiting Professor",
        "Research Professor",
        "Instructor",
        "Emeritus Professor",
        "Clinical Professor",
        "Distinguished Professor",
        "Chair of Department",
        "Dean of Faculty",
        "Provost",
    ]

    university_departments = [
        "Computer Science",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Chemistry",
        "Physics",
        "Biology",
        "Mathematics",
        "History",
        "Psychology",
        "Economics",
        "Business Administration",
        "Political Science",
        "English Literature",
        "Sociology",
        "Art and Design",
        "Music",
        "Civil Engineering",
        "Environmental Science",
        "Medical School",
        "Law School",
        "Education",
        "Languages and Linguistics",
        "Philosophy",
        "Geology",
        "Nursing",
        "Public Health",
        "Architecture",
        "Astronomy",
        "Communication Studies",
        "Theater and Dance",
        "Agricultural Science",
        "Food Science",
        "Pharmacy",
        "Social Work",
        "Anthropology",
        "Nutrition",
        "Materials Science",
    ]

    academic_degrees = [
        "Associate's Degree",
        "Bachelor's Degree",
        "Master's Degree",
        "Doctor of Philosophy (Ph.D.)",
        "Doctor of Medicine (M.D.)",
        "Juris Doctor (J.D.)",
        "Master of Business Administration (MBA)",
        "Master of Science (M.S.)",
        "Master of Arts (M.A.)",
        "Bachelor of Science (B.S.)",
        "Bachelor of Arts (B.A.)",
        "Doctor of Education (Ed.D.)",
        "Doctor of Science (Sc.D.)",
        "Doctor of Engineering (Eng.D.)",
        "Doctor of Psychology (Psy.D.)",
        "Doctor of Nursing Practice (DNP)",
        "Master of Public Health (MPH)",
        "Master of Fine Arts (MFA)",
        "Bachelor of Engineering (B.Eng.)",
        "Bachelor of Business Administration (BBA)",
        "Bachelor of Fine Arts (BFA)",
        "Bachelor of Education (B.Ed.)",
        "Associate of Science (A.S.)",
        "Associate of Arts (A.A.)",
        "Associate of Applied Science (AAS)",
        "Certificate of Higher Education",
        "Diploma of Higher Education",
        "Postgraduate Certificate",
        "Postgraduate Diploma",
        "Professional Doctorate",
        "Honorary Doctorate",
        "Fellowship",
    ]

    full_name = fake.name()
    return {
        "department": random.choice(university_departments),
        "position": random.choice(lecturer_positions),
        "full_name": full_name,
        "academic_degree": random.choice(academic_degrees),
    }


# Function to fill the database with 1000 rows for each entity
def fill_database():
    db = Session()

    # Fill subjects
    for _ in range(50):
        subject_data = generate_subject_data()
        subject = SubjectCreate(**subject_data)
        post_subject(subject, db)

    # Fill lecturers
    for _ in range(50):
        lecturer_data = generate_lecturer_data()
        lecturer = LecturerCreate(**lecturer_data)
        post_lecturer(lecturer, db)

    # Fill lessons
    lecturer_ids = db.query(Lecturer.id).limit(50).all()
    subject_names = db.query(Subject.name).limit(50).all()
    for i in range(50):
        lesson_data = generate_lesson_data(lecturer_ids[i][0], subject_names[i][0])
        lesson = LessonCreate(**lesson_data)
        post_lesson(lesson, db)

    db.close()


if __name__ == "__main__":
    fill_database()
