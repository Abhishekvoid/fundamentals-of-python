from pydantic import BaseModel, Field, PositiveFloat
from typing import Literal
from datetime import datetime
from enum import Enum
import uuid
from sqlalchemy import Column, String, Float, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class TransactionType(str, Enum):
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class UserWallet(Base):
    __tablename__ = "wallets"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True)
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    idempotency_key = Column(String, unique=True, index=True)
    from_wallet_id = Column(String, ForeignKey("wallets.id"))
    to_wallet_id = Column(String, ForeignKey("wallets.id"))
    amount = Column(Float)
    type = Column(String)  # TRANSFER
    status = Column(String, default="pending")  # pending/success/failed
    created_at = Column(DateTime, default=datetime.utcnow)

class WalletCreate(BaseModel):
    user_id: str = Field(..., min_length=3)

class TransferRequest(BaseModel):
    idempotency_key: str = Field(..., description="Unique key to prevent duplicates")
    to_user_id: str
    amount: PositiveFloat = Field(..., gt=0, description="INR amount")

class TransactionResponse(BaseModel):
    id: str
    status: str
    amount: float
    from_balance: float
    to_balance: float