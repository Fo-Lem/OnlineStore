from enum import Enum

class HTTP_RESPONSE_MESSAGE(Enum):
    #Default
    SUCCSESSFUL = "Successful"
    ABORTED = "Aborted"
    INCORRECT_DATA = "Inncorrect data"

    #CRUD operations
    SUCCESSFUL_CREATED = "Created"
    NO_ANY_PARAMETRS = "You don't provide any parametrs"
    ABORTED_CREATED = "Was not created"
    SUCCESSFUL_MODIFIED = "Modified"
    ABORTED_MODIFIED = "Was not modified"
    SUCCESSFUL_DELEATED = "Deleted"
    ABORTED_DELEATED = "Was not deleted"

    #mail
    SUCCESSFUL_SENT = "Message was sent"
    ABORTED_SENT = "Message sending was aborted"

    #On login
    ACCESS_DENIED = "Access denied"
    INCORRECT_LOGIN = "Login is incorrect"
    INCORRECT_PASSWORD = "Password is incorrect"

    #JWT token
    JWT_TOKEN_IS_VALID = "JWT token is valid"
    JWT_TOKEN_NOT_VALID = "JWT token is NOT valid"

    #Refresh token
    REFRESH_TOKEN_NOT_EXIST = "Refresh token don't exist"
    REFRESH_TOKEN_NOT_VALID = "Refresh token is NOT valid"
