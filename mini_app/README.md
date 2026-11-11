# Mini aplicación modular (temática libre)

Diseña y programa una mini aplicación con el código organizado en **paquetes y subpaquetes**, que se ejecute desde un único `main.py` (en esta carpeta).

## Requisitos mínimos
- Al menos **3 paquetes** de primer nivel (pueden colgar de un paquete raíz).
- Al menos **2 subpaquetes dentro de cada paquete**.
- Al menos **1 módulo con código en cada subpaquete**.
- Al menos **3 módulos** con un bloque `if __name__ == "__main__":` con pruebas propias que impriman resultados.
- Cada carpeta que sea paquete o subpaquete lleva su `__init__.py`.

## Temáticas posibles (la de *restaurante* NO se puede elegir)
| Aplicación | Posibles paquetes |
| --- | --- |
| Gestor de un gimnasio | `socios`, `actividades`, `facturacion` |
| Alquiler de vehículos | `flota`, `reservas`, `tarifas` |
| Tienda online de electrónica | `catalogo`, `pedidos`, `envios` |
| Clínica veterinaria | `pacientes`, `citas`, `cobros` |
| Taller mecánico | `vehiculos`, `reparaciones`, `presupuestos` |
| Agencia de viajes | `destinos`, `reservas`, `pagos` |
| Gestión de un parking | `plazas`, `accesos`, `tarificacion` |
| Monitor de sensores de una fábrica | `sensores`, `alertas`, `informes` |

## Forma de la estructura (ejemplo del enunciado)
```
app_xxx/
├── main.py
├── raiz/                    ← paquete raíz (opcional)
│   ├── __init__.py
│   ├── config.py
│   ├── paquete1/
│   │   ├── __init__.py
│   │   ├── subpaquete1/
│   │   │   ├── __init__.py
│   │   │   └── modulo.py
│   │   └── subpaquete2/
│   │       ├── __init__.py
│   │       └── modulo.py
│   ├── paquete2/ ...
│   └── paquete3/ ...
└── tests_manuales.py
```

## Comprobar la estructura
Cuando lo tengas montado:
```
python comprobar_estructura.py
```
Te dice si cumples el mínimo de paquetes, subpaquetes, módulos y bloques `if __name__ == "__main__":`, y si `main.py` se ejecuta sin errores.

> 💡 Para probar el bloque `if __name__ == "__main__":` de un módulo interno, ejecútalo como módulo desde esta carpeta:
> `python -m raiz.paquete1.subpaquete1.modulo`
