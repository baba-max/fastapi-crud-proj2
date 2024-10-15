from fastapi import HTTPException,status


class DetailedHTTPException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "server error"
    
    def __init__(self):
        super().__init__(status_code=self.STATUS_CODE,
                         detail=self.DETAIL)



class UserNotFoundException(DetailedHTTPException):
    STATUS_CODE=status.HTTP_404_NOT_FOUND
    DETAIL="user is not found"        
    

class WeightNotFound(DetailedHTTPException):
    STATUS_CODE=status.HTTP_200_OK
    DETAIL="User is existing, but weight is not found according user"
    
    
class ExistingUser(DetailedHTTPException):
    STATUS_CODE=status.HTTP_409_CONFLICT
    DETAIL="User is already exist"