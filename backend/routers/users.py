from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.schemas.user import UserCreate,UserResponse

from backend.services.user_service import create_user as create_user_service,get_user_by_email ,get_user_by_username

# creates a router object
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"message": "Database session created successfully"}

@router.post("/",response_model=UserResponse)
def create_user(user:UserCreate,db:Session = Depends(get_db)):
    
    existing_email = get_user_by_email(db,user.email)

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    existing_username = get_user_by_username(db,user.username)

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return create_user_service(db=db,
            username=user.username,
            email=user.email,
            hashed_password=user.password)