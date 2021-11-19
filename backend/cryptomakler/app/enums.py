from enum import Enum


class InvestmentOperationEnum(str, Enum):
    WITHDRAW = 'WITHDRAW'
    DEPOSIT = 'DEPOSIT'
    WITHDRAW_ALL = 'WITHDRAW_ALL'
