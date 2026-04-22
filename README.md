Binance Testnet Trading Bot

This is a simple CLI based trading bot built in Python using Binance Testnet.
The idea was to keep things clean and understandable while covering the basic requirements like placing orders, validating inputs and logging.

-What it does

* Lets you place MARKET and LIMIT orders
* Works for both BUY and SELL
* Takes input from command line
* Checks inputs before sending request
* Shows clear output in terminal
* Logs everything (requests, responses, errors)



-Project structure

trading_bot/
bot/
client.py
orders.py
validators.py
logging_config.py
cli.py


-Setup

1. Clone the repo

git clone https://github.com/YOUR_USERNAME/trading-bot-binance-testnet.git
cd trading-bot-binance-testnet

2. Create virtual environment

python -m venv venv
venv\Scripts\activate

3. Install requirements

pip install -r requirements.txt

4. Add API keys

Create a .env file and add:

API_KEY=your_api_key
API_SECRET=your_api_secret

---

-How to run

Market order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000


-Output

It prints:

* what order you are placing
* basic details like symbol, type, quantity
* response from Binance (order id, status etc)
* error message if something fails


-Logging

A file named trading_bot.log gets created.

It stores:

* order requests
* API responses
* errors


- Sample logs

I have tested both:

* one MARKET order
* one LIMIT order

and logs are generated in the log file.



- Assumptions

* Using Binance testnet only (no real money)
* Only basic order types are implemented
* Inputs are given manually through CLI


- Final

This was built as a simple and structured implementation of a trading bot using CLI.
Focus was more on clean code and handling edge cases properly.
