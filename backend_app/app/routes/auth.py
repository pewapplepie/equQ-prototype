from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import UserCreate
from ..models import User
from ..config import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(username=user.username, email=user.email, hashed_password=user.password)  # You should hash the password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
