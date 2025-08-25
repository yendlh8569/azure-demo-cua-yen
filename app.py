from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Azure Web App! 🚀"

if __name__ == "__main__":
    # Chạy local để test; khi lên Azure sẽ chạy bằng gunicorn
    app.run(host="0.0.0.0", port=8000)
