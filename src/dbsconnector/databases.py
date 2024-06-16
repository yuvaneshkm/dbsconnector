# importing necessary libraries
import pandas as pd
from pymongo.mongo_client import MongoClient
from typing import List, Dict
from pathlib import Path

# load csv file:
def load_csv(filepath:Path, delimiter:str):
    filepath = Path(filepath)
    return pd.read_csv(str(filepath), delimiter=delimiter)
    
# load excel sheet
def load_excelsheet(filepath:Path, sheet_name:str):
    filepath = Path(filepath)
    return pd.read_excel(str(filepath), sheet_name=sheet_name)

# load google sheet 
def load_gsheet(gsheet_id:str, sheet_name:str):
    base_url = 'https://docs.google.com/spreadsheets/d'
    sheet_csv = 'gviz/tq?tqx=out:csv&sheet='
    url = f'{base_url}/{gsheet_id}/{sheet_csv}{sheet_name}'
    return pd.read_csv(url)

# load mongodb data:
def load_mongodbdata(host:str, database:str, collection:str):
    client: MongoClient = MongoClient(host)
    db = client[database]
    col = db[collection]
    records = col.find()
    data: List[Dict] = list(records)
    df = pd.DataFrame(data)
    df.drop('_id', axis=1, inplace=True)
    return df
