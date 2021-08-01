from typing import Any, Dict


class WaLegApiException(Exception):
    """Throws an exception with useful info for debugging"""

    def __init__(self, http_error_num: int, http_error_text: str, http_text: str, args_sent: Dict[str, Any]):
        """
        Parameters
        ----------
        http_error_num: int
            HTTP status code (e.g. 500)
        http_error_text: str
            HTTP status text (e.g. 'Internal Server Error')
        http_text: str
            Any additional text returned with the failed request
            (e.g. System.Web.Services.Protocols.SoapException)
        args_sent: Dict
            The arguments that were sent with this request
        """
        # Store relevant info in the class to be viewabile in a debugger
        self.http_error_num = http_error_num
        self.http_error_text = http_error_text
        self.http_text = http_text
        self.args_sent = args_sent.copy()

        message = f"{http_error_num} {http_error_text}\n{http_text}"
        super().__init__(message)
