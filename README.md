# Examen Python · Práctica 16.1

Plantilla para preparar el examen: ejercicios **sin resolver** que se corrigen solos.

## 📁 Qué hay en cada sitio
| Archivo / carpeta | Para qué |
|---|---|
| `enunciado_practica_16_1.md` | El enunciado completo del modelo de examen |
| `Practica_16_1_PARA_PRACTICAR.ipynb` | **Secciones 1 a 9** en blanco. Cada ejercicio tiene una celda de comprobación ✅/❌ y una pista |
| `hoteles_etl/` | **Sección 10**: proyecto modular Hoteles Brisa (plantilla + corrector) |
| `mini_app/` | **Sección 10**: mini aplicación de temática libre (requisitos + comprobador de estructura) |
| `chuleta_examen.md` | Apuntes con los patrones de cada tipo de ejercicio, para llevar al examen |
| `soluciones/` | Secciones 1 a 9 resueltas. **Ábrelas solo después de intentarlo.** (Su Sección 10 es antigua: son ejercicios de práctica que no son los del enunciado) |

## ⚙️ Preparar VS Code (una sola vez)
1. Instala **Python 3** (en Windows marca *"Add Python to PATH"*) y **VS Code**.
2. Descarga el proyecto: en GitHub, elige la rama `claude/affectionate-noether-8fp98j` → botón **Code → Download ZIP** y descomprímelo (o `git clone` de esa rama).
3. En VS Code: **File → Open Folder…** y abre la carpeta `examenPy` (la que contiene este README). Así se aplica la configuración de `.vscode/`.
4. VS Code te ofrecerá instalar las extensiones recomendadas (**Python** y **Jupyter**): acepta.
5. Abre una terminal (**Terminal → New Terminal**) e instala lo necesario para los notebooks:
   ```
   py -m pip install -r requirements.txt
   ```
   (en Mac/Linux: `python3 -m pip install -r requirements.txt`)
6. Abre un `.ipynb` → arriba a la derecha **Select Kernel → Python Environments** → elige tu Python 3.

## ▶️ Cómo trabajar
**Secciones 1 a 9:** abre `Practica_16_1_PARA_PRACTICAR.ipynb`, ejecuta la primera celda (configuración) y ve ejercicio a ejercicio.

**Sección 10 · Hoteles Brisa** (en la terminal, dentro de la carpeta):
```
cd hoteles_etl
```
1. Ejecuta `notebook_original.ipynb` (*Run All*) y mira la salida.
2. Rellena `ANALISIS.md`.
3. Programa los archivos de `etl/` siguiendo el orden: `config` → `modelos` → `extraccion` → `transformacion` → `carga` → `orquestador` → `__init__` → `main.py`. Cada archivo explica en su cabecera qué tiene que llevar.
4. Comprueba cuando quieras:
   ```
   python comprobar.py
   ```
   Revisa la estructura, que no haya valores a mano fuera de `config.py`, los imports, el uso de `map`/`filter`/comprehension, la salida de `main.py`, el CSV y `pruebas_manuales.py`.
5. Prueba también: `python main.py` y `python pruebas_manuales.py`.
6. Ejercicio 56: `analisis.ipynb`.

**Sección 10 · Mini aplicación:** lee `mini_app/README.md`, crea tu estructura dentro de `mini_app/` y comprueba con:
```
cd mini_app
python comprobar_estructura.py
```

> En Windows, si `python` no funciona, usa `py` (por ejemplo `py comprobar.py`).
