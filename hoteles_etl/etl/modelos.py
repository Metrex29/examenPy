"""
modelos.py · Clase Reserva
==========================

Requisitos:
- Clase `Reserva` con atributos con nombre:
  id_reserva, cliente, hotel, tipo, noches, precio_noche, estado
- `@property es_socio`: True si la reserva es de un socio.
- `@property importe_total`: SE CALCULA al pedirla (no se guarda como atributo).
  noches × precio_noche, con descuento si es socio, + tasa turística por noche (sin descuento).
  Redondeado a 2 decimales.
- Método `__repr__`.

Importa las constantes de config con un import RELATIVO (from .config import ...).
"""

# TODO: imports relativos de config


class Reserva:
    def __init__(self, id_reserva, cliente, hotel, tipo, noches, precio_noche, estado):
        # TODO
        pass

    @property
    def es_socio(self):
        # TODO
        pass

    @property
    def importe_total(self):
        # TODO
        pass

    def __repr__(self):
        # TODO
        pass


if __name__ == "__main__":
    # Pruebas propias del módulo. Ejecuta con:  python -m etl.modelos  (desde la carpeta hoteles_etl)
    # TODO: crea un par de reservas e imprime su importe_total
    pass
