movies=[]

class Movie:
  def __init__(self,movie_line):
    size=None
    movie_data=movie_line.split(sep=',')
    self.id=movie_data[0]
    size=movie_data[1].index('(')
    self.name=movie_data[1][0:size]
    self.year=int(movie_data[1][size+1:size+5])
    self.generos=movie_data[2].replace('\n','').split('|')

  def show(self):
    print(self.name)
    print(self.year)
    print(self.generos)

def procesar_archivo():
  with open('movies.csv','r',encoding="utf8") as movies_file:
    for movie_line in movies_file:
      movies.append(Movie(movie_line))

def menu():
  print("Opciones")
  print("1. Buscar películas por año")
  print("2. Salir")
  return input("Indica la opción a ejecutar: ")

def buscar_por_year(year):
  for movie in movies:
    if movie.year==int(year):
      movie.show()
      print("\n")

print('Cargando películas...')
procesar_archivo()
print(f"Se han cargado {len(movies)} películas")
while True:
  opcion=menu()
  if opcion == '1':
    buscar_por_year(input("Indique el año: "))
  elif opcion=='2':
    exit()

