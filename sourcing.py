
"""
- Script is used for data enrichment.
- Created crad activity infomation including last_use as column to monitor card activity for both active and in active users
- Created transactions duration data  to monitor settlement cycle time 

"""


import pandas as pd 
import random as rand 
from datetime import timedelta,datetime


def create_transaction_time_table(data_path :str) -> pd.DataFrame:
     """
     Function that generates dataframe which has transaction_id , creation_timesatmp and end_timestamp
     """
     transaction =  pd.read_excel(data_path, sheet_name ='TRANSACTION')
     transact_time = transaction[['TRANSACTION_ID','CREATION_TIMESTAMP']]
     transact_time['END_TIMESTAMP'] = transact_time['CREATION_TIMESTAMP'].apply(lambda x: x+rand.randint(0,6000))
     return transact_time

def create_time_offset(row : pd.Series):
     """
     Function returns random date from past 3 months for active users 
     returns random date from past 6 months for inactive users  
     """
     if row == 1:
          start_date = datetime.now()
     else:
          start_date = datetime.now()-pd.DateOffset(months=3)      
     time_stamp = start_date - timedelta(days = rand.randint(0,90))
     return time_stamp
          
def create_card_activity(data_path :str)-> pd.DataFrame:
     """
     Function creates dataframe which has card_account_id,user_id,friendly_name,is_active,last_use.
     """
     card_account = pd.read_excel(data_path, sheet_name ='CARD_ACCOUNT')
     card_activity = card_account[['CARD_ACCOUNT_ID','USER_ID','FRIENDLY_NAME','IS_ACTIVE']]
     card_activity['LAST_USE'] = card_activity['IS_ACTIVE'].apply(create_time_offset )
     return card_activity







