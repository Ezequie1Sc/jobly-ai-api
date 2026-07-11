from fastapi import FastAPI

app = FastAPI(
    title="Jobly AI API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "success": True,
        "message": "Jobly AI API funcionando"
    }