from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status, HTTPException
from jose import jwt, JWTError

from server.apis.dependencies import get_db
from server.config.security import create_access_token
from server.config.settings import settings
from server.apis.login.repositories import get_user
from server.apis.login.schemas import Token

router = APIRouter()

def authenticate_user(email : str, password : str, db : Session):
    user = get_user(email, db)
    if not user:
        return False
    if password != user.password:
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    access_token = create_access_token(data={"sub" : user.email})
    return {"access_token" : access_token, "token_type" : "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

def get_current_from_token(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    credential_expection = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate Credentials")

    try:
        payload =jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        username : str = payload.get("sub")
        print("username is extracted ", username)
        if username is None:
            raise credential_expection
    except JWTError:
        raise credential_expection
    user = get_user(email = username, db=db)
    if user is None:
        raise credential_expection
    return user