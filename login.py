import streamlit as st
import pandas
import requests
# import setuptools
#import snowflake.connector

#streamlit.title('User Login')

import datetime,pytz,time

dtobj1=datetime.datetime.utcnow()   #utcnow class method
print(dtobj1)

dtobj3=dtobj1.replace(tzinfo=pytz.UTC) #replace method


#print(pytz.all_timezones) => To see all timezones
for i in range(1,100):
  dtobj_india=dtobj3.astimezone(pytz.timezone("Asia/Calcutta")) #astimezone method
  st.write(dtobj_india)
  time.sleep(i*60)

