from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def as_list(cls):
        return [item.value for item in cls]


class Status(str, BaseEnum):
    """
    This is all pet statuses
    """
    Available: str = "available"
    NotAvailable: str = "not-available"

    def __str__(self) -> str:
        return str.__str__(self)


class HttpErrorCodes(int, Enum):
    Content: int = 200
    BadRequest: int = 400
    NotFound: int = 404

    def __int__(self) -> int:
        return int.__int__(self)


