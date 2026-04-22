import logging
import random
import time

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Order Request: {symbol} {side} {order_type} {quantity} {price}")

        # simulate API delay
        time.sleep(1)

        if order_type == "MARKET":
            status = "FILLED"
            avg_price = round(random.uniform(25000, 30000), 2)

        elif order_type == "LIMIT":
            status = "NEW"
            avg_price = price

        order = {
            "orderId": random.randint(10000, 99999),
            "status": status,
            "executedQty": quantity,
            "avgPrice": avg_price
        }

        logging.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise