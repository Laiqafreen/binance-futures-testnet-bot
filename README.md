# Binance Futures Testnet Trading Bot

## Overview
A modular CLI-based trading bot built in Python that connects to Binance Futures Testnet.

## Features
- MARKET order execution
- LIMIT order execution
- Input validation
- Logging system
- Environment variable security
- Timestamp synchronization

## Tech Stack
- Python 3.13
- python-binance
- python-dotenv

## Installation

1. Clone repository
2. Create virtual environment:
   python -m venv .venv
3. Activate:
   .venv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Add .env file with:

   BINANCE_API_KEY=your_key
   BINANCE_API_SECRET=your_secret

## Usage

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
## Sample Output

Example Market Order Response:

{
  "orderId": 12439001007,
  "symbol": "BTCUSDT",
  "status": "NEW",
  "type": "MARKET",
  "side": "BUY"
}