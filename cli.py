from bot.orders import place_market_order, place_limit_order
import argparse
from bot.client import get_client
from bot.validators import (validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", dest="order_type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, )
    args = parser.parse_args()

    try:
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.order_type)
        validate_quantity(args.quantity)
        validate_price(args.order_type, args.price)
        print("Input is fine, connecting...")
        client = get_client()

        # account = client.get_account()
        
        # print("\n Your Balance:\n")
        # for  coin in account.get("balances",[]):
        #     available = float(coin.get("free",0))

        #     if available > 0:
        #         print(f"{coin['asset']}: {available:.2f}")
        print("Order Request")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.order_type}")
        print(f"Quantity: {args.quantity}")

        if args.order_type == "LIMIT":
            print(f"Price: {args.price}")

        if args.order_type == "MARKET":
            place_market_order(args.symbol, args.side, args.quantity)

        elif args.order_type == "LIMIT":
            place_limit_order(args.symbol, args.side, args.quantity, args.price)
    except Exception as e:
        print("connection failed")
        print("Error",str(e))

if __name__ == "__main__":
    main()