"""
pruebas_manuales.py
===================
Importa SOLO funciones de etl.transformacion (y etl.modelos si lo necesitas)
y comprueba casos sin ejecutar el pipeline completo.

Ejecutar desde la carpeta hoteles_etl:
    python pruebas_manuales.py

Salida esperada:
True
False
False
185.0
"""

from etl.transformacion import parsear, es_valida, a_reserva

print(es_valida(parsear("R010,Eva Lara,costa azul,general,2,95.00,confirmada")))
print(es_valida(parsear("R011,Eva Lara,costa azul,general,2,95,50,confirmada")))
print(es_valida(parsear("R012,Eva Lara,costa azul,general,,95.00,confirmada")))
print(a_reserva(parsear("R013, Eva Lara ,COSTA AZUL,Socio,2,100.00,confirmada")).importe_total)

# TODO: explica en este comentario por qué la línea R011 (precio con COMA decimal)
#       habría pasado sin error en el notebook y qué importe equivocado habría sumado.
#
#
