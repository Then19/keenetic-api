class BaseServiceException(Exception):
    status_code: int

    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code


def create_service_exception(default_message: str, default_status_code: int) -> type[BaseServiceException]:
    class CustomServiceException(BaseServiceException):
        def __init__(self, message: str | None = None, status_code: int | None = None):
            super().__init__(message or default_message, status_code or default_status_code)

    CustomServiceException.__name__ = f"ServiceException_{default_message[:20]}"
    return CustomServiceException

