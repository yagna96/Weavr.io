import pandas as pd 
import random as rand 
from datetime import timedelta,datetime


def create_transaction_time_table(data_path):
     transaction =  pd.read_excel(data_path, sheet_name ='TRANSACTION')
     transact_time = transaction[['TRANSACTION_ID','CREATION_TIMESTAMP']]
     transact_time['END_TIMESTAMP'] = transact_time['CREATION_TIMESTAMP'].apply(lambda x: x+rand.randint(0,6000))
     return transact_time

def create_time_offset(row):
     if row == 1:
          start_date = datetime.now()
     else:
          start_date = datetime.now()-pd.DateOffset(months=3)      
     time_stamp = start_date - timedelta(days = rand.randint(0,90))
     return time_stamp
          
def create_card_activity(data_path):
     card_account = pd.read_excel(data_path, sheet_name ='CARD_ACCOUNT')
     card_activity = card_account[['CARD_ACCOUNT_ID','USER_ID','FRIENDLY_NAME','IS_ACTIVE']]
     card_activity['LAST_USE'] = card_activity['IS_ACTIVE'].apply(create_time_offset )
     return card_activity







