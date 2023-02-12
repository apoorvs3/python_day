from datetime import datetime, timedelta

print(datetime.now().strftime('%d/%m/%Y'))
print(datetime.now().strftime('%H:%M'))
x = datetime.today() - timedelta(days=365*6)
print(x.strftime('%d%m%Y'))
print((datetime.today() + timedelta(days=2)).strftime("%d/%m/%Y"))
