from bot.client import BinanceFuturesClient
from bot.validators import validate_order
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        client = BinanceFuturesClient()

        order_data = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_data["price"] = price
            order_data["timeInForce"] = "GTC"

        logger.info(f"Placing order: {order_data}")

        response = client.create_order(order_data)

        logger.info(f"Order response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}