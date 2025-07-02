import requests

API_BASE = "http://localhost:5000"  # Change if deploying Flask elsewhere

def send_otp(email):
    try:
        response = requests.post(f"{API_BASE}/send-otp", json={"email": email})
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def verify_otp(email, otp):
    try:
        response = requests.post(f"{API_BASE}/verify-otp", json={"email": email, "otp": otp})
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def log_input(email, message, password):
    try:
        response = requests.post(f"{API_BASE}/log-input", json={
            "email": email,
            "message": message,
            "password": password
        })
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}
