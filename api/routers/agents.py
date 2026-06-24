from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/status")
def get_agents_status():
    return {
        "agents": [
            {
                "id": "garant",
                "name": "Architect Garant",
                "island": "Остров Сделок",
                "emoji": "🤝",
                "emotion": "Радость",
                "status": "active",
                "stats": {
                    "weekly_usdt": 0,
                    "active_deals": 0,
                    "arbitrage": 0,
                },
                "github": "https://github.com/SandraNola1/architect-garant"
            },
            {
                "id": "vpn",
                "name": "Nord1x VPN",
                "island": "Остров Защиты",
                "emoji": "🔒",
                "emotion": "Рост",
                "status": "active",
                "stats": {
                    "active_subs": 0,
                    "monthly_rub": 0,
                    "expiring_soon": 0,
                },
            },
            {
                "id": "moon",
                "name": "Мун бот",
                "island": "Остров Тайны",
                "emoji": "🌙",
                "emotion": "Вера",
                "status": "pending_payment",
                "stats": {
                    "users": 0,
                    "readings_today": 0,
                    "monthly_rub": 0,
                },
                "github": "https://github.com/SandraNola1/moon-bot"
            },
            {
                "id": "content",
                "name": "RelContent",
                "island": "Остров Творчества",
                "emoji": "🎬",
                "emotion": "Вкус",
                "status": "active",
                "stats": {
                    "weekly_reach": 0,
                    "reels_published": 0,
                    "pending_approval": 0,
                },
            },
        ],
        "updated_at": datetime.utcnow().isoformat()
    }
