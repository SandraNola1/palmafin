from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import aiosqlite
import asyncio
from datetime import datetime

router = APIRouter()

DB = "palmafin.db"

async def init_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                currency TEXT DEFAULT 'RUB',
                category TEXT,
                project TEXT,
                note TEXT,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)
        await db.commit()

class Transaction(BaseModel):
    type: str  # income | expense
    amount: float
    currency: str = "RUB"
    category: Optional[str] = None
    project: Optional[str] = None
    note: Optional[str] = None

@router.on_event("startup")
async def startup():
    await init_db()

@router.get("/summary")
async def get_summary():
    async with aiosqlite.connect(DB) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("""
            SELECT type, SUM(amount) as total
            FROM transactions
            WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
            GROUP BY type
        """)
        rows = await cur.fetchall()
    income = next((r["total"] for r in rows if r["type"] == "income"), 0)
    expense = next((r["total"] for r in rows if r["type"] == "expense"), 0)
    return {
        "month": datetime.now().strftime("%B %Y"),
        "income": round(income, 2),
        "expense": round(expense, 2),
        "net": round(income - expense, 2)
    }

@router.get("/transactions")
async def get_transactions(limit: int = 20):
    async with aiosqlite.connect(DB) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute(
            "SELECT * FROM transactions ORDER BY created_at DESC LIMIT ?", (limit,)
        )
        rows = await cur.fetchall()
    return [dict(r) for r in rows]

@router.post("/transactions")
async def add_transaction(tx: Transaction):
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            "INSERT INTO transactions (type, amount, currency, category, project, note) VALUES (?,?,?,?,?,?)",
            (tx.type, tx.amount, tx.currency, tx.category, tx.project, tx.note)
        )
        await db.commit()
    return {"ok": True}
