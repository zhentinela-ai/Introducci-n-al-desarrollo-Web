from datetime import date, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

date = date.today()
date_hour = datetime.now()
print("Formato de fechas")
print("Fecha actual:", date)
print("Fecha y hora (Formato ctime):", date_hour.ctime())
print("Fecha y hora actual:", date_hour)
print("Fecha formato1:", date_hour.strftime("%d/%m/%Y"))
print("Fecha formato2:", date_hour.strftime("%d/%m/%Y %H:%M:%S"))
print("Fecha formato3:", date_hour.strftime("%A %d/%m/%Y %I:%M:%S%p"))
today = datetime.now()
date_nac = parse(input("Ingrese su fecha de nacimiento (dd/mm/yyyy): "), dayfirst=True)
age = relativedelta(today, date_nac)
print(f"Su edad es: {age}")
print("Su edad es:", age.years, "años", age.months, "meses", age.days, "días")
nochevieja_days = today-today.replace(day=31, month=12)
navidad_days = today-today.replace(day=24, month=12)
print("Faltan", abs(nochevieja_days.days), "días para la nochevieja")
print("Faltan", abs(navidad_days.days), "días para navidad")