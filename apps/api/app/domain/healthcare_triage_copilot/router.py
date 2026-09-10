from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.healthcare_triage_copilot.schemas import AgenticHealthcareTriageCopilotSessionCreate, AgenticHealthcareTriageCopilotSessionResponse
from app.domain.healthcare_triage_copilot.service import AgenticHealthcareTriageCopilotService

router = APIRouter(prefix="/api/v1/healthcare_triage_copilot", tags=["Agentic Healthcare Triage Copilot Domain"])

@router.post("/sessions", response_model=AgenticHealthcareTriageCopilotSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticHealthcareTriageCopilotSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Healthcare Triage Copilot.
    """
    return AgenticHealthcareTriageCopilotService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticHealthcareTriageCopilotSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticHealthcareTriageCopilotService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
