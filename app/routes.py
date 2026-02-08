from fastapi import APIRouter
from .schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest):
    text = payload.text
    return AnalyzeResponse(
        length=len(text),
        uppercase=text.isupper()
    )