from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Duygu",
        "role": "Cloud Engineer",
        "status": "Active",
        "skills": ["Linux", "Git", "Python", "FastAPI"]
    }