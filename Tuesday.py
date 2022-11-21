#To see if today is Tuesday 

import datetime
print ("Check if today is Tuesday")

today = datetime.datetime.today()
dayofweek = today.weekday()
if dayofweek == 1:
    print ("Today is Tuesday")
elif dayofweek == 2:
    print ("Today is Wednesday")
else:
    print ("It's not Tuesday")