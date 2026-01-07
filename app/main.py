from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name="Cloud CI/CD App hosted in the cloud service provider platform",
        version=os.getenv("APP_VERSION", "1.0"),
        deployed_at=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S IST"),
        environment="Google Cloud Run"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)