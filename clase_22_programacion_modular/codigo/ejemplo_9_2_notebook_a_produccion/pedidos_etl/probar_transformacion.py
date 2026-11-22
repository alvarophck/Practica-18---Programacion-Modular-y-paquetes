"""Prueba aislada de la transformación (Sección 5 del Ejemplo 9.2)."""

from etl.transformacion import parsear, es_valido

print(es_valido(parsear("P010,Rosa Vidal,bilbao,19.95,entregado")))
print(es_valido(parsear("P009,Rosa Vidal,bilbao,9,95,entregado")))
print(es_valido(parsear("P011,Iván Paz,bilbao,,entregado")))
