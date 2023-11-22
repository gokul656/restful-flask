from pydantic import BaseModel, field_validator

from web.app.models.user import User


class UserRegister(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def validate_email(cls, email):
        if User.exists(User.email == email):
            raise ValueError("email already exists")
        return email

    @field_validator("password")
    def validate_password(cls, password):
        if password is None:
            raise ValueError("invalid password")
        elif len(password) <= 8:
            raise ValueError("password length must be greater than 8")
