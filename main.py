import pandas as pd
import json
from time import sleep
from twilio.rest import Client

account_sid = 'AC49bafda8488b7bd9ae75c7df76f8341e'
auth_token = '1a5f3b6b04fed50aa51355c7243775f5'
client = Client(account_sid, auth_token)

df = pd.read_excel('birthdays.xlsx', parse_dates=['Date Of Birth'])

if "Test" in df.columns:
    test_rows = df[df["Test"] == True]
else:
    print("No 'Test' column found. Using all rows for testing.")
    test_rows = df

test_iterations = 1

for i in range(test_iterations):
    for index, row in test_rows.iterrows():
        name = row["Name"]
        mobile = row["Mobile"]

        content_vars = json.dumps({"person": name})
        
        try:
            message = client.messages.create(
                from_='whatsapp:+14155238886',  
                to=f'whatsapp:{mobile}',  
                content_sid='HXef62361731273ee6f2c29e67b052c01d', 
                content_variables=content_vars
            )
            print(f"Sent test reminder for {name}. Message SID: {message.sid}")
        except Exception as e:
            print(f"Error sending message to {name} at {mobile}: {e}")
    
    sleep(10)