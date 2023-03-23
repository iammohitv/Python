from datetime import datetime
now = datetime.now()

print(now)
print(type(now.hour))

if(now.hour>5 and now.hour<=12):
    print("Good Morning Sir")
elif(now.hour>12 and now.hour<=6):
    print("Good Afternoon Sir")
elif(now.hour>6 and now.hour<=8):
    print("Good Evening Sir")
else:
    print("Good Night Sir")