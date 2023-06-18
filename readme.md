
## Sample data
 {"auth-token": "PRO1","key": "XXX","value": "33200","key1": "Close","value1": "28099.9","key2": "Strategy","value2": "TT_STREND","key3": "Ticker","value3": "BTCUSDT30M2023"}

## Insomnia
POST http://localhost:5000/webhook

Open Insomnia console and send text like below:
{"auth-token": "PRO1","key": "XXX","value": "33200","key1": "Close","value1": "28099.9","key2": "Strategy","value2": "TT_STREND","key3": "Ticker","value3": "BTCUSDT30M2023"}


## How to run Flask webserver
cd trading-webhook
SET FLASK_APP=app.py
or
export FLASK_APP=app.py 

flask run
or
flask run --host=0.0.0.0 --port=8080
It will listen on http://127.0.0.1:5000 or http://localhost:5000
or
<ip address>:8080

## EC2 setup
make sure port 8080 is open.

## setup env
git config --global user.name "ivnaas"
git config --global user.email ivnaas.group@gmail.com 
ssh-keygen
cat /home/ec2-user/.ssh/id_rsa.pub
mkdir gitrepo
cd gitrepo
git clone -b master git@github.com:ivnaas/trading-webhook.git
cd trading-webhook/
