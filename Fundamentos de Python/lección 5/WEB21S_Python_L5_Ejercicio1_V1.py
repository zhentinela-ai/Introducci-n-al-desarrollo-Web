"""
Description: Ejercicio de Diccionarios, Listas y Conjuntos
Author: Nextu
Version: 1
"""

print("Menu de opciones:")
print("1. Mostrar nombre de los delitos")
print("2. Mostrar los diez delitos más ocurridos")
print("3. Salir del programa")
while True:
  opcion=input("Seleccione la opción que desea aplicar:")
  if opcion in ['1','2','3']:
    break

#Procesando Archivo
uniq_crimes=set()
crimes_count=dict()
with open('Sacramento_crime_Jan2006.txt') as crimen_file:
  for event in crimen_file:
    crime_event=event.split(sep=',')
    crime_name=crime_event[5].replace('\n','')
    uniq_crimes=uniq_crimes|{crime_name}
    crime_count=crimes_count.get(crime_name)
    if crime_count:
      crimes_count[crime_name]=crime_count+1
    else:
      crimes_count[crime_name]=1
crime_count_ordered=sorted(((value,key) for (key,value) in crimes_count.items()),reverse=True)

#Mostrar resultados
if (opcion=='1'):
  for crime in uniq_crimes:
    print(crime)
elif (opcion=='2'):
  i=0
  for crime in crime_count_ordered:
    i+=1
    print(crime)
    if i>10:
      break
else:
  exit()