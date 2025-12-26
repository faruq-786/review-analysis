import sys

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()

        if exc_tb:
            self.line_no = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.line_no = "Unknown"
            self.file_name = "Unknown"

    def __str__(self):
        return (
            f"Error occurred in python script "
            f"[{self.file_name}] "
            f"line number [{self.line_no}] "
            f"error message [{self.error_message}]"
        )
