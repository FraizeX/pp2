from datetime import *

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(today.strftime("%x"))
print(yesterday.strftime("%x"))
print(tomorrow.strftime("%x"))

