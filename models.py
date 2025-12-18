from flask import session

def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session["cart"] = cart

def cart_count():
    return sum(session.get("cart", {}).values())
