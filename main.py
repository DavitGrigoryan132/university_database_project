from fastapi import FastAPI
from api.lecturer import router as lecturer_router
from api.lesson import router as lesson_router
from api.subject import router as subject_router

# Create a FastAPI app
app = FastAPI()
app.include_router(lesson_router)
app.include_router(lecturer_router)
app.include_router(subject_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
