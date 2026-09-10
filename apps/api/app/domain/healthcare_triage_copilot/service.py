from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.healthcare_triage_copilot.models import AgenticHealthcareTriageCopilotSession, AgenticHealthcareTriageCopilotItem
from app.domain.healthcare_triage_copilot.schemas import AgenticHealthcareTriageCopilotSessionCreate, AgenticHealthcareTriageCopilotItemCreate

class AgenticHealthcareTriageCopilotService:
    @staticmethod
    def create_session(db: Session, data: AgenticHealthcareTriageCopilotSessionCreate) -> AgenticHealthcareTriageCopilotSession:
        db_obj = AgenticHealthcareTriageCopilotSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticHealthcareTriageCopilotSession:
        return db.query(AgenticHealthcareTriageCopilotSession).filter(AgenticHealthcareTriageCopilotSession.id == session_id).first()
