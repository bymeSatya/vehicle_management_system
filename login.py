import streamlit
import pandas
import requests
# import setuptools
#import snowflake.connector

streamlit.title('User Login')

timer = 10

# Create a function that will be called every second
def count_down():
  # Decrement the timer by 1
  timer -= 1

  # Update the timer text
  st.write(f"Time remaining: {timer} seconds")

  # If the timer has reached zero, stop counting
  if timer == 0:
    return

# Start the timer
asyncio.run(periodic(count_down, 1))
