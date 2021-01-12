from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

class Access360FullMixin:
    @staticmethod
    def  Response(message:dict, success:bool, status_code)->dict:
        if success:
            return JSONResponse(content={"status":"success", "message":message}, status_code=status_code)
        return JSONResponse(content={"status": "error", "message": message}, status_code=status_code)
    @staticmethod
    def getData(data:dict) -> dict:
        try:
            if data:
                for data in data:
                    return data
        except Exception:
            ErrorResponseData = {"error": "Invalid details to iterate"}
            return Access360FullMixin.Response(message=ErrorResponseData, success=False,
                                                               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



