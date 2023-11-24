from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Lecturer, get_db
from schema import LecturerCreate, create_lecturer, LecturerSchema


router = APIRouter()


# Create Lecturer
@router.post("/lecturers/", response_model=LecturerSchema)
def post_lecturer(lecturer: LecturerCreate, db: Session = Depends(get_db)):
    return create_lecturer(db, lecturer)


# Read Lecturer
@router.get("/lecturers/{lecturer_id}", response_model=LecturerSchema)
def read_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    return db.query(Lecturer).filter(Lecturer.id == lecturer_id).first()


# Update Lecturer
@router.put("/lecturers/{lecturer_id}", response_model=LecturerSchema)
def update_lecturer(lecturer_id: int, lecturer: LecturerCreate, db: Session = Depends(get_db)):
    db_lecturer = db.query(Lecturer).filter(Lecturer.id == lecturer_id).first()
    if db_lecturer:
        for key, value in lecturer.model_dump(mode="python").items():
            setattr(db_lecturer, key, value)
        db.commit()
        db.refresh(db_lecturer)
        return db_lecturer
    else:
        raise HTTPException(status_code=404, detail="Lecturer not found")


# Delete Lecturer
@router.delete("/lecturers/{lecturer_id}", response_model=LecturerSchema)
def delete_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    db_lecturer = db.query(Lecturer).filter(Lecturer.id == lecturer_id).first()
    if db_lecturer:
        db.delete(db_lecturer)
        db.commit()
        return db_lecturer
    else:
        raise HTTPException(status_code=404, detail="Lecturer not found")


# List all Lecturers
@router.get("/lecturers/", response_model=list[LecturerSchema])
def list_lecturers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    lecturers = db.query(Lecturer).offset(skip).limit(limit).all()
    return lecturers
