from enum import Enum


class FileExtension(Enum):
    TXT = 'txt'
    CSV = 'csv'


class HouseAttribute(Enum):
    ADDRESS = 'address'
    CITY = 'city'
    MODEL_NAME = 'model name'
    SQUARE_FOOTAGE = 'square footage'
    SALE_STATUS = 'sale status'
    STATE = 'state'
    ZIPCODE = 'zipcode'


class SaleStatus(Enum):
    SOLD = 'sold'
    AVAILABLE = 'available'
    UNDER_CONTRACT = 'under contract'

