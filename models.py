from sqlalchemy import create_engine, Column, Integer, \
    String, Date, Time, Boolean, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="university",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()


# Dependency to get the SQLAlchemy session
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


class Lecturer(Base):
    __tablename__ = "lecturer"

    id = Column(Integer, primary_key=True)
    department = Column(String)
    position = Column(String)
    full_name = Column(String)
    academic_degree = Column(String)

    _lesson = relationship("Lesson", backref="lecturer")


class Lesson(Base):
    __tablename__ = "lesson"

    date = Column(Date, primary_key=True)
    time = Column(Time, primary_key=True)
    classroom = Column(String)
    type = Column(String)
    group = Column(String)
    lecturer_id = Column(Integer, ForeignKey("lecturer.id"))
    subject_name = Column(String, ForeignKey("subject.name"))


class Subject(Base):
    __tablename__ = "subject"

    name = Column(String, primary_key=True)
    exam_type = Column(String)
    hours = Column(Integer)
    required = Column(Boolean, default=True)

    _lesson = relationship("Lesson", backref="subject")


Base.metadata.create_all(engine)
