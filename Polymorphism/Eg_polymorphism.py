# Concept: Polymorphism
# Polymorphism allows different classes to have methods with the exact same name but different underlying logic.
#  This lets you loop through a collection of different objects and call the same method on all of them uniformly, 
# without caring about their specific class type



class EmailNotification:
    def __init__(self,sender_email):
        self.sender_email=sender_email

    def send_msg(self,message):
        print(f"Sending email from {self.sender_email}:{message}")

    
class SMSNotification:
    def __init__(self,phone_number):
        self.phone_number=phone_number

    def send_msg(self,message):
        print(f"Sending SMS text to ph no {self.phone_number}:{message}")



email=EmailNotification("example@oop.com")
sms=SMSNotification(5784768798)

#create list of objects
channels=[email,sms]

msg="System update completed"

#looping through objects
for channel in channels:
    channel.send_msg(msg)