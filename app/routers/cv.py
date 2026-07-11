from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.matching_service import extract_skills
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter(
    prefix="/cv",
    tags=["CV"]
)

MAX_FILE_SIZE = 5 * 1024 * 1024


@router.post("/analyze")
async def analyze_cv(file: UploadFile = File(...)):
    filename = file.filename or ""

    if not filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten archivos PDF"
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="El archivo está vacío"
        )

    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="El PDF no puede superar los 5 MB"
        )

    try:
        text = extract_text_from_pdf(file_content)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="No se pudo leer el archivo PDF"
        )

    if not text:
        raise HTTPException(
            status_code=422,
            detail="No se encontró texto dentro del PDF"
        )

    skills = extract_skills(text)

    return {
        "success": True,
        "filename": filename,
        "text": text,
        "skills": skills,
        "total_skills": len(skills)
    }