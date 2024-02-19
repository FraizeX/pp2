import datetime

x = datetime.datetime.now()

if int(x.strftime("%d")) >= 5:
    print(int(x.strftime("%d")) - 5)
else:
    y = datetime.datetime(2024, 1, 31)
    print(int(y.strftime("%d")) + int(x.strftime("%d"))  - 5)