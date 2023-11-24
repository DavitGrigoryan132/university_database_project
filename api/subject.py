from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Subject, get_db
from schema import SubjectCreate, SubjectSchema, create_subject

router = APIRouter()


# Create Subject
@router.post("/subjects/", response_model=SubjectSchema)
def post_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return create_subject(db, subject)


# Read Subject
@router.get("/subjects/{name}", response_model=SubjectSchema)
def read_subject(name: str, db: Session = Depends(get_db)):
    return db.query(Subject).filter(Subject.name == name).first()


# Update Subject
@router.put("/subjects/{name}", response_model=SubjectSchema)
def update_subject(name: str, subject: SubjectCreate, db: Session = Depends(get_db)):
    db_subject = db.query(Subject).filter(Subject.name == name).first()
    if db_subject:
        for key, value in subject.dict().items():
            setattr(db_subject, key, value)
        db.commit()
        db.refresh(db_subject)
        return db_subject
    else:
        raise HTTPException(status_code=404, detail="Subject not found")


# Delete Subject
@router.delete("/subjects/{name}", response_model=SubjectSchema)
def delete_subject(name: str, db: Session = Depends(get_db)):
    db_subject = db.query(Subject).filter(Subject.name == name).first()
    if db_subject:
        db.delete(db_subject)
        db.commit()
        return db_subject
    else:
        raise HTTPException(status_code=404, detail="Subject not found")


# List all Subjects
@router.get("/subjects/", response_model=list[SubjectSchema])
def list_subjects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    subjects = db.query(Subject).offset(skip).limit(limit).all()
    return subjects


# Update a subject's hours if it's required
@router.put("/update-subject-hours/{name}", response_model=SubjectSchema)
def update_subject_hours(name: str, db: Session = Depends(get_db)):
    db_subject = db.query(Subject).filter(Subject.name == name, Subject.required == True).first()
    if db_subject:
        db_subject.hours += 10  # Increase hours by 10
        db.commit()
        db.refresh(db_subject)
        return db_subject
    else:
        raise HTTPException(status_code=404, detail="Subject not found or not required")


# Get a list of subjects sorted by name
@router.get("/subjects-sorted/", response_model=list[SubjectSchema])
def list_subjects_sorted(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    subjects = (
        db.query(Subject)
        .order_by(Subject.name)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return subjects
