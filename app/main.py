from fastapi import FastAPI

from app.parser import extract_ips
from app.detector import detect_bruteforce

app = FastAPI(
    title="Cyber Log Analyzer"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "Cyber Log Analyzer"
    }

@app.get("/alerts")
def alerts():

    ips = extract_ips("logs/sample_auth.log")

    return detect_bruteforce(
        ips,
        threshold=5
    )