from database import SessionLocal
from models import Log
from datetime import datetime, timedelta
def detect_bruteforce():
    db = SessionLocal()

    time_window = datetime.utcnow() - timedelta(minutes=2)
    
    logs = db.query(Log).filter(
        Log.action =="login",
        Log.status == "fail",
        Log.timestamp >= time_window
    ).all()

    db.close()
    if len(logs) > 5:
        return True
    return False