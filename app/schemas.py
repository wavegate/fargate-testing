from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    length: int
    uppercase: bool