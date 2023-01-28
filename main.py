import requests
import datetime                     #. Date aquiring
import pytz                         #. Time Zone Management
import pandas as pd                 #..Data frame manipulation & used to analyze data
import MetaTrader5 as mt5                 #. Importing OHLC data
import numpy as np                  #. Array Manipulation
from math import floor
from termcolor import colored as cl
import matplotlib.pyplot as plt     #. Plotting charts
import plotly.express as px

plt.rcParams['figure.figsize'] = (20, 10)
plt.style.use('fivethirtyeight')

account = int(78519565)
password = "moreP789"
server = "Exness-MT5Trial7"

if not mt5.initialize(login=account, password=password, server=server):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
authorized=mt5.login(account, password=password, server=server)

if authorized:
    print(mt5.account_info())
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
