from datetime import datetime
print(datetime.today())

print(datetime.now())

print(datetime.utcnow())

timestamp = 1633049477
print(datetime.fromtimestamp(timestamp))

# date_string = "2025-09-29 14:30:45"
# dt_object = datetime.strptime(date_string,"%y-%m-%d %H:%M:%S")
# print(dt_object)

now = datetime.now()
formatted_date = now.strftime("%y-%m-%d %H:%M:%S")
print(formatted_date)
print(now.date())

print(now.time())

from datetime import date
current_date = date.today()
print(current_date)
specific_date=date(2025,5,7)
print(specific_date)


from datetime import time
specific_date=time(14,30,9)
print(specific_date)
specific_time_micro=time(14,30,45,123456)
print(specific_time_micro)


from datetime import datetime , date,timedelta
delta = timedelta(days=10)
print(delta)
current_date = date.today()
new_date = current_date + delta
print("current_date:,current_date")
print("New_date(after 10 days):",new_date)
current_datetime = datetime.now()
new_date = current_datetime - timedelta(days = 5)
print("current Date: ,current_datetime")
print("New datetime(5 days before)",new_date)


from datetime import datetime , timezone
utc_now = datetime.now(timezone.utc)
print(utc_now)

from datetime import datetime,timezone,timedelta
now_utc = datetime.now(timezone.utc)
print(now_utc)
offset = timezone(timedelta(hours=2))
now_ofset=datetime.now(offset)
print(now_ofset)

date1=datetime(2025,9,29)
date2=datetime(2025,12,31)
date_diff = date2-date1
print(date_diff)

from datetime import datetime,timedelta
new_date = datetime.now() + timedelta(days= 15)
print(new_date)


from datetime import datetime
now = datetime.now()
print(now.strftime("%I:%M %p"))