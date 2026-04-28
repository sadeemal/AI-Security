from flask import Flask
from database import SessionLocal
from models import Log
from detectionsys import detect_bruteforce
app = Flask(__name__)

def log_event(user_id, action, status, ip="127.0.0.1"):
    db = SessionLocal()
    log = Log(
        user_id=user_id, 
        action=action, 
        status=status, 
        ip=ip
    )
    db.add(log)
    db.commit()
    db.close()

@app.route('/')
def home():
    return "Backend Running!!!"

@app.route('/login')
def login():
    # simulate login
    log_event(user_id=1, action="login", status="fail")
    return "Login Attempt Logged*!*"
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/login')
def login():
    log_event(user_id=1, action="login", status="fail")

    if detect_bruteforce():
        print("Detected Brute Force!!!")
    
    return "Login Attempt Logged"
