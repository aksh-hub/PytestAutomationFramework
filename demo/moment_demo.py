import moment

from datetime import date
from datetime import  datetime


print(datetime.now().strftime("%d-%m-%Y_%H:%M:%S"))
print(moment.now())

print(moment.now().strftime("%H:%M:%S_%d-%m-%Y"))