## THIS FILE IS A CUSTOM ERROR HANDLING SCRIPT THAT RETURNS ERROR DETAILS

##IMPORTS
import sys
from source.logs import logging

## Function to print error details
def error_message_tracker(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    message = "Error in script: [{0}], line: [{1}], error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return message 

## Class for exception handling
class CustomException(Exception):

    ## Initialize error message value in exception class
    def __init__(self, message, error_detail:sys):
        super().__init__(message)
        self.message = error_message_tracker(message, error_detail=error_detail)

    ## Return error message to be printed when class is called
    def __str__(self):
        return self.message
    


