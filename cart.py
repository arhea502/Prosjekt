from flask import Blueprint, session, redirect, url_for, render_template

cart = Blueprint('cart', __name__)

@cart.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = {}
    session["cart"][str(product_id)] = session["cart"].get(str(product_id), 0) + 1
    return redirect(url_for("index"))

@cart.route("/cart")
def cart_page():
    return render_template("cart.html")
