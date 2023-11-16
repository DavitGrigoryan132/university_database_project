from typing import Optional
from datetime import date, time
from pydantic import BaseModel, PositiveInt, constr


class LecturerBase(BaseModel):
    department: str
    position: str
    full_name: str
    academic_degree: str


class LecturerCreate(LecturerBase):
    pass


class Lecturer(LecturerBase):
    id: PositiveInt

    class Config:
        orm_mode = True


class LessonBase(BaseModel):
    date: date
    time: time
    classroom: str
    type: str
    group: str
    lecturer_id: PositiveInt
    subject_name: constr(max_length=255)


class LessonCreate(LessonBase):
    pass


class Lesson(LessonBase):
    class Config:
        orm_mode = True


class SubjectBase(BaseModel):
    name: str
    exam_type: str
    hours: int
    required: Optional[bool]


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    class Config:
        orm_mode = True


# Function to add a new lesson to the database
def create_lesson(db_session, lesson: LessonCreate):
    db_lesson = Lesson(**lesson.model_dump(mode="python"))
    db_session.add(db_lesson)
    db_session.commit()
    db_session.refresh(db_lesson)
    return db_lesson


# Function to add a new lecturer to the database
def create_lecturer(db_session, lecturer: LecturerCreate):
    db_lecturer = Lecturer(**lecturer.model_dump(mode="python"))
    db_session.add(db_lecturer)
    db_session.commit()
    db_session.refresh(db_lecturer)
    return db_lecturer


# Function to add a new subject to the database
def create_subject(db_session, subject: SubjectCreate):
    db_subject = Subject(**subject.model_dump(mode="python"))
    db_session.add(db_subject)
    db_session.commit()
    db_session.refresh(db_subject)
    return db_subject
