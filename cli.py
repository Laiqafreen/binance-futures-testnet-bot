import argparse
from bot.orders import place_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\n===== ORDER RESPONSE =====")
    print(response)

if __name__ == "__main__":
    main()