## General Information

This is a program which helps people to to do statistical calculations and drawings via the values retrieving by external sources(in version 1.0.0 only binance is available as external source) or using manuel imports.I would want to say that some ready files(these are the informations retrieved by exchange market:iotausdt.json,hbarusdt.json,btcusdt.json,ethusdt.json and xmrusdt.json . Also one excel file is included as an example for outputting json data to excel.) to do experimental data analysis are also included and you can convert datas getten by binance into excel format. 
It is in version 1.0.0 for the moment and some big improvements will be realesed to this application sooner. Some of them are t-contribution(to do estimation using samples defined on the normal curves),alpha vintage and also artificial learning algorithms.
I would be glad if you open an issue in case you remarked any bugs🙂

## RUN

python main.py


## How to get data from Binance 

First of all you have to get an api_key and api_secret from binance(click profil icon than api management section) than you have to add your api_key and api secret on config.json .

structure
{
    "api_key" :  "your_api_key"
    ,"api_secret":"your_api_secret"
}

When you do this operation you can easily get data from Binance via this application.

## TOOL SETUP

# Install Python dependencies

Run the following line in the terminal: pip install -r requirements.txt.

## REQUIREMENTS ```

# Modules:

[python-binance2==1.0.13,
openpyxl==3.0.9,
pandas==1.3.3,
numpy==1.21.2,
matplotlib==3.4.3,
pyfiglet==0.8.post1]

# Python Version

python>=3.x ```

## Support the Project

XMR:83sZZZuU6rKSzzYbsEJCqTH5Rk7xrvjZi8sqPUfbD8XUKutUqkegQx9aNwfXfrggEw9g2K7QEqNVP5Kz8Vtq7oCXV1Aiyer