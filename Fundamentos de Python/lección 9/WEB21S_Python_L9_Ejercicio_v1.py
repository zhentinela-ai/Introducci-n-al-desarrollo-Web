from os import waitpid
import re

def policy_password(password):
  password_pattern="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!$%&=_\-\+#;:\?\*])[A-Za-z\d!$%&=_\-\+#;:?\*]{8,14}$"
  return re.fullmatch(password_pattern,password) and policy_pass_history(password)

def policy_pass_history(password):
  try:
    with  open('pass_store-pass','r') as pass_file:
      for last_pass in pass_file:
        if password==last_pass.replace('\n',''):
          return False
  except Exception as error:
    print('Fallo al intentar leer las contraseñas anteriores')
    print(f'Error: {error}')
    return False
  return True

while True:
  password=input('Ingrese la contraseña: ')
  if policy_password(password):
    password_confirm=input('Vuelva a ingresar la contraseña: ')
    if password==password_confirm:
      print('Su contraseña se ha almacenado correctamente')
      break
    else:
      print('A ingresado una contraseña diferente, por favor  vuledva a ingresar la contraseña')
  else:
    print('Su contraseña no cumple con la política de contraseñas')
    print("""Recuerde la contraseña debe:
      - Contener al menos una letra mayúscula
      - Contener al menos una letra minúscula
      - Contener al menos un número
      - Contener al menos un caracter del siguiente conjunto: !·$%&=_-+#;:?
      - Debe ser diferente a las contraseñas anteriores
    """)


try:
  with open('pass_store-pass','a') as pass_file:
    pass_file.write(password+'\n')
except PermissionError as error:
  print('Falla al almacenar su contraseña.')
  print(f'Error: {error}')

