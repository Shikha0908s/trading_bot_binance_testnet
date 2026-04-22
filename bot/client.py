from time import time
from xmlrpc import client

from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv() # loading api from .env

def get_client():
    """
    create and return a Binance Futures Testnet client.
    """
    api_key =os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API Credentials not found. check your .env file.")
    
    client = Client(api_key=api_key, api_secret=api_secret)

    # ensure we are using futures testnet (not real trading)
    client.API_URL = "https://testnet.binance.vision/api"

    client = Client(api_key, api_secret, testnet=True)
    client.API_REQUEST_TIMEOUT = 30
    client.timestamp_offset = client.get_server_time()['serverTime'] - int(time.time() * 1000)

    return client