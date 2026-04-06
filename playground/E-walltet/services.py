import sqlite3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///./wallet.db", echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

class WalletService:
    def __init__(self):
        self.db = SessionLocal()

    def get_wallet(self, user_id: str) -> UserWallet:
        # Create if not exists
        wallet = self.db.query(UserWallet).filter(UserWallet.user_id == user_id).first()
        if not wallet:
            wallet = UserWallet(user_id=user_id)
            self.db.add(wallet)
            self.db.commit()
        return wallet

    def transfer(self, from_user_id: str, req: TransferRequest) -> TransactionResponse:
        with self.db.begin():  # ACID transaction
            # Idempotency check
            existing = self.db.query(Transaction).filter(Transaction.idempotency_key == req.idempotency_key).first()
            if existing:
                return self._build_response(existing)

            from_wallet = self.get_wallet(from_user_id)
            to_wallet = self.get_wallet(req.to_user_id)

            if from_wallet.balance < req.amount:
                raise ValueError("Insufficient balance")

            # Atomic updates
            txn = Transaction(
                idempotency_key=req.idempotency_key,
                from_wallet_id=from_wallet.id,
                to_wallet_id=to_wallet.id,
                amount=req.amount,
                type="transfer"
            )
            self.db.add(txn)

            from_wallet.balance -= req.amount
            to_wallet.balance += req.amount

            txn.status = "success"
            self.db.commit()

        return self._build_response(txn)

    def _build_response(self, txn: Transaction) -> TransactionResponse:
        from_wallet = self.db.query(UserWallet).get(txn.from_wallet_id)
        to_wallet = self.db.query(UserWallet).get(txn.to_wallet_id)
        return TransactionResponse(
            id=txn.id, status=txn.status, amount=txn.amount,
            from_balance=from_wallet.balance, to_balance=to_wallet.balance
        )

    def history(self, user_id: str, limit: int = 10):
        wallet = self.get_wallet(user_id)
        txns = self.db.query(Transaction).filter(
            (Transaction.from_wallet_id == wallet.id) | (Transaction.to_wallet_id == wallet.id)
        ).order_by(Transaction.created_at.desc()).limit(limit).all()
        return [{"id": t.id, "amount": t.amount, "status": t.status, "date": t.created_at} for t in txns]