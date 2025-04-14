from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google # type: ignore
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Replace with your own secret key

# Google OAuth Setup
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Allow HTTP for localhost
google_bp = make_google_blueprint(
    client_id="",
    client_secret="",
    redirect_to="welcome"
)
app.register_blueprint(google_bp, url_prefix="/login")

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/welcome")
def welcome():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    user_info = resp.json()
    return f"Hello, {user_info['name']}! You are logged in with Google."

@app.route("/login/google/authorized")
def authorized_debug():
    return "You're at the authorized route."

if __name__ == "__main__":
    app.run(debug=True)

