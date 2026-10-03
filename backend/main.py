from fastapi import FastAPI

app = FastAPI(title="AI Career Agent")


@app.get("/")
def home():
    return {
        "message": "AI Career Agent is running!",
        "status": "success"
    }