"""FastAPI 后端示例 — 与报告 §7.1 对应（PoC）"""
from fastapi import FastAPI
import sqlite3

app = FastAPI(title="AI Intelligence Radar API")


@app.get("/api/v1/daily_insights")
async def get_daily_insights():
    conn = sqlite3.connect("ai_radar.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, url, innovation, eng_value
        FROM insights
        WHERE status = '未处理'
        ORDER BY created_at DESC LIMIT 10
        """
    )
    records = cursor.fetchall()
    conn.close()
    return {
        "code": 200,
        "data": [
            {"title": r[0], "url": r[1], "innovation": r[2], "eng_value": r[3]}
            for r in records
        ],
    }
