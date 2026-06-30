import requests

LOG_URL = "http://4.224.186.213/evaluation-service/logs"

def log(stack, level, package, message, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    try:
        response = requests.post(LOG_URL, json=data, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}