from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import agents, finance

app = FastAPI(title="Palmafin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents.router, prefix="/api/agents")
app.include_router(finance.router, prefix="/api/finance")

@app.get("/health")
def health():
    return {"status": "ok"}
