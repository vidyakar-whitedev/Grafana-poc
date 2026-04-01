import requests
import psycopg2
import time

TOKEN = "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"
REPO = "vidyakar-whitedev/Grafana-poc"

DB_CONFIG = {
    "dbname": "github",
    "user": "postgres",
    "password": "postgres",
    "host": "db"
}

def fetch_and_store():
    url = f"https://api.github.com/repos/{REPO}/actions/runs"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for run in data.get("workflow_runs", []):
        cur.execute("""
            INSERT INTO github_actions (workflow_name, status, conclusion, created_at)
            VALUES (%s, %s, %s, %s)
        """, (
            run["name"],
            run["status"],
            run["conclusion"],
            run["created_at"]
        ))

    conn.commit()
    cur.close()
    conn.close()

while True:
    fetch_and_store()
    time.sleep(300)  # every 5 mins
