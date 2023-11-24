from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from models import Lesson, Lecturer, get_db
from schema import LessonCreate, LessonSchema, LessonWithLecturerSchema, create_lesson


router = APIRouter()


# Create Lesson
@router.post("/lessons/", response_model=LessonSchema)
def post_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    return create_lesson(db, lesson)


# Read Lesson
@router.get("/lessons/{date}/{time}", response_model=LessonSchema)
def read_lesson(date: str, time: str, db: Session = Depends(get_db)):
    return db.query(Lesson).filter(Lesson.date == date, Lesson.time == time).first()


# Update Lesson
@router.put("/lessons/{date}/{time}", response_model=LessonSchema)
def update_lesson(date: str, time: str, lesson: LessonCreate, db: Session = Depends(get_db)):
    db_lesson = db.query(Lesson).filter(Lesson.date == date, Lesson.time == time).first()
    if db_lesson:
        for key, value in lesson.dict().items():
            setattr(db_lesson, key, value)
        db.commit()
        db.refresh(db_lesson)
        return db_lesson
    else:
        raise HTTPException(status_code=404, detail="Lesson not found")


# Delete Lesson
@router.delete("/lessons/{date}/{time}", response_model=LessonSchema)
def delete_lesson(date: str, time: str, db: Session = Depends(get_db)):
    db_lesson = db.query(Lesson).filter(Lesson.date == date, Lesson.time == time).first()
    if db_lesson:
        db.delete(db_lesson)
        db.commit()
        return db_lesson
    else:
        raise HTTPException(status_code=404, detail="Lesson not found")


# List all Lessons
@router.get("/lessons/", response_model=list[LessonSchema])
def list_lessons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    lessons = db.query(Lesson).offset(skip).limit(limit).all()
    return lessons


# List all lessons with associated lecturer information
@router.get("/lessons-with-lecturers/", response_model=list[LessonWithLecturerSchema])
def list_lessons_with_lecturers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    lessons = (
        db.query(Lesson, Lecturer.full_name)
        .join(Lecturer, Lesson.lecturer_id == Lecturer.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [{"lesson": lesson, "lecturer_full_name": lecturer_full_name} for lesson, lecturer_full_name in lessons]


# Count the number of lessons for each subject
@router.get("/lesson-count-by-subject/", response_model=dict)
def lesson_count_by_subject(db: Session = Depends(get_db)):
    result = (
        db.query(Lesson.subject_name, func.count(Lesson.subject_name))
        .group_by(Lesson.subject_name)
        .all()
    )
    return dict(result)
