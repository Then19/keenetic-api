from functools import wraps
from typing import Any, Callable

from fastapi import HTTPException

from src.logger import logger
from src.service.exceptions import BaseServiceException


def service_exception_handler(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        try:
            return await func(*args, **kwargs)
        except BaseServiceException as e:
            raise HTTPException(e.status_code, str(e))
        except HTTPException as e:
            raise e
        except Exception as e:
            logger.error(e)
            raise HTTPException(status_code=400, detail='Ошибка обработки запроса. Пожалуйста, обратитесь к администратору')
    return wrapper
