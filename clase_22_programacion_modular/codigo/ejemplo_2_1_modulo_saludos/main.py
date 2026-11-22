# Forma 1: importar el módulo completo
import saludos

print("--- Forma 1: import saludos ---")
saludos.saludar()                  # función del módulo
objeto = saludos.Saludo()          # objeto de la clase
objeto.saludar_persona("Ana")      # método del objeto

# Forma 2: importar solo la clase
from saludos import Saludo

print("--- Forma 2: from saludos import Saludo ---")
objeto = Saludo()
objeto.saludar_persona("Ana")
