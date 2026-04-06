from fastapi import FastAPI, HTTPException, Depends
from .models import WalletCreate, TransferRequest, TransactionResponse
from .service import WalletService

app = FastAPI(title="E-Wallet API")
service = WalletService()

@app.post("/wallets", response_model=dict)
async def create_wallet(req: WalletCreate):
    wallet = service.get_wallet(req.user_id)
    return {"wallet_id": wallet.id, "balance": wallet.balance}

@app.post("/transfer", response_model=TransactionResponse)
async def transfer(req: TransferRequest, from_user_id: str = "sender_user"):
    try:
        return service.transfer(from_user_id, req)
    except ValueError as e:
        raise HTTPException(400, str(e))

@app.get("/balance/{user_id}")
async def get_balance(user_id: str):
    wallet = service.get_wallet(user_id)
    return {"balance": wallet.balance}

@app.get("/history/{user_id}")
async def get_history(user_id: str, limit: int = 10):
    return service.history(user_id, limit)