from enum import Enum


class SaleStatus(Enum):
    SOLD = 'sold'
    AVAILABLE = 'available'
    UNDER_CONTRACT = 'under contract'


class FileExtension(Enum):
    TXT = 'txt'
    CSV = 'csv'
