def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")
    
    if symbol!= symbol.upper():
        raise ValueError("Symbol must be uppercase.")
    
def validate_side(side):
    if side != "BUY" and side != "SELL":
        raise ValueError("Side should be BUY or SELL.")

def validate_order_type(order_type):
    if order_type != "MARKET" and order_type != "LIMIT":
        raise ValueError("Order type should be MARKET or LIMIT.")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be > 0")

def validate_price(order_type, price):
    if order_type == "LIMIT" and (price <= 0 or price is None):
        raise ValueError("Enter a valid price ")
    