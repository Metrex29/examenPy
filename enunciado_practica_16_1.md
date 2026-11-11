# 🧗🏽‍♂️ Practica 16.1 - Modelo Examen Python

---

>
## Indicaciones generales

- Esta practica no hay que entregarla. 
- En el examen real saldrán de 10 a 15 preguntas como máximo y serán del mismo estilo y estructura de este modelo.
- Falta añadir preguntas del tema de programación modular.

---

## Sección 1. Lectura de código: ¿qué se muestra por pantalla?

En esta sección **no hay que programar**. Lee cada fragmento y escribe lo que mostrará por pantalla **antes de ejecutarlo**. Después, ejecútalo y comprueba si acertaste. Si no acertaste, explica con tus palabras por qué.

### Ejercicio 1.1 · El contador de tiendas

```python
class Tienda:
    total_tiendas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Tienda.total_tiendas += 1

t1 = Tienda("Centro")
t2 = Tienda("Norte")
t1.total_tiendas = 10

print(Tienda.total_tiendas, t1.total_tiendas, t2.total_tiendas)
```

**Pregunta extra:** ¿por qué `t1` y `t2` no muestran el mismo número?

### Ejercicio 1.2 · Dos listas que parecen tres

```python
pedidos_a = [101, 102, 103]
pedidos_b = pedidos_a
pedidos_c = pedidos_a[:]

pedidos_b.append(104)
pedidos_c.append(999)

print(pedidos_a)
print(pedidos_b)
print(pedidos_c)
print(pedidos_a is pedidos_b, pedidos_a is pedidos_c, pedidos_a == pedidos_b)
```

### Ejercicio 1.3 · Filtrar o clasificar

```python
valoraciones = [4, 7, 5, 9, 3]

resultado_1 = [v for v in valoraciones if v >= 5]
resultado_2 = ["POSITIVA" if v >= 5 else "NEGATIVA" for v in valoraciones]

print(resultado_1)
print(resultado_2)
```

**Pregunta extra:** ¿por qué el `if` está en una posición distinta en cada comprehension?

### Ejercicio 1.4 · Cuenta atrás

```python
def cuenta_atras(n):
    if n == 0:
        return "¡Despegue!"
    return str(n) + " " + cuenta_atras(n - 1)

print(cuenta_atras(3))
```

**Pregunta extra:** ¿qué ocurriría si se borran las dos líneas del `if`?

### Ejercicio 1.5 · Recepción de un hotel

```python
class Huesped:
    def bienvenida(self):
        return "Bienvenido"

class HuespedVIP(Huesped):
    def bienvenida(self):
        return super().bienvenida() + " - Tiene champán en la habitación"

class HuespedGrupo(Huesped):
    def bienvenida(self):
        return "Bienvenidos, el guía les espera en el vestíbulo"

for huesped in [Huesped(), HuespedVIP(), HuespedGrupo()]:
    print(huesped.bienvenida())
```

### Ejercicio 1.6 · Atributos con guiones bajos

```python
class Tarjeta:
    def __init__(self):
        self.titular = "Ana"
        self._saldo = 500
        self.__pin = 1234

t = Tarjeta()
print(t.titular)        # Línea A
print(t._saldo)         # Línea B
print(t._Tarjeta__pin)  # Línea C
print(t.__pin)          # Línea D
```

Indica qué líneas funcionan, cuál produce un error y de qué tipo es ese error.

### Ejercicio 1.7 · Funciones que fabrican funciones

```python
def crear_etiqueta(prefijo):
    def etiquetar(codigo):
        return prefijo + "-" + str(codigo)
    return etiquetar

factura = crear_etiqueta("FAC")
albaran = crear_etiqueta("ALB")

print(factura(15), albaran(7), factura(albaran(1)))
```

### Ejercicio 1.8 · La cafetería y la herencia múltiple

```python
class Bebida:
    def ingredientes(self):
        return ["café"]

class ConLeche(Bebida):
    def ingredientes(self):
        return super().ingredientes() + ["leche"]

class ConHielo(Bebida):
    def ingredientes(self):
        return super().ingredientes() + ["hielo"]

class Frappe(ConLeche, ConHielo):
    def ingredientes(self):
        return super().ingredientes() + ["nata"]

class CafeFrio(ConHielo, ConLeche):
    pass

print(Frappe().ingredientes())
print(CafeFrio().ingredientes())
print([clase.__name__ for clase in Frappe.__mro__])
```

**Preguntas extra:**

1. Dentro de `ConLeche`, `super()` no llama a `Bebida`. ¿A qué clase llama en un objeto `Frappe` y por qué?
2. ¿Por qué `"café"` aparece una sola vez si `ConLeche` y `ConHielo` heredan las dos de `Bebida`?
3. ¿Por qué cambia el orden de los ingredientes en `CafeFrio`?
---

## Sección 2. Comprehensions

### Ejercicio 2.1 · Precios con IVA

Una tienda guarda los precios **sin IVA** de sus productos:

```python
precios = [8.50, 12.00, 3.20, 45.90, 19.99, 7.00]
```

Usa **una sola list comprehension** para obtener los precios **con IVA (21 %)**, pero solo de los productos que cuestan **más de 10 €** sin IVA. Redondea cada precio a 2 decimales.

**Salida esperada**

```plain text
[14.52, 55.54, 24.19]
```

### Ejercicio 2.2 · Clasificar paquetes

Una empresa de mensajería tiene el peso de cada paquete en kilos:

```python
pesos = [0.5, 3.2, 12.0, 1.1, 25.4, 7.8]
```

Crea con una list comprehension una lista en la que cada paquete aparezca como `"LIGERO"` si pesa menos de 5 kg o como `"PESADO"` en caso contrario. Después, muestra cuántos paquetes son pesados.

**Salida esperada**

```plain text
['LIGERO', 'LIGERO', 'PESADO', 'LIGERO', 'PESADO', 'PESADO']
Paquetes pesados: 3
```

### Ejercicio 2.3 · Ciudades sin repetir

En un formulario de clientes, las ciudades se escribieron de forma poco cuidada:

```python
ciudades = ["Madrid", " madrid", "SEVILLA", "Valencia ", "sevilla", "Bilbao", "MADRID"]
```

Con **una set comprehension**, obtén las ciudades distintas, sin espacios sobrantes y con solo la primera letra en mayúscula. Muestra el resultado ordenado alfabéticamente y el número de ciudades distintas.

**Salida esperada**

```plain text
['Bilbao', 'Madrid', 'Sevilla', 'Valencia']
Ciudades distintas: 4
```

### Ejercicio 2.4 · Butacas libres en un cine

Un cine guarda cuántas butacas quedan libres en cada sala para la sesión de esta noche:

```python
butacas_libres = {"Sala 1": 0, "Sala 2": 34, "Sala 3": 6, "Sala 4": 0, "Sala 5": 120}
```

Con **comprehensions**, crea:

4. Una **lista** con los nombres de las salas completas (0 butacas libres). Para esta usa una list comprehension.
5. Un diccionario que asocie cada sala con un estado:
- `"COMPLETA"` si tiene 0 butacas libres;
- `"ÚLTIMAS PLAZAS"` si tiene menos de 10;
- `"DISPONIBLE"` en cualquier otro caso.
6. Un diccionario solo con las salas que **no** están completas, en el que el valor sea el **porcentaje de ocupación**, sabiendo que todas las salas tienen 150 butacas. Redondea a 1 decimal.
**Salida esperada**

```plain text
['Sala 1', 'Sala 4']
{'Sala 1': 'COMPLETA', 'Sala 2': 'DISPONIBLE', 'Sala 3': 'ÚLTIMAS PLAZAS', 'Sala 4': 'COMPLETA', 'Sala 5': 'DISPONIBLE'}
{'Sala 2': 77.3, 'Sala 3': 96.0, 'Sala 5': 20.0}
```

### Ejercicio 2.5 · Unir las cestas de la compra

Un supermercado online guarda los productos de cada cesta en una lista independiente:

```python
cestas = [["pan", "leche"], ["huevos"], [], ["leche", "café", "pan"]]
```

7. Con una list comprehension **con dos ****`for`**, crea una única lista con todos los productos de todas las cestas.
8. Con una dictionary comprehension, crea un diccionario que indique cuántas veces aparece cada producto. Pista: puedes usar el método `count()` de las listas.
**Salida esperada**

```plain text
['pan', 'leche', 'huevos', 'leche', 'café', 'pan']
{'pan': 2, 'leche': 2, 'huevos': 1, 'café': 1}
```

---

## Sección 3. Programación funcional

Una empresa de taxis registra los trayectos del día. Trabaja con estos datos en todos los ejercicios de la sección:

```python
carreras = [
    {"id": 1, "pasajero": "Raúl",    "km": 12.0, "importe": 18.5, "tarjeta": True},
    {"id": 2, "pasajero": "Sofía",   "km": 3.5,  "importe": 7.0,  "tarjeta": False},
    {"id": 3, "pasajero": "Iván",    "km": 28.0, "importe": 42.0, "tarjeta": True},
    {"id": 4, "pasajero": "Claudia", "km": 8.0,  "importe": 13.5, "tarjeta": True},
    {"id": 5, "pasajero": "Hugo",    "km": 15.0, "importe": 24.0, "tarjeta": False},
]
```

> El campo `tarjeta` indica si el pasajero pagó con tarjeta (`True`) o en efectivo (`False`).

### Ejercicio 3.1 · Funciones lambda

9. Crea una función lambda llamada `con_suplemento` que reciba un importe y le sume 2.50 € de suplemento nocturno.
10. Crea una función lambda llamada `es_larga` que reciba unos kilómetros y devuelva `True` si son 10 o más.
11. Usa `sorted()` con una lambda para ordenar las carreras **de más a menos kilómetros** y muestra solo el nombre del pasajero.
**Salida esperada**

```plain text
21.0
False
['Iván', 'Hugo', 'Raúl', 'Claudia', 'Sofía']
```

> La primera línea muestra `con_suplemento(18.5)` y la segunda, `es_larga(3.5)`.

### Ejercicio 3.2 · `map()`

Usa `map()` con una lambda para obtener:

12. La lista de kilómetros de todas las carreras.
13. Una lista de textos con el formato `"Carrera 1: 18.5 €"`.
**Salida esperada**

```plain text
[12.0, 3.5, 28.0, 8.0, 15.0]
['Carrera 1: 18.5 €', 'Carrera 2: 7.0 €', 'Carrera 3: 42.0 €', 'Carrera 4: 13.5 €', 'Carrera 5: 24.0 €']
```

### Ejercicio 3.3 · `filter()`

Usa `filter()` con una lambda para obtener:

14. Las carreras pagadas **en efectivo**. Muestra solo el nombre del pasajero.
15. Las carreras pagadas **con tarjeta y de 10 km o más**. Muestra solo su `id`.
**Salida esperada**

```plain text
['Sofía', 'Hugo']
[1, 3]
```

### Ejercicio 3.4 · `reduce()`

Importa `reduce` desde el módulo `functools` y úsalo para calcular:

16. La **recaudación total** del día.
17. La **carrera más larga**. Muestra el nombre del pasajero.
18. Los **kilómetros recorridos en carreras pagadas con tarjeta**. Combina `filter()` y `reduce()`.
**Salida esperada**

```plain text
Recaudación total: 105.0 €
Carrera más larga: Iván
Km pagados con tarjeta: 48.0
```

### Ejercicio 3.5 · Funciones que reciben funciones

Escribe una función `transformar_importes(carreras, operacion)` que reciba la lista de carreras y **una función**, y devuelva una lista con el resultado de aplicar esa función al importe de cada carrera. No uses `map()`: resuélvelo con una list comprehension.

Pruébala con:

- una función normal `a_dolares(x)`, que convierta euros a dólares con un cambio de 1.08 y redondee a 2 decimales;
- una lambda que añada un 10 % de propina, también redondeada a 2 decimales.
**Salida esperada**

```plain text
[19.98, 7.56, 45.36, 14.58, 25.92]
[20.35, 7.7, 46.2, 14.85, 26.4]
```

### Ejercicio 3.6 · Funciones que devuelven funciones

La empresa cobra un precio por kilómetro distinto según la franja horaria. Escribe una función `crear_tarifa(precio_km)` que **devuelva otra función**. Esa función recibirá unos kilómetros y devolverá el precio del trayecto, redondeado a 2 decimales.

```python
tarifa_diurna = crear_tarifa(1.10)
tarifa_nocturna = crear_tarifa(1.35)

print(tarifa_diurna(10))
print(tarifa_nocturna(10))
print([tarifa_nocturna(c["km"]) for c in carreras])
```

**Salida esperada**

```plain text
11.0
13.5
[16.2, 4.73, 37.8, 10.8, 20.25]
```

---

## Sección 4. Recursión

En esta sección **no puedes usar bucles** (`for` ni `while`) dentro de las funciones recursivas, salvo que el enunciado lo permita. Cada función debe tener un caso base claro.

### Ejercicio 4.1 · Sumar los dígitos de un código

Escribe una función recursiva `suma_digitos(n)` que reciba un número entero positivo y devuelva la suma de sus cifras.

Pista: `n % 10` da la última cifra y `n // 10` quita la última cifra.

```python
print(suma_digitos(4528))
print(suma_digitos(7))
```

**Salida esperada**

```plain text
19
7
```

### Ejercicio 4.2 · Total de una lista de gastos

Escribe una función recursiva `total_gastos(gastos)` que sume todos los valores de una lista. Usa la idea: *el total es el primer elemento más el total del resto de la lista*. El caso base es la lista vacía.

```python
print(total_gastos([12.5, 30, 7.5, 50]))
print(total_gastos([]))
```

**Salida esperada**

```plain text
100.0
0
```

### Ejercicio 4.3 · ¿Es un palíndromo?

Un palíndromo es una palabra que se lee igual al derecho y al revés. Escribe una función recursiva `es_palindromo(texto)` que devuelva `True` o `False`.

Pista: compara el primer y el último carácter y, si coinciden, vuelve a llamar a la función con el texto sin esos dos caracteres.

```python
print(es_palindromo("reconocer"))
print(es_palindromo("radar"))
print(es_palindromo("python"))
```

**Salida esperada**

```plain text
True
True
False
```

### Ejercicio 4.4 · Cajas dentro de cajas

Un almacén prepara envíos en los que unas cajas pueden ir **dentro de otras cajas**. Cada caja se representa con una lista y cada artículo con un número que indica su peso en kilos:

```python
envio = [2, [3, 1], [[4, 5], 2], [], 6]
```

En este envío hay una caja exterior con un artículo de 2 kg, una caja con dos artículos, una caja que contiene otra caja, una caja vacía y un artículo de 6 kg.

19. Escribe una función recursiva `peso_total(caja)` que devuelva los kilos que pesa todo el contenido.
20. Escribe una función recursiva `contar_articulos(caja)` que devuelva cuántos artículos hay en total. Las cajas no cuentan como artículos.
Pista: usa `isinstance(elemento, list)` para saber si un elemento es una caja. En este ejercicio **sí puedes usar un ****`for`** para recorrer el contenido de cada caja, porque las cajas interiores se tratan con la llamada recursiva.

**Salida esperada**

```plain text
Peso total: 23 kg
Número de artículos: 7
```

### Ejercicio 4.5 · Iterativo frente a recursivo

Una persona ahorra dinero en una cuenta que da un **2 % de interés al año**. Escribe dos funciones que calculen el dinero que tendrá tras `n` años, partiendo de un capital inicial:

- `ahorro_iterativo(capital, anios)`, con un bucle;
- `ahorro_recursivo(capital, anios)`, sin bucles.
Redondea el resultado a 2 decimales al mostrarlo.

```python
print(round(ahorro_iterativo(1000, 5), 2))
print(round(ahorro_recursivo(1000, 5), 2))
```

**Salida esperada**

```plain text
1104.08
1104.08
```

**Pregunta:** ¿qué ocurriría con la versión recursiva si se llamara con `anios = 5000`?

---

## Sección 5. Clases y objetos

### Ejercicio 5.1 · Artículos de una tienda de deportes

Crea una clase `Articulo` con:

- **Atributos de instancia:** `nombre`, `precio` y `stock`. El `stock` tiene valor por defecto 0.
- **Método ****`valor_inventario()`****:** devuelve el precio multiplicado por el stock.
- **Método ****`vender(cantidad)`****:**
- si hay stock suficiente, lo resta y devuelve `True`;
- si no lo hay, no cambia nada y devuelve `False`.
- **Método ****`reponer(cantidad)`****:** suma unidades al stock.
- **Método ****`__str__`****:** devuelve un texto como `Balón de fútbol | 25.0 € | 10 uds.`
```python
a1 = Articulo("Balón de fútbol", 25.0, 10)
a2 = Articulo("Cinta de pádel", 9.5)

print(a1)
print(a2)
print(a1.vender(3))
print(a2.vender(1))
a2.reponer(20)
print(a1)
print(a2)
print(a1.valor_inventario(), a2.valor_inventario())
```

**Salida esperada**

```plain text
Balón de fútbol | 25.0 € | 10 uds.
Cinta de pádel | 9.5 € | 0 uds.
True
False
Balón de fútbol | 25.0 € | 7 uds.
Cinta de pádel | 9.5 € | 20 uds.
175.0 190.0
```

### Ejercicio 5.2 · Cuentas de un banco

Crea una clase `Cuenta` con:

- **Atributo de clase ****`total_cuentas`****:** cuenta cuántas cuentas se han creado.
- **Atributo de clase ****`COMISION_RETIRADA`****:** vale 1.5 €.
- **Atributos de instancia:** `titular` y `_saldo`. El saldo inicial vale 0.0 si no se indica. El guion bajo indica que el saldo no debe modificarse directamente desde fuera de la clase.
- **Método ****`ingresar(importe)`****:** suma el importe al saldo solo si es positivo.
- **Método ****`retirar(importe)`****:**
- resta el importe **más la comisión**, solo si hay saldo suficiente para ambos;
- devuelve `True` o `False` según se haya podido retirar o no.
- **Método ****`consultar_saldo()`****:** devuelve el saldo.
- **Método de clase ****`cuentas_creadas()`****:** usa `@classmethod` y devuelve el valor de `total_cuentas`.
- **Método ****`__repr__`****:** devuelve un texto como `Cuenta('Laura', 150.0)`.
```python
c1 = Cuenta("Laura", 100.0)
c2 = Cuenta("Diego")

c1.ingresar(50)
c1.ingresar(-20)
print(c1.retirar(48.5))
print(c2.retirar(10))
print(c1, c2)
print("Cuentas creadas:", Cuenta.cuentas_creadas())
```

**Salida esperada**

```plain text
True
False
Cuenta('Laura', 100.0) Cuenta('Diego', 0.0)
Cuentas creadas: 2
```

### Ejercicio 5.3 · Carrito de la compra (composición)

Usando la clase `Articulo` del ejercicio 5.1, crea una clase `Carrito` que **contenga** una lista de líneas de compra. Cada línea es una tupla `(articulo, cantidad)`.

- **Método ****`agregar(articulo, cantidad)`****:** añade una línea al carrito.
- **Método ****`total()`****:** devuelve el importe total del carrito.
- **Método ****`resumen()`****:** muestra cada línea con el formato `3 x Balón de fútbol = 75.0 €` y, al final, el total.
```python
carrito = Carrito()
carrito.agregar(Articulo("Balón de fútbol", 25.0, 10), 3)
carrito.agregar(Articulo("Cinta de pádel", 9.5, 20), 2)
carrito.agregar(Articulo("Botella deportiva", 15.0, 5), 1)
carrito.resumen()
```

**Salida esperada**

```plain text
3 x Balón de fútbol = 75.0 €
2 x Cinta de pádel = 19.0 €
1 x Botella deportiva = 15.0 €
TOTAL: 109.0 €
```

### Ejercicio 5.4 · Lista de objetos

Con la clase `Articulo` del ejercicio 5.1 y esta lista:

```python
catalogo = [
    Articulo("Esterilla", 30.0, 12),
    Articulo("Comba", 12.0, 0),
    Articulo("Bicicleta estática", 180.0, 3),
    Articulo("Mancuernas", 45.0, 0),
]
```

Resuelve cada apartado en **una sola línea**, usando comprehensions o `sorted()`:

21. Los nombres de los artículos sin stock.
22. Un diccionario `nombre → valor_inventario()`.
23. El catálogo ordenado por precio de menor a mayor. Muestra cada artículo con `print()`.
**Salida esperada**

```plain text
['Comba', 'Mancuernas']
{'Esterilla': 360.0, 'Comba': 0.0, 'Bicicleta estática': 540.0, 'Mancuernas': 0.0}
Comba | 12.0 € | 0 uds.
Esterilla | 30.0 € | 12 uds.
Mancuernas | 45.0 € | 0 uds.
Bicicleta estática | 180.0 € | 3 uds.
```

---

## Sección 6. Sobrecarga de operadores y conversión de tipos

### Ejercicio 6.1 · Sumar y comparar importes

Crea una clase `Importe` que guarde una `cantidad` en euros. Haz que funcionen estas operaciones:

- `+` entre dos importes, que devuelve un **nuevo** `Importe`;
- `==` y `<`, que comparan las cantidades;
- `str()`, que muestra el importe con 2 decimales y el símbolo `€`;
- `float()`, que devuelve la cantidad como número decimal.
```python
a = Importe(19.99)
b = Importe(5.01)
c = Importe(25)

total = a + b
print(total)
print(total == c)
print(a < b)
print(float(a) * 2)
```

**Salida esperada**

```plain text
25.00 €
True
False
39.98
```

### Ejercicio 6.2 · Lista de reproducción

Crea una clase `ListaReproduccion` con un atributo `nombre` y una lista interna de canciones. Haz que funcionen estas operaciones:

- `len(lista)`, que devuelve el número de canciones;
- `"titulo" in lista`, que indica si una canción está en la lista;
- `lista += "titulo"`, que añade una canción y devuelve la propia lista;
- `str(lista)`, que muestra un texto como `Viaje (3 canciones)`.
```python
viaje = ListaReproduccion("Viaje")
viaje += "Canción A"
viaje += "Canción B"
viaje += "Canción C"

print(viaje)
print(len(viaje))
print("Canción B" in viaje)
print("Canción Z" in viaje)
```

**Salida esperada**

```plain text
Viaje (3 canciones)
3
True
False
```

### Ejercicio 6.3 · Precios escritos a mano

Un restaurante recibe los precios de su carta como texto, con coma decimal y el símbolo del euro, por ejemplo `"12,50 €"`.

24. Crea una clase `Precio` que guarde el valor en euros como número decimal.
25. Añade un **método estático** `desde_texto(texto)` que reciba un texto como `"7,25 €"` y devuelva un objeto `Precio`.
26. Haz que:
- `float(precio)` devuelva el valor en euros;
- `bool(precio)` devuelva `False` si el precio es 0 (plato gratuito) y `True` en caso contrario;
- `str(precio)` muestre el formato `7.25 €`, con 2 decimales.
```python
carta = ["12,50 €", "0,00 €", "7,25 €", "18,00 €"]
precios = [Precio.desde_texto(t) for t in carta]

print([float(p) for p in precios])
print("Total carta:", sum(float(p) for p in precios))
print("Platos gratuitos:", len([p for p in precios if not p]))
print(precios[2])
```

**Salida esperada**

```plain text
[12.5, 0.0, 7.25, 18.0]
Total carta: 37.75
Platos gratuitos: 1
7.25 €
```

---

## Sección 7. Herencia, polimorfismo y herencia múltiple

### Ejercicio 7.1 · Peajes de una autopista

Una autopista cobra peajes distintos según el tipo de vehículo.

27. Crea una superclase `Vehiculo` con los atributos `matricula` y `kilometros`, y un método `peaje()` que devuelva 0.10 € por kilómetro.
28. Crea estas subclases, que **sobrescriben** `peaje()`:
- `Moto`: paga la mitad que un vehículo normal;
- `Camion`: tiene un atributo adicional `ejes` y paga lo mismo que un vehículo normal **más 2 € por cada eje**. Usa `super()` tanto en el constructor como en `peaje()`.
29. Crea una lista con un `Vehiculo`, una `Moto` y un `Camion` y recórrela con **un único bucle**, mostrando la matrícula y el peaje redondeado a 2 decimales.
30. Muestra el total recaudado.
```python
vehiculos = [
    Vehiculo("1234-ABC", 100),
    Moto("5678-DEF", 100),
    Camion("9012-GHI", 100, 4),
]
```

**Salida esperada**

```plain text
1234-ABC → 10.0 €
5678-DEF → 5.0 €
9012-GHI → 18.0 €
Total recaudado: 33.0 €
```

**Pregunta:** ¿en qué parte de tu código se aplica el polimorfismo?

### Ejercicio 7.2 · Suscripciones de una plataforma de series

Una plataforma de series ofrece varios tipos de suscripción.

31. Crea una superclase `Suscripcion` con `usuario` y `cuota_base`, y los métodos:
- `precio_mensual()`, que devuelve la cuota base;
- `ficha()`, que devuelve `"<usuario> (<tipo>): <precio> €"`. `<tipo>` es el nombre de la clase y `<precio>` se muestra con 2 decimales. Pista: `type(self).__name__`.
32. Crea estas subclases:
- `Familiar`: recibe además `perfiles_extra` y cuesta la cuota base más 3 € por cada perfil extra;
- `Anual`: tiene un 15 % de descuento sobre la cuota base;
- `ConAnuncios`: cuesta el 60 % de la cuota base.
33. Recorre la lista de suscripciones mostrando la ficha de cada una y calcula los ingresos mensuales totales con `sum()` y una comprehension.
```python
suscripciones = [
    Suscripcion("Carlos", 12),
    Familiar("Lucía", 12, 2),
    Anual("Sergio", 12),
    ConAnuncios("Nerea", 12),
]
```

**Salida esperada**

```plain text
Carlos (Suscripcion): 12.00 €
Lucía (Familiar): 18.00 €
Sergio (Anual): 10.20 €
Nerea (ConAnuncios): 7.20 €
Ingresos mensuales: 47.40 €
```

### Ejercicio 7.3 · Impresora multifunción (herencia múltiple)

34. Crea una clase `EquipoOficina` con un atributo `modelo` y un método `encender()` que muestre `"<modelo>: encendido"`.
35. Crea dos clases que hereden de `EquipoOficina`:
- `Impresora`, con un método `imprimir(documento)` que muestre `"Imprimiendo <documento>"`;
- `Escaner`, con un método `escanear(documento)` que muestre `"Escaneando <documento>"`.
36. Crea una clase `Multifuncion` que herede de `Impresora` **y** de `Escaner`, con un método `fotocopiar(documento)` que reutilice los dos anteriores.
37. Además, cada clase debe sobrescribir un método `descripcion()` que use `super()`, para que en un objeto `Multifuncion` se obtenga la descripción completa.
```python
equipo = Multifuncion("OfiPro 300")
equipo.encender()
equipo.fotocopiar("contrato.pdf")
print(equipo.descripcion())
print([clase.__name__ for clase in Multifuncion.__mro__])
```

**Salida esperada**

```plain text
OfiPro 300: encendido
Escaneando contrato.pdf
Imprimiendo contrato.pdf
Equipo de oficina + Escáner + Impresora + Multifunción
['Multifuncion', 'Impresora', 'Escaner', 'EquipoOficina', 'object']
```

**Pregunta:** explica con tus palabras por qué la descripción sale en ese orden. Relaciónalo con el MRO que se muestra en la última línea.

### Ejercicio 7.4 · Permisos de usuarios en una aplicación (herencia múltiple con `super()`)

Una aplicación de gestión de contenidos tiene varios tipos de usuario. Cada tipo **suma** permisos a los del tipo del que hereda.

**Parte A. Crear las clases**

| Clase | Hereda de | Permiso que añade |
| --- | --- | --- |
| `Usuario` | — | `"leer"` |
| `Editor` | `Usuario` | `"editar"` |
| `Moderador` | `Usuario` | `"borrar comentarios"` |
| `Administrador` | `Editor` y `Moderador`, en ese orden | `"gestionar usuarios"` |

Requisitos:

38. Todas las clases reciben solo el parámetro `nombre`. `Usuario` lo guarda como atributo.
39. El constructor de **cada** clase llama primero a `super().__init__(nombre)` y **después** muestra `"Configurando <Clase>"`. `Usuario` no llama a `super()` y solo muestra su mensaje.
40. Cada clase tiene un método `permisos()` que devuelve la lista de permisos. Las subclases **no repiten** los permisos de sus padres: los obtienen con `super().permisos()` y les añaden el suyo.
41. `Usuario` tiene además un método `puede(accion)` que devuelve `True` si la acción está en `self.permisos()`.
**Parte B. Probar la clase**

```python
admin = Administrador("Marina")
print(admin.permisos())
print(admin.puede("borrar comentarios"), admin.puede("borrar la base de datos"))
print([clase.__name__ for clase in Administrador.__mro__])
```

**Salida esperada**

```plain text
Configurando Usuario
Configurando Moderador
Configurando Editor
Configurando Administrador
['leer', 'borrar comentarios', 'editar', 'gestionar usuarios']
True False
['Administrador', 'Editor', 'Moderador', 'Usuario', 'object']
```

**Parte C. Preguntas**

42. ¿Por qué `"Configurando Usuario"` aparece **una sola vez**, si `Editor` y `Moderador` llaman los dos a `super().__init__()`?
43. Cambia temporalmente `Editor.permisos()` para que devuelva directamente `["leer", "editar"]`, sin usar `super()`. ¿Qué permiso pierde el administrador? ¿Por qué?
44. Cambia el orden de la herencia a `class Administrador(Moderador, Editor)`. ¿Qué cambia en la salida?
---

## Sección 8. Refactorización: de código espagueti a clases

Una agencia de viajes tiene un programa que **funciona**, pero está escrito todo seguido. Tiene listas con posiciones difíciles de recordar, muchos `if/elif` según el tipo de reserva y cálculos repetidos. Cada vez que la agencia quiere vender un nuevo tipo de reserva hay que tocar el programa en varios sitios.

Tu tarea es **reorganizarlo usando clases, objetos, herencia y polimorfismo**, sin cambiar lo que muestra por pantalla.

### Parte A. Analizar el código original

Copia el código, ejecútalo y anota su salida. **No lo modifiques todavía.**

```python
# Programa original de la agencia de viajes
# Cada reserva: [tipo, cliente, cantidad, precio_unitario, destino]
reservas = [
    ["vuelo", "Ana López", 2, 120.0, "Madrid-Roma"],
    ["hotel", "Luis Pérez", 3, 85.0, "Hotel Mar Azul"],
    ["tren", "Marta Gil", 1, 45.0, "Madrid-Sevilla"],
    ["vuelo", "Pablo Ruiz", 1, 300.0, "Madrid-Nueva York"],
    ["hotel", "Eva Sanz", 2, 140.0, "Hotel Centro"],
]

total = 0
for r in reservas:
    if r[0] == "vuelo":
        precio = r[2] * r[3]
        precio = precio + 25
        if r[3] > 200:
            precio = precio + r[2] * 30
        print("VUELO | " + r[1] + " | " + r[4] + " | " + str(r[2]) + " pasajeros | " + str(round(precio, 2)) + " €")
    elif r[0] == "hotel":
        precio = r[2] * r[3]
        if r[2] >= 3:
            precio = precio * 0.9
        precio = precio + r[2] * 1.5
        print("HOTEL | " + r[1] + " | " + r[4] + " | " + str(r[2]) + " noches | " + str(round(precio, 2)) + " €")
    elif r[0] == "tren":
        precio = r[2] * r[3]
        print("TREN | " + r[1] + " | " + r[4] + " | " + str(r[2]) + " billetes | " + str(round(precio, 2)) + " €")
    total = total + precio

print("TOTAL AGENCIA: " + str(round(total, 2)) + " €")

# Contar reservas de más de 200 €: hay que repetir todos los cálculos
caras = 0
for r in reservas:
    if r[0] == "vuelo":
        precio = r[2] * r[3] + 25
        if r[3] > 200:
            precio = precio + r[2] * 30
    elif r[0] == "hotel":
        precio = r[2] * r[3]
        if r[2] >= 3:
            precio = precio * 0.9
        precio = precio + r[2] * 1.5
    elif r[0] == "tren":
        precio = r[2] * r[3]
    if precio > 200:
        caras = caras + 1

print("Reservas de más de 200 €: " + str(caras))
```

Las reglas de precio que esconde el código son:

| Tipo | Cantidad significa | Cálculo del precio |
| --- | --- | --- |
| Vuelo | pasajeros | pasajeros × precio + 25 € de tasas. Si el billete cuesta más de 200 €, se suman 30 € por pasajero. |
| Hotel | noches | noches × precio. Con 3 noches o más, un 10 % de descuento. Después se suma 1.5 € por noche de tasa turística. |
| Tren | billetes | billetes × precio. |

Antes de programar, responde:

45. ¿Qué significan `r[2]` y `r[3]`? ¿Es fácil saberlo sin leer el comentario?
46. ¿En cuántos sitios distintos está escrita la regla del precio de un hotel?
47. Si mañana la agencia vende **cruceros**, ¿cuántas partes del programa habría que tocar?
### Parte B. Crear la superclase

Crea una clase `Reserva` con:

- **Atributos:** `cliente`, `destino`, `cantidad` y `precio_unitario`.
- **Método ****`precio_base()`****:** devuelve cantidad × precio unitario.
- **Método ****`precio_total()`****:** en la superclase devuelve el precio base.
- **Método ****`unidad()`****:** devuelve el texto de la unidad, por ejemplo `"unidades"`.
- **Método ****`__str__`****:** devuelve la línea completa con el formato del programa original. El tipo (`VUELO`, `HOTEL`…) se obtiene a partir del nombre de la clase, y la unidad, con `unidad()`.
### Parte C. Crear las subclases

Crea `ReservaVuelo`, `ReservaHotel` y `ReservaTren`. Cada una debe:

- sobrescribir `unidad()`;
- sobrescribir `precio_total()` **solo si lo necesita**, reutilizando `precio_base()` o `super().precio_total()` en lugar de repetir la multiplicación.
Pista para el tipo: si la clase se llama `ReservaVuelo`, puedes obtener `"VUELO"` con `type(self).__name__.replace("Reserva", "").upper()`.

### Parte D. Crear una clase que agrupe las reservas (composición)

Crea una clase `Agencia` que **contenga** una lista de reservas y tenga estos métodos:

- `agregar(reserva)`;
- `mostrar()`, que imprime cada reserva;
- `total()`, que devuelve la suma de los precios totales;
- `contar_superiores_a(importe)`, que devuelve cuántas reservas superan ese importe.
### Parte E. Reescribir el programa principal

```python
agencia = Agencia()
agencia.agregar(ReservaVuelo("Ana López", "Madrid-Roma", 2, 120.0))
agencia.agregar(ReservaHotel("Luis Pérez", "Hotel Mar Azul", 3, 85.0))
agencia.agregar(ReservaTren("Marta Gil", "Madrid-Sevilla", 1, 45.0))
agencia.agregar(ReservaVuelo("Pablo Ruiz", "Madrid-Nueva York", 1, 300.0))
agencia.agregar(ReservaHotel("Eva Sanz", "Hotel Centro", 2, 140.0))

agencia.mostrar()
print(f"TOTAL AGENCIA:{round(agencia.total(), 2)} €")
print(f"Reservas de más de 200 €:{agencia.contar_superiores_a(200)}")
```

**Salida esperada** (idéntica a la del programa original)

```plain text
VUELO | Ana López | Madrid-Roma | 2 pasajeros | 265.0 €
HOTEL | Luis Pérez | Hotel Mar Azul | 3 noches | 234.0 €
TREN | Marta Gil | Madrid-Sevilla | 1 billetes | 45.0 €
VUELO | Pablo Ruiz | Madrid-Nueva York | 1 pasajeros | 355.0 €
HOTEL | Eva Sanz | Hotel Centro | 2 noches | 283.0 €
TOTAL AGENCIA: 1182.0 €
Reservas de más de 200 €: 4
```

### Parte F. Ampliación

La agencia empieza a vender **cruceros**. La cantidad son los camarotes y el precio es camarotes × precio más un 12 % de tasas portuarias. Crea `ReservaCrucero` y añade esta reserva:

```python
agencia.agregar(ReservaCrucero("Jorge Vidal", "Crucero Mediterráneo", 1, 900.0))
```

**Salida esperada** (solo las líneas nuevas o que cambian)

```plain text
CRUCERO | Jorge Vidal | Crucero Mediterráneo | 1 camarotes | 1008.0 €
TOTAL AGENCIA: 2190.0 €
Reservas de más de 200 €: 5
```

### Restricciones

- En el programa final **no puede quedar ningún ****`if/elif`**** que pregunte por el tipo de reserva**.
- No se puede usar `isinstance()` para decidir cómo calcular el precio.
- El cálculo de cada tipo de reserva debe estar escrito **en un único sitio**.
- Para añadir el crucero **no debes modificar** ni `Reserva` ni `Agencia`.
**Pregunta final:** compara tu respuesta a la pregunta 3 de la Parte A con lo que has tenido que hacer en la Parte F. ¿Qué ha cambiado?

---

## Sección 9. Ejercicio integrador: restaurante de comida a domicilio

Un restaurante quiere un pequeño programa para analizar los pedidos del día. Este ejercicio combina clases, herencia, polimorfismo, comprehensions, programación funcional y recursión.

### Parte A. Jerarquía de clases

48. Crea una superclase `Plato` con `nombre` y `precio`, un método `precio_final()` que devuelva el precio y un método `__str__` con el formato `Nombre - 12.50 €`, usando `precio_final()`.
49. Crea estas subclases:
- `PlatoVegano`: tiene un 10 % de descuento sobre su precio;
- `PlatoGourmet`: tiene un recargo fijo de 3 €.
### Parte B. Datos del día

```python
pedidos = [
    {"cliente": "Ana",   "plato": PlatoVegano("Ensalada quinoa", 11.0),  "unidades": 2},
    {"cliente": "Luis",  "plato": Plato("Hamburguesa", 9.5),             "unidades": 1},
    {"cliente": "Marta", "plato": PlatoGourmet("Risotto trufa", 18.0),   "unidades": 1},
    {"cliente": "Ana",   "plato": Plato("Pizza margarita", 10.0),        "unidades": 3},
    {"cliente": "Pablo", "plato": PlatoVegano("Curry garbanzos", 12.0),  "unidades": 1},
]
```

### Parte C. Comprehensions

50. Una **lista** con el importe de cada pedido (`precio_final() × unidades`), redondeado a 2 decimales.
51. Un **set** con los clientes distintos, ordenado alfabéticamente al mostrarlo.
52. Un **diccionario** `nombre del plato → precio final` de todos los platos.
### Parte D. Programación funcional

53. Con `filter()`, obtén los pedidos de **platos veganos**. Muestra el nombre del plato. Pista: `isinstance()`.
54. Con `map()` y `reduce()`, calcula la **facturación total** del día.
55. Crea una función `crear_filtro_minimo(minimo)` que devuelva otra función. Úsala para obtener los pedidos cuyo importe sea **igual o superior a 20 €** y muestra el nombre del cliente.
### Parte E. Recursión

Escribe una función recursiva `contar_unidades(pedidos)` que devuelva el total de unidades vendidas, **sin usar bucles**.

### Parte F. Informe final

Muestra un informe con este aspecto:

```plain text
=== CARTA DEL DÍA ===
Ensalada quinoa - 9.90 €
Hamburguesa - 9.50 €
Risotto trufa - 21.00 €
Pizza margarita - 10.00 €
Curry garbanzos - 10.80 €

Importes por pedido: [19.8, 9.5, 21.0, 30.0, 10.8]
Clientes distintos: ['Ana', 'Luis', 'Marta', 'Pablo']
Precios finales: {'Ensalada quinoa': 9.9, 'Hamburguesa': 9.5, 'Risotto trufa': 21.0, 'Pizza margarita': 10.0, 'Curry garbanzos': 10.8}
Platos veganos pedidos: ['Ensalada quinoa', 'Curry garbanzos']
Facturación total: 91.1 €
Pedidos de 20 € o más: ['Marta', 'Ana']
Unidades vendidas: 8
```

**Pregunta final:** si mañana el restaurante añade una clase `PlatoInfantil` con un precio fijo de 6 €, ¿qué partes del programa tendrías que cambiar y cuáles funcionarían sin tocarlas? Justifica tu respuesta.

## Sección 10: Programación Modular

---

> **Hoteles Brisa** es una cadena con tres hoteles: *Costa Azul*, *Sierra Nevada* y *Centro Histórico*. Un analista de revenue ha preparado en un notebook el **informe de ingresos por hotel**:
1. Lee las reservas del día, que llegan en formato CSV.
2. Descarta las reservas con el número de noches o el precio vacíos o mal escritos.
3. Descarta las reservas anuladas.
4. Calcula el importe de cada reserva: noches × precio por noche, con un **10 % de descuento para los socios** del programa de fidelización, más una **tasa turística de 2,50 € por noche** (la tasa no tiene descuento).
5. Suma noches e ingresos por hotel, ordena de mayor a menor ingreso y calcula el **ingreso medio por noche**.
6. Muestra el informe por pantalla y lo guarda en `informe_hoteles.csv`.
La dirección quiere que el informe se ejecute **automáticamente cada noche**. El trabajo consiste en convertir el notebook en un proyecto Python modular que haga **exactamente lo mismo**.

---

> Crear el notebook en VS Code o Jupyter con las siguientes celdas y ejecutarlo para comprobar la salida antes de empezar a modularizar.

**Celda [1]** · Cargar los datos

```python
datos = """id,cliente,hotel,tipo,noches,precio_noche,estado
R001, Carmen Vidal ,costa azul,socio,3,95.00,confirmada
R002,Andrés Molina,SIERRA NEVADA,general,2,120.00,anulada
R003,Lucía Ferrer,Costa Azul,general,5,95.00,confirmada
R004,Raúl Ortega,centro histórico,socio,,80.00,confirmada
R005,Nuria Campos,Sierra Nevada,general,4,120.00,check-out
R006,Tomás Reyes,centro histórico,general,1,8O.00,confirmada
R007,Irene Navarro,Centro Histórico,socio,2,80.00,confirmada
R008,Óscar Prieto,sierra nevada,socio,3,120.00,ANULADA
R009,Paula Serrano,Sierra Nevada,general,2,135.50,confirmada"""
lineas = datos.split("\n")[1:]
print("Reservas leídas:", len(lineas))
```

```plain text
Reservas leídas: 9
```

**Celda [2]** · Limpiar y descartar errores

```python
reservas = []
errores = []
for l in lineas:
    c = [x.strip() for x in l.split(",")]
    try:
        n = int(c[4])
        p = float(c[5])
        reservas.append([c[0], c[1].title(), c[2].title(), c[3].lower(), n, p, c[6].lower()])
    except ValueError:
        errores.append(c[0])
print("Reservas con errores:", errores)
```

```plain text
Reservas con errores: ['R004', 'R006']
```

> En `R006` el precio está escrito con una letra **O** en lugar de un cero: `8O.00`.

**Celda [3]** · Quitar las reservas anuladas

```python
anuladas = [r[0] for r in reservas if r[6] == "anulada"]
reservas = [r for r in reservas if r[6] != "anulada"]
print("Reservas anuladas:", anuladas)
print("Reservas válidas:", len(reservas))
```

```plain text
Reservas anuladas: ['R002', 'R008']
Reservas válidas: 5
```

**Celda [4]** · Calcular el importe de cada reserva

```python
def es_socio(r):
    return r[3] == "socio"

for r in reservas:
    base = r[4] * r[5]
    if es_socio(r):
        base = base * 0.90
    r.append(round(base + 2.50 * r[4], 2))
print(reservas[0])
```

```plain text
['R001', 'Carmen Vidal', 'Costa Azul', 'socio', 3, 95.0, 'confirmada', 264.0]
```

**Celda [5]** · Agregar por hotel

```python
ingresos = {}
noches = {}
for r in reservas:
    ingresos[r[2]] = round(ingresos.get(r[2], 0) + r[7], 2)
    noches[r[2]] = noches.get(r[2], 0) + r[4]
ingresos = dict(sorted(ingresos.items(), key=lambda x: x[1], reverse=True))
```

**Celda [6]** · Mostrar el informe

```python
print("Informe de ingresos por hotel:")
for h, t in ingresos.items():
    print(f"  {h:<17}{noches[h]:>3} noches {t:>9.2f} €   media/noche {t/noches[h]:>7.2f} €")
print(f"  {'TOTAL':<17}{sum(noches.values()):>3} noches {sum(ingresos.values()):>9.2f} €")
```

```plain text
Informe de ingresos por hotel:
  Sierra Nevada      6 noches    766.00 €   media/noche  127.67 €
  Costa Azul         8 noches    751.50 €   media/noche   93.94 €
  Centro Histórico   2 noches    149.00 €   media/noche   74.50 €
  TOTAL             16 noches   1666.50 €
```

**Celda [7]** · Guardar el informe en CSV

```python
with open("informe_hoteles.csv", "w", encoding="utf-8") as f:
    f.write("hotel,noches,ingresos\n")
    for h, t in ingresos.items():
        f.write(f"{h},{noches[h]},{t}\n")
print("Informe guardado en informe_hoteles.csv")
```

```plain text
Informe guardado en informe_hoteles.csv
```

Contenido de `informe_hoteles.csv`:

```plain text
hotel,noches,ingresos
Sierra Nevada,6,766.0
Costa Azul,8,751.5
Centro Histórico,2,149.0
```

---

Antes de escribir código, completar esta tabla con **al menos cinco problemas** concretos del notebook, indicando la celda donde se ve cada uno. Usar como guía la tabla de la Sección 2 del Ejemplo 9.2.

| Problema en el notebook | Dónde se ve (celda y línea) | Consecuencia en producción |
| --- | --- | --- |
| … | … | … |

> 💡 Pistas para buscar problemas:
- ¿Qué pasa si se ejecuta dos veces la celda 4? ¿Y si se salta la celda 3?
- ¿Qué significan `r[3]`, `r[4]` o `r[7]`?
- ¿Dónde están escritos el `0.90`, el `2.50`, el `"anulada"` y el `"socio"`?
- ¿Por qué `es_socio()` está definida en mitad del notebook y depende de la posición `r[3]`?
- ¿Se podría usar la limpieza de reservas en otro informe sin copiar y pegar?

---

Completar la tabla que indica **a qué módulo y a qué función, clase o constante** va a parar cada celda:

| Celda del notebook | Módulo de producción | Función / clase / constante |
| --- | --- | --- |
| Celda 1: cargar los datos |  |  |
| Celda 2: limpiar y descartar errores |  |  |
| Celda 3: quitar anuladas |  |  |
| Celda 4: calcular importes |  |  |
| Celda 5: agregar por hotel |  |  |
| Celda 6: mostrar el informe |  |  |
| Celda 7: guardar en CSV |  |  |
| `0.90`, `2.50`, `"anulada"`, `"socio"`, nombre del CSV |  |  |

---

### Estructura mínima exigida

```plain text
hoteles_etl/
├── main.py                 ← punto de entrada
└── etl/                    ← paquete del pipeline
    ├── __init__.py         ← recepción del paquete
    ├── config.py           ← reglas de negocio y parámetros
    ├── modelos.py          ← clase Reserva
    ├── extraccion.py       ← E: obtener las líneas en bruto
    ├── transformacion.py   ← T: parsear, validar, convertir, filtrar
    ├── carga.py            ← L: clase InformeHoteles + exportar a CSV
    └── orquestador.py      ← une E, T y L en el orden correcto
```

### Requisitos por módulo

| Módulo | Requisitos |
| --- | --- |
| `config.py` | Solo constantes en mayúsculas: descuento de socio, tasa turística por noche, estado de anulación, tipo de cliente socio y nombre del fichero de salida. Ningún otro módulo puede tener esos valores escritos «a mano» |
| `modelos.py` | Clase `Reserva` con atributos con nombre (`id_reserva`, `cliente`, `hotel`, `tipo`, `noches`, `precio_noche`, `estado`). Una `@property` `es_socio` y una `@property` `importe_total` que **se calcula** al pedirla (no se guarda como columna). Método `__repr__` |
| `extraccion.py` | Función `leer_lineas(texto)` que devuelve las líneas sin la cabecera |
| `transformacion.py` | Funciones **puras**: `parsear(linea)`, `es_valida(campos)`, `a_reserva(campos)` y `transformar(lineas)`. `transformar()` devuelve las reservas activas, los ids con errores y los ids anulados. Usar al menos un `map()`, un `filter()` con `lambda` y una comprehension |
| `carga.py` | Clase `InformeHoteles` con `cargar(reservas)`, `__len__`, `por_hotel()` (devuelve, ordenado de mayor a menor ingreso, un diccionario `{hotel: (noches, ingresos)}`) y `total()`. Función `exportar_csv(informe, ruta)` que genera el CSV |
| `orquestador.py` | Función `ejecutar_pipeline(texto)` que devuelve un diccionario con `leidas`, `errores`, `anuladas` e `informe` |
| `__init__.py` | Expone `ejecutar_pipeline` y `exportar_csv`. Define `__version__ = "1.0.0"` y `__all__` |
| `main.py` | Contiene los datos de entrada, una función `mostrar_informe(resultado)`, una función `main()` y el bloque `if __name__ == "__main__":`. **Solo importa del paquete ****`etl`**, nunca de sus módulos internos |

### Reglas de importación

- Dentro del paquete `etl` se usan **imports relativos** (`from .config import TASA_TURISTICA`).
- Desde `main.py` se usan **imports absolutos** a través de la recepción (`from etl import ejecutar_pipeline, exportar_csv`).
- No puede haber **imports circulares**: el sentido de las dependencias es `config` → `modelos` → `transformacion` / `carga` → `orquestador` → `__init__` → `main`.
---

Desde la carpeta del proyecto:

```powershell
cd hoteles_etl
python main.py
```

**Salida esperada** (debe ser **idéntica** a la del notebook, sin la fila de la celda 4):

```plain text
Reservas leídas: 9
Reservas con errores: ['R004', 'R006']
Reservas anuladas: ['R002', 'R008']
Reservas válidas: 5
Informe de ingresos por hotel:
  Sierra Nevada      6 noches    766.00 €   media/noche  127.67 €
  Costa Azul         8 noches    751.50 €   media/noche   93.94 €
  Centro Histórico   2 noches    149.00 €   media/noche   74.50 €
  TOTAL             16 noches   1666.50 €
Informe guardado en informe_hoteles.csv
```

El fichero `informe_hoteles.csv` generado debe tener **el mismo contenido** que el del notebook.

---

Crear un archivo `pruebas_manuales.py` en la carpeta `hoteles_etl` que importe **solo** las funciones de `etl.transformacion` y `etl.modelos` y compruebe estos casos sin ejecutar el pipeline completo:

```python
from etl.transformacion import parsear, es_valida, a_reserva

print(es_valida(parsear("R010,Eva Lara,costa azul,general,2,95.00,confirmada")))
print(es_valida(parsear("R011,Eva Lara,costa azul,general,2,95,50,confirmada")))
print(es_valida(parsear("R012,Eva Lara,costa azul,general,,95.00,confirmada")))
print(a_reserva(parsear("R013, Eva Lara ,COSTA AZUL,Socio,2,100.00,confirmada")).importe_total)
```

**Salida esperada:**

```plain text
True
False
False
185.0
```

> Explicar en un comentario por qué la línea `R011` (precio escrito con **coma decimal**) habría pasado sin error en el notebook y qué importe equivocado habría sumado.

---

56. **El notebook importa el paquete.** Crear un notebook nuevo `analisis.ipynb` en la carpeta `hoteles_etl` que, en lugar de repetir el código, importe `ejecutar_pipeline` y muestre el hotel con mayor ingreso medio por noche.
---

Diseñar y programar una **mini aplicación de temática libre** cuyo código esté organizado en **paquetes y subpaquetes**. La aplicación debe seguir la forma modular y ejecutarse desde un único `main.py`.

**Requisito estructural mínimo:**

- Al menos **3 paquetes** de primer nivel.
- Al menos **2 subpaquetes dentro de cada paquete**.
- Al menos **1 módulo con código en cada subpaquete**.
---

Se puede elegir cualquiera de estas o proponer otra (con el visto bueno del profesor):

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

---

> Este ejemplo usa la temática **restaurante** solo para mostrar el tipo de organización esperada. Esta temática **no se puede elegir**.

```plain text
app_restaurante/
├── main.py
├── restaurante/                     ← paquete raíz de la aplicación
│   ├── __init__.py
│   ├── config.py
│   ├── carta/                       ← paquete 1
│   │   ├── __init__.py
│   │   ├── modelos/                 ← subpaquete 1.1
│   │   │   ├── __init__.py
│   │   │   └── platos.py            (Plato, Entrante, Principal, Postre)
│   │   └── servicios/               ← subpaquete 1.2
│   │       ├── __init__.py
│   │       └── filtros.py           (filtrar por precio, alérgenos…)
│   ├── comandas/                    ← paquete 2
│   │   ├── __init__.py
│   │   ├── modelos/                 ← subpaquete 2.1
│   │   │   ├── __init__.py
│   │   │   └── comanda.py           (Mesa, Comanda, LineaComanda)
│   │   └── gestion/                 ← subpaquete 2.2
│   │       ├── __init__.py
│   │       └── cocina.py            (cola de comandas, tiempos)
│   └── caja/                        ← paquete 3
│       ├── __init__.py
│       ├── calculos/                ← subpaquete 3.1
│       │   ├── __init__.py
│       │   ├── impuestos.py
│       │   └── descuentos.py
│       └── informes/                ← subpaquete 3.2
│           ├── __init__.py
│           └── cierre.py            (cierre de caja del día)
└── tests_manuales.py
```

> Los tres paquetes (`carta`, `comandas`, `caja`) pueden colgar de un **paquete raíz** (`restaurante`) o estar directamente al lado de `main.py`. Las dos opciones son válidas; con paquete raíz los imports quedan `from restaurante.caja.calculos.impuestos import ...`.

---

- Al menos **3 módulos** incluyen un bloque `if __name__ == "__main__":` con pruebas propias que imprimen resultados.

