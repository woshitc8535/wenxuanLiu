from datetime import datetime
dt = datetime(2012,10,16,10,20)
print(dt)

dt2 = datetime(1992,10,16,9,20)
if dt.timestamp() > dt2.timestamp():
    print('Y')
else:
    print('N')