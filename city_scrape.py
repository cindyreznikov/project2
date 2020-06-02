# Dependencies
import requests
import json
import gmaps
import pandas as pd
# from config import api_key gkey
from pprint import pprint

# read csv file
file="./data/charity_data.csv"
cities_data_df=pd.read_csv(file)
cities_data_df.count()