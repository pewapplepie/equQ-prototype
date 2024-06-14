from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import ProgramCreate, Program
from ..models import Program as ProgramModel
from ..config import get_db
from ..services.event_publisher import publish_event


router = APIRouter(prefix="/programs", tags=["programs"])

@router.get("/", response_model=list[Program])
def read_all_program(db: Session = Depends(get_db)):
    try:
        programs = db.query(ProgramModel).all()
        return programs
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=Program)
def create_program(program: ProgramCreate, db: Session = Depends(get_db)):
    new_program = ProgramModel(
        title = program.title,
        description = program.description,
        application_deadline = program.application_deadline,
        curriculum = program.curriculum
    )
    db.add(new_program)
    db.commit()
    db.refresh(new_program)
    # publish_event('program.created', {'program_id': new_program.id, 'title': new_program.title})
    return new_program

@router.put("/{program_id}", response_model=Program)
def update_program(program_id: int, program: ProgramCreate, db: Session = Depends(get_db)):
    program_model = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()

    if program_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {program_id} does not exist"
        )

    program_model.title = program.title
    program_model.description = program.description
    program_model.application_deadline = program.application_deadline
    program_model.curriculum = program.curriculum

    db.add(program_model)
    db.commit()
    db.refresh(program_model)  # Ensure the instance is updated

    return program_model

@router.delete("/{program_id}", response_model=dict)
def delete_program(program_id: int, db: Session = Depends(get_db)):
    program_model = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()

    if program_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {program_id} does not exist"
        )

    db.delete(program_model)
    db.commit()

    return {"detail": f"Program with ID {program_id} has been deleted"}