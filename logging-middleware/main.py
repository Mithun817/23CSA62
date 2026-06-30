from fastapi import FastAPI
from logger import log

app = FastAPI()

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJtaXRodW5fMjNjc2E2MkBrZ2tpdGUuYWMuaW4iLCJleHAiOjE3ODI4MDA5MDcsImlhdCI6MTc4MjgwMDAwNywiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImQ4ZTZiNmNmLThkMjQtNDFiYi05ZTY2LTBmMzQ5MmMwYTlhZSIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6Im1pdGh1biByIiwic3ViIjoiMzE5NWVlMjktOGNmNS00YzMzLTg5ZDYtYTQ5NDczYTExNTU3In0sImVtYWlsIjoibWl0aHVuXzIzY3NhNjJAa2draXRlLmFjLmluIiwibmFtZSI6Im1pdGh1biByIiwicm9sbE5vIjoiMjNjc2E2MiIsImFjY2Vzc0NvZGUiOiJXak55Q1QiLCJjbGllbnRJRCI6IjMxOTVlZTI5LThjZjUtNGMzMy04OWQ2LWE0OTQ3M2ExMTU1NyIsImNsaWVudFNlY3JldCI6IkV0QmpLakJIWVV6QXdOenQifQ.gsph3P_DIzJPGWi9jCudllcVGoYVlZtxlP6LXkxVnjY"

@app.get("/")
def home():
    log(
        "backend",
        "info",
        "route",
        "Home endpoint accessed",
        ACCESS_TOKEN
    )

    return {"message": "Server Running"}

@app.get("/test")
def test():
    result = log(
        "backend",
        "debug",
        "handler",
        "Testing logging middleware",
        ACCESS_TOKEN
    )

    return result