# 📒 Chuleta para el examen de Python

> Para tenerla **abierta durante el examen**. Busca el tipo de pregunta en el índice y copia el patrón.

| Si te piden… | Ve a |
|---|---|
| "¿Qué se muestra por pantalla?" | [1](#1-lectura-de-código-trampas-típicas) |
| Lista / set / diccionario "en una línea" | [2](#2-comprehensions) |
| `lambda`, `map`, `filter`, `reduce`, `sorted` | [3](#3-programación-funcional) |
| Función que recibe o devuelve funciones | [3](#3-programación-funcional) |
| Función recursiva | [4](#4-recursión) |
| Crear una clase | [5](#5-clases) |
| `+`, `==`, `len`, `in`, `str`, `float`… sobre objetos | [6](#6-sobrecarga-de-operadores) |
| Herencia, `super()`, MRO | [7](#7-herencia-super-y-mro) |
| Refactorizar `if/elif` por tipo → clases | [8](#8-refactorizar-ifelif-a-polimorfismo) |
| Módulos y paquetes | [9](#9-programación-modular) |
| Preguntas de teoría | [10](#10-respuestas-de-teoría-listas-para-copiar) |

---

## 1. Lectura de código: trampas típicas

| Código | Qué pasa |
|---|---|
| `b = a` (listas) | **Mismo objeto**: si cambias `b`, cambia `a`. |
| `c = a[:]` / `a.copy()` / `list(a)` | **Copia** nueva. |
| `a is b` / `a == b` | ¿Mismo objeto? / ¿Mismo contenido? |
| `obj.atrib_clase = 10` | **Crea un atributo de instancia** que tapa al de clase. La clase y los demás objetos no cambian. |
| `Clase.atrib = 10` | Cambia el de clase para todos (los que no lo tapan). |
| `self._x` | Un guion: solo convención ("privado"). Se puede leer desde fuera. |
| `self.__x` | Name mangling: fuera solo existe como `obj._Clase__x`. `obj.__x` da **`AttributeError`**. |
| Recursión sin caso base | **`RecursionError`** (límite ≈ 1000 llamadas). |
| `def f(x, lista=[])` | ⚠️ La lista por defecto se **comparte** entre llamadas. Usa `None`. |
| `print(map(...))` | Sale `<map object ...>`: le falta `list()`. |
| `"a" + 3` | `TypeError` → hay que poner `str(3)`. |
| `int("3.5")` | `ValueError` → `int(float("3.5"))`. |
| `d["no_existe"]` / `lista[99]` | `KeyError` / `IndexError`. |
| `round(2.5)` → `2`, `round(3.5)` → `4` | Redondeo "del banquero" al par. |
| `7 // 2` → `3`, `7 % 2` → `1`, `7 / 2` → `3.5` | División entera, resto, división real. |
| `print(a, b)` | Los separa con **un espacio**. `print()` solo → línea vacía. |

**Funciones que fabrican funciones (closures):** la función interna **recuerda** las variables de la externa.
`factura(albaran(1))` → primero se evalúa lo de **dentro**.

---

## 2. Comprehensions

```python
[EXPR for x in LISTA]                       # transformar
[EXPR for x in LISTA if COND]               # filtrar  → if AL FINAL, sin else
[A if COND else B for x in LISTA]           # clasificar → if/else DELANTE
[A if c1 else B if c2 else C for x in LISTA]  # tres opciones
[y for sub in LISTA for y in sub]           # aplanar (mismo orden que los for anidados)

{EXPR for x in LISTA}                       # set (sin repetidos, sin orden)
{k: v for k, v in DICC.items()}             # diccionario
{k: v for k, v in DICC.items() if v > 0}
{x: lista.count(x) for x in lista}          # contar apariciones
sum(x["precio"] for x in lista)             # suma (generador, sin corchetes)
len([x for x in lista if cond])             # contar los que cumplen
```

Textos útiles: `.strip()` quita espacios, `.capitalize()` primera en mayúscula, `.upper()`, `.lower()`, `.title()`, `.replace(a, b)`, `.split(",")`, `", ".join(lista)`.

---

## 3. Programación funcional

```python
from functools import reduce              # ¡reduce hay que importarlo!

doble = lambda x: x * 2
es_par = lambda x: x % 2 == 0

list(map(lambda c: c["km"], carreras))                    # transformar
list(filter(lambda c: c["tarjeta"] and c["km"] >= 10, carreras))  # filtrar
sorted(carreras, key=lambda c: c["km"], reverse=True)     # ordenar (reverse = de mayor a menor)
max(carreras, key=lambda c: c["km"])                      # el mayor según un campo

reduce(lambda acum, c: acum + c["importe"], carreras, 0)  # SUMAR un campo → valor inicial 0 obligatorio
reduce(lambda a, b: a if a["km"] >= b["km"] else b, carreras)   # EL MAYOR → sin valor inicial
reduce(lambda acum, c: acum + c["km"], filter(lambda c: c["tarjeta"], carreras), 0)  # filter + reduce
reduce(lambda a, b: a + b, map(lambda p: p["precio"], lista), 0)                  # map + reduce
```

**Función que recibe una función:**
```python
def transformar(lista, operacion):
    return [operacion(x) for x in lista]

transformar(datos, a_dolares)          # ¡se pasa SIN paréntesis!
transformar(datos, lambda x: x * 1.1)
```

**Función que devuelve una función:**
```python
def crear_tarifa(precio_km):
    def calcular(km):
        return round(km * precio_km, 2)
    return calcular                     # ¡SIN paréntesis!

nocturna = crear_tarifa(1.35)
nocturna(10)                            # 13.5
```

---

## 4. Recursión

**Receta:** 1) **caso base**: cuándo paro y qué devuelvo. 2) **caso recursivo**: un trozo + la función aplicada a algo **más pequeño**.

```python
def suma_lista(lista):                 # recorrer una lista
    if not lista:                      # lista vacía
        return 0
    return lista[0] + suma_lista(lista[1:])

def suma_digitos(n):                   # números: cifra a cifra
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)      # última cifra + resto

def es_palindromo(t):                  # textos: por los extremos
    if len(t) <= 1:
        return True
    if t[0] != t[-1]:
        return False
    return es_palindromo(t[1:-1])

def ahorro(capital, anios):            # repetir n veces
    if anios == 0:
        return capital
    return ahorro(capital * 1.02, anios - 1)

def contar_unidades(pedidos):          # campo de una lista de diccionarios
    if not pedidos:
        return 0
    return pedidos[0]["unidades"] + contar_unidades(pedidos[1:])

def peso_total(caja):                  # listas anidadas (aquí SÍ se usa for)
    total = 0
    for e in caja:
        if isinstance(e, list):
            total += peso_total(e)     # caja → recursión
        else:
            total += e                 # (para CONTAR: total += 1)
    return total

def factorial(n):                      # clásicos
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
```

**Iterativo vs. recursivo:** la recursiva queda más corta y "matemática", pero cada llamada ocupa memoria. Con muchas llamadas (≈ más de 1000) da `RecursionError`; la iterativa no.

---

## 5. Clases

```python
class Cuenta:
    total_cuentas = 0                  # atributo de CLASE (compartido)
    COMISION = 1.5                     # constante de clase

    def __init__(self, titular, saldo=0.0):   # valor por defecto
        self.titular = titular         # atributo de INSTANCIA
        self._saldo = saldo            # "privado" por convención
        Cuenta.total_cuentas += 1      # ¡con Cuenta., NO con self.!

    def retirar(self, importe):        # devuelve True/False
        total = importe + Cuenta.COMISION
        if total <= self._saldo:
            self._saldo -= total
            return True
        return False

    @classmethod
    def cuentas_creadas(cls):          # recibe la clase
        return cls.total_cuentas

    @staticmethod
    def desde_texto(texto):            # no recibe ni self ni cls
        return Cuenta("Anónimo", float(texto.replace(",", ".")))

    def __str__(self):                 # print(obj) / str(obj) → para personas
        return f"{self.titular}: {self._saldo:.2f} €"

    def __repr__(self):                # en listas y consola → para programadores
        return f"Cuenta({self.titular!r}, {self._saldo})"   # !r pone las comillas
```

- `__str__` y `__repr__` **devuelven** un texto (`return`), no lo imprimen.
- `print(obj)` usa `__str__`; si no existe, usa `__repr__`. `print([obj1, obj2])` usa siempre `__repr__`.

**Composición** (una clase que **contiene** objetos de otra):
```python
class Carrito:
    def __init__(self):
        self.lineas = []                         # lista de tuplas (articulo, cantidad)
    def agregar(self, articulo, cantidad):
        self.lineas.append((articulo, cantidad))
    def total(self):
        return sum(a.precio * c for a, c in self.lineas)
```

**Lista de objetos:** `[a.nombre for a in catalogo if a.stock == 0]`, `{a.nombre: a.valor() for a in catalogo}`, `sorted(catalogo, key=lambda a: a.precio)`.

**Formatos de f-string:** `{x:.2f}` → 2 decimales · `{x:.1f}` → 1 decimal · `{x!r}` → con comillas · `{x:>10}` → alinear a la derecha.

---

## 6. Sobrecarga de operadores

| Quiero que funcione | Método | Devuelve |
|---|---|---|
| `a + b` | `__add__(self, otro)` | **un objeto nuevo**: `return Importe(self.c + otro.c)` |
| `a - b`, `a * b` | `__sub__`, `__mul__` | objeto nuevo |
| `a += x` | `__iadd__(self, x)` | **`return self`** ⚠️ (si no, la variable pasa a valer `None`) |
| `a == b` | `__eq__(self, otro)` | `bool` |
| `a < b`, `a <= b`, `a > b` | `__lt__`, `__le__`, `__gt__` | `bool` (con `__lt__` ya funciona `sorted()`) |
| `str(a)`, `print(a)` | `__str__` | `str` |
| `float(a)`, `int(a)` | `__float__`, `__int__` | número |
| `bool(a)`, `if a:`, `not a` | `__bool__` | `bool` |
| `len(a)` | `__len__` | `int` |
| `x in a` | `__contains__(self, x)` | `bool` |
| `a[i]` | `__getitem__(self, i)` | el elemento |
| `for x in a` | `__iter__` | `return iter(self.lista)` |

```python
class Importe:
    def __init__(self, cantidad):
        self.cantidad = cantidad
    def __add__(self, otro):
        return Importe(self.cantidad + otro.cantidad)
    def __eq__(self, otro):
        return round(self.cantidad, 2) == round(otro.cantidad, 2)   # redondear: decimales de coma flotante
    def __lt__(self, otro):
        return self.cantidad < otro.cantidad
    def __str__(self):
        return f"{self.cantidad:.2f} €"
    def __float__(self):
        return float(self.cantidad)
```

Texto `"12,50 €"` → número: `float(texto.replace("€", "").strip().replace(",", "."))`.

---

## 7. Herencia, `super()` y MRO

```python
class Vehiculo:
    def __init__(self, matricula, km):
        self.matricula = matricula
        self.km = km
    def peaje(self):
        return self.km * 0.10

class Camion(Vehiculo):
    def __init__(self, matricula, km, ejes):     # recibe lo del padre + lo nuevo
        super().__init__(matricula, km)          # el padre guarda lo suyo
        self.ejes = ejes                         # yo guardo lo nuevo
    def peaje(self):                             # SOBRESCRIBIR ampliando
        return super().peaje() + 2 * self.ejes

class Moto(Vehiculo):                            # sin __init__ → usa el del padre
    def peaje(self):
        return super().peaje() / 2
```

- Nombre de la clase del objeto: `type(self).__name__` → `"Camion"`.
- `isinstance(obj, Vehiculo)` → `True` también para `Camion` y `Moto`.

### Herencia múltiple: método en 3 pasos
1. **Escribe el MRO:** la clase, sus padres **de izquierda a derecha** y los abuelos comunes **al final**, una sola vez. Compruébalo con `[c.__name__ for c in Clase.__mro__]`.
   `class D(B, C)` con `B(A)` y `C(A)` → `D → B → C → A → object`.
2. **`super()` = la SIGUIENTE clase del MRO del objeto**, no "mi padre". En un `D`, el `super()` de `B` llama a **`C`**.
3. Si cada método hace **primero** `super()` y **después** añade lo suyo (`print`, `+ ["x"]`, `+ " texto"`), lo añadido sale en **orden INVERSO al MRO**: `A`, `C`, `B`, `D`.

Ejemplo (`Administrador(Editor, Moderador)`):
MRO `Administrador → Editor → Moderador → Usuario`, y los mensajes salen `Usuario, Moderador, Editor, Administrador`.

- **¿Por qué el abuelo se ejecuta una sola vez?** Porque está una sola vez en el MRO y la cadena de `super()` recorre el MRO.
- **Si una clase NO llama a `super()`** corta la cadena: las clases que van detrás en el MRO no se ejecutan (se pierde su parte).
- **Si cambias el orden de los padres**, cambia el MRO y, con él, el orden de los resultados.

---

## 8. Refactorizar `if/elif` a polimorfismo

**Antes:** `if r[0] == "vuelo": ... elif r[0] == "hotel": ...`, repetido en varios sitios.
**Después:**

```python
class Reserva:                                   # superclase con lo común
    def __init__(self, cliente, destino, cantidad, precio_unitario):
        self.cliente = cliente
        self.destino = destino
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
    def precio_base(self):
        return self.cantidad * self.precio_unitario
    def precio_total(self):                      # por defecto
        return self.precio_base()
    def unidad(self):
        return "unidades"
    def __str__(self):
        tipo = type(self).__name__.replace("Reserva", "").upper()
        return f"{tipo} | {self.cliente} | {self.destino} | {self.cantidad} {self.unidad()} | {round(self.precio_total(), 2)} €"

class ReservaHotel(Reserva):                     # cada subclase: SOLO lo que cambia
    def unidad(self):
        return "noches"
    def precio_total(self):
        precio = self.precio_base()
        if self.cantidad >= 3:                   # este if es una regla de negocio, no pregunta por el tipo → vale
            precio *= 0.9
        return precio + self.cantidad * 1.5

class ReservaTren(Reserva):                      # no sobrescribe precio_total → le vale el del padre
    def unidad(self):
        return "billetes"

class Agencia:                                   # composición
    def __init__(self):
        self.reservas = []
    def agregar(self, r):
        self.reservas.append(r)
    def mostrar(self):
        for r in self.reservas:
            print(r)
    def total(self):
        return sum(r.precio_total() for r in self.reservas)          # ← polimorfismo
    def contar_superiores_a(self, importe):
        return len([r for r in self.reservas if r.precio_total() > importe])
```

**Para añadir un tipo nuevo:** solo se crea una subclase nueva. No se toca nada más.

---

## 9. Programación modular

```python
# mi_modulo.py
IVA = 0.21
def precio_con_iva(p):
    return round(p * (1 + IVA), 2)

if __name__ == "__main__":        # solo si se ejecuta directamente (python mi_modulo.py), NO al importar
    print(precio_con_iva(10))
```

```python
import mi_modulo                  # → mi_modulo.precio_con_iva(10)
import mi_modulo as mm            # → mm.precio_con_iva(10)
from mi_modulo import precio_con_iva, IVA   # → precio_con_iva(10)
from mi_modulo import *           # ⚠️ evitar: puede pisar tus nombres y no se sabe de dónde viene cada cosa
```

**Paquete** = carpeta con `__init__.py`:
```
tienda/
├── __init__.py       ← se ejecuta al importar el paquete; p. ej.: from .productos import Producto
├── productos.py
└── ventas.py         ← from .productos import Producto   (el "." = import relativo, del mismo paquete)
```
`from tienda import Producto` · `from tienda.ventas import total` · `from tienda import ventas` · `import tienda.ventas`

- Un módulo se ejecuta **una sola vez** aunque se importe varias veces (se guarda en `sys.modules`). Para recargarlo: `importlib.reload(mod)`.
- Python busca los módulos en `sys.path`: primero la carpeta del script.
- En Jupyter, `%%writefile archivo.py` (primera línea de la celda) crea el archivo.
- Biblioteca estándar: `math.sqrt`, `math.ceil` (hacia arriba), `math.floor`, `math.pi`, `random.randint(a, b)`, `random.choice(lista)`, `random.seed(n)`, `from datetime import date` → `date.today()`, `.strftime("%d/%m/%Y")`.

**Ventajas de la programación modular:** reutilizar código, organizar el programa en partes pequeñas, evitar choques de nombres (cada módulo es su propio espacio de nombres), que varias personas trabajen a la vez y que sea más fácil probarlo y mantenerlo.

---

## 10. Respuestas de teoría (listas para copiar)

- **Polimorfismo:** la misma llamada (`v.peaje()`) se comporta distinto según la clase del objeto, sin `if` que pregunte por el tipo. Se aplica en el bucle que recorre la lista de objetos.
- **Herencia:** una subclase reutiliza los atributos y métodos de la superclase y puede **añadir** cosas o **sobrescribirlas**.
- **Sobrescribir con `super()`:** se amplía el método del padre en vez de repetir su código.
- **Composición:** un objeto **contiene** otros objetos (un `Carrito` tiene `Articulos`). Es una relación "tiene un"; la herencia es "es un".
- **Encapsulación:** `_x` indica que no se toque desde fuera (convención); `__x` aplica name mangling.
- **Atributo de clase vs. de instancia:** el de clase lo comparten todos los objetos; el de instancia es propio de cada uno.
- **`@classmethod` vs. `@staticmethod`:** el primero recibe la clase (`cls`) y sirve para trabajar con atributos de clase o crear objetos; el segundo no recibe nada y es una función auxiliar dentro de la clase.
- **Ventaja de refactorizar a clases:** el cálculo de cada tipo está en **un único sitio**. Para añadir un tipo nuevo solo se crea una subclase, sin tocar el resto (abierto a la ampliación, cerrado a la modificación). Además, los nombres de los atributos (`reserva.cantidad`) se entienden mejor que los índices (`r[2]`).
- **¿Qué cambiaría al añadir `PlatoInfantil`?** Solo crear la subclase que sobrescriba `precio_final()`. Todo lo que usa `precio_final()` funciona sin tocarlo; solo lo que usa `isinstance()` con un tipo concreto depende de las clases.
