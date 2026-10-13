from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="PigeonPost API")

# База данных в памяти (для простоты)
pigeons_db = {}
pigeon_id_counter = 0

class PigeonCreate(BaseModel):
    name: str
    speed_kmh: float
    
    class Config:
        # Для pydantic v1 это нужно, чтобы работать с FastAPI корректно
        orm_mode = True

@app.get("/")
def root():
    return {"message": "🐦 PigeonPost API is alive!", "status": "голуби на базе"}

@app.post("/api/v1/pigeons")
def create_pigeon(pigeon: PigeonCreate):
    global pigeon_id_counter
    pigeon_id_counter += 1
    new_pigeon = {
        "id": pigeon_id_counter,
        "name": pigeon.name,
        "speed_kmh": pigeon.speed_kmh,
        "status": "отдыхает"
    }
    pigeons_db[pigeon_id_counter] = new_pigeon
    return new_pigeon

@app.get("/api/v1/pigeons/{pigeon_id}")
def get_pigeon(pigeon_id: int):
    if pigeon_id not in pigeons_db:
        raise HTTPException(status_code=404, detail="Голубь улетел и не вернулся 🕊️💨")
    return pigeons_db[pigeon_id]