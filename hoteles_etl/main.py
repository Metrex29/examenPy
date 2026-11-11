"""
main.py · Punto de entrada
==========================

Requisitos:
- Contiene los datos de entrada (ya están abajo).
- Una función `mostrar_informe(resultado)`, una función `main()` y el bloque `if __name__ == "__main__":`.
- SOLO importa del paquete `etl` (from etl import ...), NUNCA de sus módulos internos (nada de from etl.carga ...).

Ejecutar desde la carpeta hoteles_etl:
    python main.py
"""

# TODO: import desde el paquete etl

DATOS = """id,cliente,hotel,tipo,noches,precio_noche,estado
R001, Carmen Vidal ,costa azul,socio,3,95.00,confirmada
R002,Andrés Molina,SIERRA NEVADA,general,2,120.00,anulada
R003,Lucía Ferrer,Costa Azul,general,5,95.00,confirmada
R004,Raúl Ortega,centro histórico,socio,,80.00,confirmada
R005,Nuria Campos,Sierra Nevada,general,4,120.00,check-out
R006,Tomás Reyes,centro histórico,general,1,8O.00,confirmada
R007,Irene Navarro,Centro Histórico,socio,2,80.00,confirmada
R008,Óscar Prieto,sierra nevada,socio,3,120.00,ANULADA
R009,Paula Serrano,Sierra Nevada,general,2,135.50,confirmada"""


def mostrar_informe(resultado):
    # TODO: los print del informe (celdas 1, 2, 3 y 6 del notebook)
    pass


def main():
    # TODO: ejecutar el pipeline, mostrar el informe y exportar el CSV
    pass


# TODO: bloque if __name__ == "__main__":
