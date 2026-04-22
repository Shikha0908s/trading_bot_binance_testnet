import logging
from bot.logging_config import setup_logger

setup_logger()
from bot.client import get_client
def place_market_order(symbol, side, quantity):
    client = get_client()
    try:
        logging.info(f"Placing MARKET order: {symbol} {side} {quantity}")

        order = client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Order Response: {order}")

        print("Market order placed")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order['executedQty']}")

    except Exception as e:
        logging.error(f"Market Order Failed: {str(e)}")

        print("Error placing order:")
        print(e)


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        logging.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")

        order = client.create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=str(price),
            timeInForce="GTC"
        )

        logging.info(f"Order Response: {order}")

        print("Limit order placed")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Price: {price}")

    except Exception as e:
        logging.error(f"Limit Order Failed: {str(e)}")
        print("Error placing order:")
        print(e)