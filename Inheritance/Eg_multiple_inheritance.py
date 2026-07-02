# Concept: Multiple Inheritance
#  When a child class inherits from TWO OR MORE separate, independent parent classes at the same time. The child combines the traits and behaviors 
# of all its parents into one single class.

class Clock:
    def __init__(self,time_format):
        self.time_format=time_format

    def show_time(self):
        print(f"Displaying the time in {self.time_format} format")

class Phone:
    def __init__(self,phone_number):
        self.phone_number=phone_number

    def make_call(self):
        print(f"Calling from {self.phone_number}")

class SmartWatch(Clock,Phone):
    def __init__(self,time_format,phone_number,strap_color):
        Clock.__init__(self,time_format)
        Phone.__init__(self,phone_number)
        self.strap_color=strap_color

    def check_notifications(self):
        print(f"Checking notifications on {self.strap_color} color watch")

Watch=SmartWatch("12-hour",2346578919,"White")

Watch.show_time()
Watch.make_call()
Watch.check_notifications()