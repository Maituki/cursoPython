#de toda la libreria hemos seleccionado esa función
#from is_isbn import is_isbn
#comprueba que el email a crear es correcto
from email_validator import validate_email, EmailNotValidError

email = "n@gmail.com"
is_new_account = True # False for login pages

try:
  # Check that the email address is valid.
  validation = validate_email(email, check_deliverability=is_new_account)

  # Take the normalized form of the email address
  # for all logic beyond this point (especially
  # before going to a database query where equality
  # may not take into account Unicode normalization).  
  email = validation.email
  print(email)
except EmailNotValidError as e:
  # Email is not valid.
  # The exception message is human-readable.
  print(str(e))
        
          
#devuelve true si existe el isbn - identificador de los libros
#print(is_isbn.is_isbn('144933072X'))

#print(dir())