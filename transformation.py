"""
Script that transform the sample data file into various csv file . Csv files are stored in Result folder 
"""
import pandas as pd 
from datetime import datetime
from sourcing import create_card_activity,create_transaction_time_table

data_path = 'data/sample-files.xlsx'


def transform_user_profile(data_path :str):
    """
    Function to transform user profile 
    """
    user_profile = pd.read_excel(data_path, sheet_name ='USER')
    # find null values in user_id to drop them  
    # considering it primary key for sql table
    user_profile = user_profile.dropna(subset =['USER_ID'])
    #combining first and last names 
    user_profile.to_csv('Result/user_profile.csv')

def transform_bank_account(data_path :str):
    """
    Function to transform bank account 
    """
    bank_account = pd.read_excel(data_path, sheet_name ='BANK_ACCOUNT')
    # bank account and user id should be non null 
    bank_account = bank_account.dropna(subset=['BANK_ACCOUNT_ID','USER_ID'])
    # (bank accountid, user id) need to be unique 
    bank_account =bank_account.drop_duplicates(subset=['BANK_ACCOUNT_ID','USER_ID'])
    bank_account.to_csv('Result/bank_account.csv')

def transform_card_account(data_path :str):
    """
    Function to transform card account 
    """
    card_account = pd.read_excel(data_path, sheet_name ='CARD_ACCOUNT')
    # card account and user id should be non null ss
    card_account = card_account.dropna(subset=['CARD_ACCOUNT_ID','USER_ID'])
    # (card accountid, user id) need to be unique 
    card_account=card_account.drop_duplicates(subset=['CARD_ACCOUNT_ID','USER_ID'])
    accepted_card_types= ['VIRTUAL','PHYSICAL']
    card_account =card_account[card_account['CARD_TYPE'].isin(accepted_card_types)]
    card_account.to_csv('Result/card_account.csv')

def transform_transaction(data_path :str):
    """
    Function to transform transaction data
    """
    transaction = pd.read_excel(data_path, sheet_name ='TRANSACTION')
    transaction.rename(columns={'CREATION TIMESTAMP':'CREATION_TIMESTAMP'})
    # card account and account id should be non null 
    transaction = transaction.dropna(subset=['TRANSACTION_ID','ACCOUNT_ID'])
    # (card accountid, account id) need to be unique 
    transaction=transaction.drop_duplicates(subset=['TRANSACTION_ID','ACCOUNT_ID'])
    # checking acceptable values 
    accepted_transaction_types= ['SETTLEMENT','DEPOSIT']
    transaction =transaction[transaction['TRANSACTION_TYPE'].isin(accepted_transaction_types)]
    transaction.to_csv('Result/transactions.csv')

def save_transaction_time(data_path :str):
    """
    Function to save transaction duration data
    """
    transaction_time =create_transaction_time_table(data_path)
    transaction_time.to_csv('Result/transactions_time.csv')

def save_card_activity(data_path :str):
    """
    Function to save card activity data
    """
    card_activity = create_card_activity(data_path)
    card_activity.to_csv('Result/card_activity.csv')


save_card_activity(data_path=data_path)
save_transaction_time(data_path=data_path)
transform_transaction(data_path=data_path)
transform_card_account(data_path=data_path)
transform_bank_account(data_path=data_path)
transform_user_profile(data_path=data_path)
user_state= pd.read_excel(data_path, sheet_name ='USER_STATE')
user_state.to_csv('Result/user_state.csv')





