import sys

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts the filename and line number where the error occurred.
    """
    # exc_info returns (type, value, traceback)
    _, _, exc_tb = sys.exc_info()
    
    # Navigate the traceback to the actual frame where the error happened
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = f"Error occurred in script: [{file_name}] line number: [{line_number}] error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        # We override the message with the detailed version
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self) -> str:
        return self.error_message