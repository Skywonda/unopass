from sqlalchemy.orm import Session

from server.apis.user.models import User

def get_user(email, db : Session):
    user = db.query(User).filter(User.email == email).first()
    return user 