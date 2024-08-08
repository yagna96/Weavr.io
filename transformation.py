from sourcing import *
import pandas as pd 
from datetime import datetime




user_profile['DATE'] = pd.to_datetime(user_profile['CREATION_TIMESTAMP'], unit ='s')
user_profile['DAY']= user_profile['DATE'].dt.day
user_profile['MONTH']= user_profile['DATE'].dt.month 
user_profile['YEAR']= user_profile['DATE'].dt.year 
user_profile['TIME']=user_profile['DATE'].dt.time