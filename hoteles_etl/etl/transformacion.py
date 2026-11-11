"""
transformacion.py · T (Transform): parsear, validar, convertir y filtrar
========================================================================

Requisitos:
- Funciones PURAS (no imprimen, no modifican nada de fuera, mismo resultado para la misma entrada):
    * parsear(linea)      → lista de campos limpios (sin espacios a los lados)
    * es_valida(campos)   → True/False: ¿se puede convertir a reserva sin errores?
    * a_reserva(campos)   → objeto Reserva (con los textos normalizados como en la celda 2)
    * transformar(lineas) → devuelve: reservas activas, ids con errores, ids anulados
- Usa al menos un map(), un filter() con lambda y una comprehension.

Equivale a las celdas 2 y 3 del notebook.

Piensa: ¿qué pasa con una línea que tiene MÁS campos de la cuenta? (mira la prueba de R011)
"""

# TODO: imports relativos (config y modelos)


def parsear(linea):
    # TODO
    pass


def es_valida(campos):
    # TODO
    pass


def a_reserva(campos):
    # TODO
    pass


def transformar(lineas):
    # TODO
    pass


if __name__ == "__main__":
    # Pruebas propias del módulo. Ejecuta con:  python -m etl.transformacion  (desde hoteles_etl)
    # TODO
    pass
