from enum import Enum, unique


@unique
class DataStatus(Enum):
    DELETED = 0
    NORMAL = 1
