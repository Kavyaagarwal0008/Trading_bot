#  Trading Bot (Binance Futures Testnet Simulation)

##  Overview
This project is a simplified trading bot built in Python that simulates placing orders on Binance Futures Testnet.

It supports MARKET and LIMIT orders with a clean CLI interface, structured codebase, logging, and proper error handling.

Due to API key generation limitations, a mock execution mode is implemented. The architecture is designed such that real Binance API integration can be added بسهولة.

---

##  Features

###  Core Features
- Place MARKET and LIMIT orders
- Support BUY and SELL sides
- CLI-based user input
- Input validation and error handling
- Structured and modular code
- Logging of order requests and responses

###  Bonus Feature (Enhanced CLI UX)
- Interactive prompts instead of command-line flags
- Input validation with retry
- Order confirmation before execution

---

##  Project Structure

trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py            # Mock client
│   ├── orders.py            # Order execution logic
│   ├── validators.py        # Input validation
│   └── logging_config.py    # Logging setup
│
├── cli.py                   # Main CLI application
├── trading_bot.log          # Log file (generated after run)
├── requirements.txt
└── README.md
---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download Project
git clone <[Repo-Link](https://github.com/Kavyaagarwal0008/Trading_bot)>
cd trading_bot

### 2️⃣ Install Dependencies
pip install -r requirements.txt


*(Note: This project uses standard Python libraries only)*
---
##  How to Run

Run the CLI application:
python cli.py

---

##  Example Execution
Welcome to Trading Bot

Enter Symbol (e.g., BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Order Type (MARKET/LIMIT): MARKET
Enter Quantity: 0.01

Confirm Order? (y/n): y

###  Output
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

 Order Successful!
Order ID: 54321
Status: FILLED
Executed Qty: 0.01
Avg Price: 27450.23

---

##  Logging

All API requests, responses, and errors are logged in:
trading_bot.log
2026-04-22 12:00:00 - INFO - Order Request: BTCUSDT BUY MARKET 0.01
2026-04-22 12:00:01 - INFO - Order Response: {...}

##  Author
Kavya Agarwal || kavyaagarwal580@gmail.com

---

##  Note
This project is developed as part of the Primetrade.ai hiring task.

Mock execution is used due to API constraints, but the system is fully designed for real-world API integration.
