class Date(object): # inherits from the 'object' class
    def get_date(self):
        return "23-08-2023"

class Time(Date): # inherits from 'Date' class
    def get_time(self):
        return "6:34 AM"

dt=Date()
print(dt.get_date())

tm=Time()
print(tm.get_time())
print(tm.get_date()) # finds this in the Date class



