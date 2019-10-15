from datetime import *
today=datetime.today()
print(today)
print(date.today())
oneMONTH=timedelta(days=30)
nextMONTH=today+oneMONTH
print(nextMONTH)
nextDAY=today+timedelta(days=1)
print(nextDAY)
prevDAY=today-timedelta(days=1)
print(prevDAY)