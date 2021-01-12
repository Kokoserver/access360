from pydantic import BaseModel, EmailStr, Field

class UserRegisterationInput(BaseModel):
    username:str = Field(title="Username", description="The user name that will appear everywhere", min_length=3, max_length=50)
    email:EmailStr
    gender:str
    password:bytes = Field(title="User password", description="User password to protect account")
    confirmPassword:bytes = Field(title=" Confirm user password", description="User password to protect account")


class UserLoginInput(BaseModel):
    email:EmailStr
    password:bytes


