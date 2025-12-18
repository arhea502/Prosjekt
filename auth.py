from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

auth = Blueprint('auth', __name__)
login_manager = LoginManager()

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MARIA_PASSWORD",
        database="Nettbutikk"
    )

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    if user:
        return User(user['id'], user['username'])
    return None

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        db.close()
        if user and password == user['password']:  # plaintext for now
            login_user(User(user['id'], user['username']))
            return redirect(url_for('admin.dashboard'))
        else:
            flash("Invalid username or password")
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
