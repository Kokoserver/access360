import bcrypt
from fastapi import status, HTTPException


class AccountManager(object):
    @staticmethod
    def hash_password(password:bytes):
        convertPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        if convertPassword:
            return  convertPassword
        errorResponseData = {
            "status": "error", "message": "Error Creating account please check your details and try again"
        }
        raise HTTPException(detail=errorResponseData, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def check_password(plainPassword, hashedPassword):
        checkPassword = bcrypt.checkpw(plainPassword, hashedPassword)
        if checkPassword:
            return True
        return False







