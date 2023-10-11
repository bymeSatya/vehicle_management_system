import streamlit as st
import pandas
import requests
# import setuptools
#import snowflake.connector

#streamlit.title('User Login')

import datetime,pytz

dtobj1=datetime.datetime.utcnow()   #utcnow class method
print(dtobj1)

dtobj3=dtobj1.replace(tzinfo=pytz.UTC) #replace method


#print(pytz.all_timezones) => To see all timezones
dtobj_india=dtobj3.astimezone(pytz.timezone("Asia/Calcutta")) #astimezone method
print(dtobj_india)

