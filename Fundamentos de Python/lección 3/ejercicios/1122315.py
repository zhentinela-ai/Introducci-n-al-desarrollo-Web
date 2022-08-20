"""
Description: Calcula el tiempo que estará 
de vacaciones, y el tiempo que falta para
tomarlas
Author: NextU
Version 1.0
"""

from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

salida=parse(input("Indique la fecha en la que saldrá de vacaciones (DD/MM/YYYY): "),dayfirst=True)
regreso=parse(input("Indique la fecha en la que regresará de vacaciones (DD/MM/YYYY): "),dayfirst=True)
vacaciones=relativedelta(regreso,salida)
print(f"Estará {vacaciones.days} días de vacaciones")
falta=relativedelta(salida,datetime.now())
print(f"Faltan {falta.months} meses y {falta.days} días para las vacaciones")