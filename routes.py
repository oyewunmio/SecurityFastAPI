from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from deps import get_db, get_current_user
from models import UserCreate, User, UserLogin, Token, UserOutput
from typing import Annotated, Any
from fastapi.security import OAuth2PasswordRequestForm
from utils import get_password_hash, verify_password, create_access_token
import crud
from datetime import timedelta
from config import settings
router = APIRouter()

@router.post("/register", tags=["login"])
async def register(
    user: UserCreate, 
    db: Annotated[Session,  Depends(get_db)]
):
    #hash the password
    user.password = get_password_hash(user.password)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return user

@router.post("/login", tags=["login"])
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    # get user by email
    user = crud.authenticate(
        session=db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )
    

@router.post("/login/test-token", response_model=UserOutput)
def test_token(current_user: Annotated[User, Depends(get_current_user)]
) -> Any:
    """
    Test access token
    """
    return current_user


    
    