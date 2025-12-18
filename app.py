from flask import Flask, render_template, request, redirect, session
from db import get_db




app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/")
def index():
    q = request.args.get("q", "")
    category = request.args.get("category")
    price = request.args.get("price")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    sql = "SELECT * FROM products WHERE name LIKE %s"
    params = [f"%{q}%"]

    if category:
        sql += " AND category=%s"
        params.append(category)

    if price:
        sql += " AND price <= %s"
        params.append(price)

    cursor.execute(sql, params)
    products = cursor.fetchall()

    return render_template("index.html", products=products)

@app.route("/product/<int:id>")
def product(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()

    cursor.execute("SELECT * FROM reviews WHERE product_id=%s", (id,))
    reviews = cursor.fetchall()

    return render_template("product.html", product=product, reviews=reviews)

@app.route("/add-to-cart/<int:id>")
def add_to_cart(id):
    cart = session.get("cart", {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    session["cart"] = cart
    return redirect("/cart")

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    db = get_db()
    cursor = db.cursor(dictionary=True)

    items = []
    total = 0

    for pid, qty in cart.items():
        cursor.execute("SELECT * FROM products WHERE id=%s", (pid,))
        product = cursor.fetchone()
        product["qty"] = qty
        product["subtotal"] = qty * product["price"]
        total += product["subtotal"]
        items.append(product)

    return render_template("cart.html", items=items, total=total)

@app.route("/checkout")
def checkout():
    session.pop("cart", None)
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=24537, debug=True)



import db
print(db.__file__)
