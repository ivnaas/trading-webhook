
## Sample data
 {"auth-token": "PRO1","key": "XXX","value": "33200","key1": "Close","value1": "28099.9","key2": "Strategy","value2": "TT_STREND","key3": "Ticker","value3": "BTCUSDT30M2023"}

## Insomnia
POST http://localhost:5000/webhook

Open Insomnia console and send text like below:
{"auth-token": "PRO1","key": "XXX","value": "33200","key1": "Close","value1": "28099.9","key2": "Strategy","value2": "TT_STREND","key3": "Ticker","value3": "BTCUSDT30M2023"}


## How to run Flask webserver
cd trading-webhook
SET FLASK_APP=app.py
flask run
It will listen on http://127.0.0.1:5000 or http://localhost:5000



