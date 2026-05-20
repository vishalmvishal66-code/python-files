from datetime import datetime ,timedelta
today = datetime.now()
one_day = timedelta( weeks=1)
last_week = today - one_day
print('last_week:'+str(last_week))
