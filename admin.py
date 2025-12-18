from flask import Blueprint, render_template
from flask_login import login_required
import mysql.connector

admin = Blueprint('admin', __name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="arian",
        password="gamemode c",
        database="Nettbutikk"
    )

@admin.route("/admin")
@login_required
def dashboard():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("admin.html", products=products)
