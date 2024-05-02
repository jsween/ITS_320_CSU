from enum import Enum


class FileExtension(Enum):
    """
    Supported File Extensions
    """
    TXT = 'txt'
    CSV = 'csv'


class HouseAttribute(Enum):
    """
    Supported House Attributes
    """
    ADDRESS = 'address'
    CITY = 'city'
    MODEL_NAME = 'model name'
    SQUARE_FOOTAGE = 'square footage'
    SALE_STATUS = 'sale status'
    STATE = 'state'
    ZIPCODE = 'zipcode'


class SaleStatus(Enum):
    """
    Valid Sales Status
    """
    SOLD = 'sold'
    AVAILABLE = 'available'
    UNDER_CONTRACT = 'under contract'

