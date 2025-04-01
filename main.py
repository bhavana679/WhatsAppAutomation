from twilio.rest import Client
from datetime import datetime,timedelta
import time 

account_sid = 'AC92197cd372120d87f3089fa253ee70dc'
account_token = '0b4b3c535ea1fec018a99862a34e8819'

client = Client(account_sid, account_token)
def send_whatsapp_message(recipient_number,message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to='whatsapp:+91'+recipient_number
        )
        print("Message sent successfully"+"messsage SID:"+message.sid)
    except Exception as e:
        print("Error occured while sending message",e)

name = input("Enter Recipient's name:")
recipient_number = input("Enter recipient whatsapp number:") 
message_body = input("Enter message body:")

date_str = input("enter the date to send the message(yyyy-mm-dd):")
time_str = input("enter the time to send the message(hh:mm in 24hour format):")

scheduled_date = datetime.strptime(f"{date_str} {time_str}","%Y-%m-%d %H:%M")
current_date = datetime.now()
time_diff = scheduled_date - current_date
delay_seconds = time_diff.total_seconds()
if delay_seconds <= 0:
    print("The specified time has already passed. Please enter a future time")
else:
    print(f"message scheduled to be sent to{name} at {scheduled_date}")
    time.sleep(delay_seconds) 
    send_whatsapp_message(recipient_number,message_body)
