from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo
import os

app = Flask(__name__)

@app.route("/")
def home():
    ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    return render_template(
        "index.html",
        app_name="""Cloud CI/CD "Fully-Automated" App (New) hosted in the cloud service provider platform""",
        version=os.getenv("APP_VERSION", "1.0"),
        deployed_at=ist_time.strftime("%Y-%m-%d %H:%M:%S IST"),
        environment="Google Cloud Run"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)