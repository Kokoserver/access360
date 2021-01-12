from fastapi import  APIRouter, status
from mongoengine import errors
from access360.api.model  import accountModel
from access360.api.model.userMixin import AccountManager
from access360.view.generalMixin import Access360FullMixin
from access360.api.model.AccountPydanticModel import UserRegisterationInput, UserLoginInput
import json

router = APIRouter(prefix="/api/v1/user", tags=["User Account"])

@router.post("/register")
def registerUserAccount(user:UserRegisterationInput):
    if user.password.strip() == user.confirmPassword.strip():
        try:
            password = AccountManager.hash_password(password=user.password)
            newUserDetails = {
                "username": user.username,
                "email": user.email,
                "gender": user.gender,
                "password": password
            }
            newUser = accountModel.UserAccount(**newUserDetails).save(clean=True)
            if newUser:
                SuccessResponseData = {
                    "user": newUser.to_json(indent=4),
                    "message": "Account was created successfully",
                    "extra detail": {
                        "login": "Login to your account",
                        "method": "post",
                        "body": {"email": "string", "password": "string"}
                    }
                }
                return Access360FullMixin.Response(message=SuccessResponseData, success=True,
                                                   status_code=status.HTTP_201_CREATED)
            ErrorResponseData = {"message": "Error creating account, check your detail and try again"}
            return Access360FullMixin.Response(message=ErrorResponseData, success=False,
                                        status_code=status.HTTP_400_BAD_REQUEST)
        except errors.ValidationError:
            ErrorResponseData = {"message": "Error creating account, check your detail and try again"}
            return Access360FullMixin.Response(message=ErrorResponseData, success=False,
                                        status_code=status.HTTP_400_BAD_REQUEST)

        except errors.NotUniqueError:
            ErrorResponseData = {"message": "Account with this email already exist, try again"}
            return Access360FullMixin.Response(message=ErrorResponseData, success=False,
                                               status_code=status.HTTP_400_BAD_REQUEST)

    ErrorResponseData = {"message":"Password do not match, try again"}
    return Access360FullMixin.Response(message=ErrorResponseData,
                                       success=False,
                                       status_code=status.HTTP_400_BAD_REQUEST)

@router.post("/login")
def loginUserAccount(userIn:UserLoginInput):
    checkUser = accountModel.UserAccount(email=userIn.email)
    print(print(checkUser.pk))

    # if checkUser:
    #     if AccountManager.check_password(user.password, checkUser.password):
    #         SuccessResponseData = {"message":"logged in successfully" }
    #         Access360FullMixin.Response(message=SuccessResponseData,
    #                                     status_code=status.HTTP_200_OK, success=True)
    #         ErrorResponseData = {"message": "Error login, try again"}
    #         return Access360FullMixin.Response(message=ErrorResponseData,
    #                                            status_code=status.HTTP_401_UNAUTHORIZED,
    #                                            success=False)
    # ErrorResponseData = {"message": "Account does not exist"}
    # return Access360FullMixin.Response(message=ErrorResponseData,
    #                                    status_code=status.HTTP_401_UNAUTHORIZED,
    #                                    success=False)





