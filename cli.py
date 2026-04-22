import sys
from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

setup_logger()

def get_input(prompt, validator=None):
    while True:
        value = input(prompt)
        try:
            if validator:
                validator(value)
            return value
        except Exception as e:
            print(f"❌ {e}")

def main():
    print("\n Welcome to Trading Bot")
    print("---------------------------")

    symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()

    side = get_input("Enter Side (BUY/SELL): ", validate_side)

    order_type = get_input("Enter Order Type (MARKET/LIMIT): ", validate_order_type)

    quantity = get_input("Enter Quantity: ", validate_quantity)

    price = None
    if order_type == "LIMIT":
        price = get_input("Enter Price: ")

    client = get_client()

    print("\n Order Summary:")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")

    confirm = input("\nConfirm Order? (y/n): ")

    if confirm.lower() != "y":
        print("❌ Order Cancelled")
        sys.exit()

    try:
        order = place_order(client, symbol, side, order_type, quantity, price)

        print("\n✅ Order Successful!")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order['executedQty']}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()