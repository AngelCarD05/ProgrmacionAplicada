import time  
cadena = 'Python'

# Recorrer cada letra de la cadena
for letra in cadena:
   if letra == 't':
      # Si la letra actual es 't', se salta esa iteración del bucle
      continue
   print(letra)  # Imprime la letra si no fue 't'
   time.sleep(1)  # Pausa la ejecución 1 segundo
