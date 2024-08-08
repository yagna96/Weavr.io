
import pandas as pd 
from datetime import datetime

data_path = 'data/sample-files.xlsx'

def time_transformations(df):
    df['DATE'] = pd.to_datetime(df['CREATION_TIMESTAMP'], unit ='s')
    df['DAY']= df['DATE'].dt.day
    df['MONTH']= df['DATE'].dt.month 
    df['YEAR']= df['DATE'].dt.year 
    df['TIME']=df['DATE'].dt.time

def transform_user_profile(data_path):
    user_profile = pd.read_excel(data_path, sheet_name ='USER')
    # date transformations converting unix into datetime 
    user_profile = time_transformations(user_profile)
    # find null values in user_id to drop them  
    # considering it primary key for sql table
    user_profile = user_profile.dropna(subset =['USER_ID'])
    #combining first and last names 

def transform_bank_account(data_path):
    bank_account = pd.read_excel(data_path, sheet_name ='BANK_ACCOUNT')
    # bank account and user id should be non null 
    bank_account = bank_account.dropna(subset=['BANK_ACCOUNT_ID','USER_ID'])
    # (bank accountid, user id) need to be unique 
    bank_account =bank_account.drop_duplicates(subset=['BANK_ACCOUNT_ID','USER_ID'])
    bank_account = time_transformations(bank_account)

def transform_card_account(data_path):
    card_account = pd.read_excel(data_path, sheet_name ='CARD_ACCOUNT')
    # card account and user id should be non null 
    card_account = card_account.dropna(subset=['CARD_ACCOUNT_ID','USER_ID'])
    # (card accountid, user id) need to be unique 
    card_account=card_account.drop_duplicates(subset=['CARD_ACCOUNT_ID','USER_ID'])
    accepted_card_types= ['VIRTUAL','PHYSICAL']
    card_account =card_account['CARD_TYPE'].isin(accepted_card_types)
    card_account = time_transformations(card_account)

def tarnsform_transaction(data_path):
    transaction = pd.read_excel(data_path, sheet_name ='TRANSACTION')
    # card account and user id should be non null 
    card_account = card_account.dropna(subset=['CARD_ACCOUNT_ID','USER_ID'])
    # (card accountid, user id) need to be unique 
    card_account=card_account.drop_duplicates(subset=['CARD_ACCOUNT_ID','USER_ID'])
    accepted_card_types= ['VIRTUAL','PHYSICAL']
    card_account =card_account['CARD_TYPE'].isin(accepted_card_types)
    card_account = time_transformations(card_account)




