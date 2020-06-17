#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from enum import Enum

class WorkOrderPriority(Enum):
    URGENT = "URGENT"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NONE = "NONE"
    MISSING_ENUM = ""

    @classmethod
    def _missing_(cls, value: str) -> "WorkOrderPriority":
        return cls.MISSING_ENUM