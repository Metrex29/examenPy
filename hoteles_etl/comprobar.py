"""
comprobar.py · Corrector automático del proyecto hoteles_etl
============================================================
NO hace falta tocar este archivo. Ejecútalo cuando quieras ver cómo vas:

    python comprobar.py

(desde la carpeta hoteles_etl, o con el botón ▶ de VS Code teniendo este archivo abierto)
"""

import ast
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ETL = os.path.join(AQUI, "etl")

SALIDA_MAIN = """Reservas leídas: 9
Reservas con errores: ['R004', 'R006']
Reservas anuladas: ['R002', 'R008']
Reservas válidas: 5
Informe de ingresos por hotel:
  Sierra Nevada      6 noches    766.00 €   media/noche  127.67 €
  Costa Azul         8 noches    751.50 €   media/noche   93.94 €
  Centro Histórico   2 noches    149.00 €   media/noche   74.50 €
  TOTAL             16 noches   1666.50 €
Informe guardado en informe_hoteles.csv"""

CSV = """hotel,noches,ingresos
Sierra Nevada,6,766.0
Costa Azul,8,751.5
Centro Histórico,2,149.0"""

SALIDA_PRUEBAS = "True\nFalse\nFalse\n185.0"

MODULOS = ["__init__", "config", "modelos", "extraccion", "transformacion", "carga", "orquestador"]
VALORES_PROHIBIDOS = {0.9, 0.90, 0.1, 2.5, "anulada", "socio", "informe_hoteles.csv"}

resultados = []


def ok(msg):
    resultados.append(True)
    print("  ✅", msg)


def fallo(msg, pista=""):
    resultados.append(False)
    print("  ❌", msg)
    if pista:
        print("     💡", pista)


def aviso(msg):
    print("  ⚠️ ", msg)


def ejecutar(archivo):
    r = subprocess.run([sys.executable, archivo], cwd=AQUI, capture_output=True,
                       text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    return r.stdout, r.stderr


def comparar(obtenido, esperado):
    a = [l.rstrip() for l in obtenido.strip("\n").splitlines()]
    b = [l.rstrip() for l in esperado.strip("\n").splitlines()]
    if a == b:
        return None
    for i in range(max(len(a), len(b))):
        la = a[i] if i < len(a) else "(no hay línea)"
        lb = b[i] if i < len(b) else "(no debería haber más líneas)"
        if la != lb:
            return f"Línea {i + 1} distinta:\n        tu salida: {la!r}\n        esperada : {lb!r}"


def arbol(nombre):
    with open(os.path.join(ETL, nombre + ".py"), encoding="utf-8") as f:
        return ast.parse(f.read())


def constantes_sin_docstrings(tree):
    docstrings = set()
    for nodo in ast.walk(tree):
        if isinstance(nodo, (ast.Module, ast.ClassDef, ast.FunctionDef)) and nodo.body:
            primero = nodo.body[0]
            if isinstance(primero, ast.Expr) and isinstance(primero.value, ast.Constant):
                docstrings.add(id(primero.value))
    return [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and id(n) not in docstrings]


def main():
    print("\n1) Estructura de carpetas")
    faltan = [m for m in MODULOS if not os.path.exists(os.path.join(ETL, m + ".py"))]
    if not faltan and os.path.exists(os.path.join(AQUI, "main.py")):
        ok("Están main.py y todos los módulos de etl/")
    else:
        fallo(f"Faltan archivos: {faltan}")
        return

    print("\n2) config.py: solo constantes en MAYÚSCULAS")
    tree = arbol("config")
    asignados = [t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)]
    otros = [n for n in tree.body if not isinstance(n, (ast.Assign, ast.Expr))]
    if len(asignados) >= 5 and all(a.isupper() for a in asignados) and not otros:
        ok(f"{len(asignados)} constantes: {', '.join(asignados)}")
    else:
        fallo("config.py debe tener al menos 5 constantes en MAYÚSCULAS y nada más",
              "descuento socio, tasa turística, estado anulada, tipo socio y nombre del CSV")

    print("\n3) Valores escritos «a mano» fuera de config.py")
    limpio = True
    for m in MODULOS:
        if m == "config":
            continue
        for c in constantes_sin_docstrings(arbol(m)):
            if not isinstance(c.value, bool) and c.value in VALORES_PROHIBIDOS:
                fallo(f"etl/{m}.py línea {c.lineno}: {c.value!r} está escrito a mano", "impórtalo de config")
                limpio = False
    if limpio:
        ok("Ningún módulo de etl repite valores de config")

    print("\n4) Imports")
    bien = True
    for m in MODULOS:
        for n in ast.walk(arbol(m)):
            absoluto = (isinstance(n, ast.ImportFrom) and n.level == 0 and (n.module or "").split(".")[0] == "etl") or \
                       (isinstance(n, ast.Import) and any(a.name.split(".")[0] == "etl" for a in n.names))
            if absoluto:
                fallo(f"etl/{m}.py línea {n.lineno}: dentro del paquete usa imports RELATIVOS", "from .config import ...")
                bien = False
    with open(os.path.join(AQUI, "main.py"), encoding="utf-8") as f:
        tree_main = ast.parse(f.read())
    for n in ast.walk(tree_main):
        if isinstance(n, ast.ImportFrom) and (n.module or "").startswith("etl."):
            fallo(f"main.py línea {n.lineno}: importa de un módulo interno ({n.module})", "usa solo: from etl import ...")
            bien = False
    if bien:
        ok("Relativos dentro de etl y main.py solo importa del paquete")
    nombres_main = {f.name for f in tree_main.body if isinstance(f, ast.FunctionDef)}
    tiene_bloque = any(isinstance(n, ast.If) and "__name__" in ast.unparse(n.test) for n in tree_main.body)
    if {"main", "mostrar_informe"} <= nombres_main and tiene_bloque:
        ok("main.py tiene main(), mostrar_informe() y el bloque if __name__ == \"__main__\"")
    else:
        fallo("main.py necesita main(), mostrar_informe() y if __name__ == \"__main__\":")

    print("\n5) transformacion.py: map, filter con lambda y comprehension")
    tree = arbol("transformacion")
    llamadas = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
    usa_map = any(n.func.id == "map" for n in llamadas)
    usa_filter = any(n.func.id == "filter" and n.args and isinstance(n.args[0], ast.Lambda) for n in llamadas)
    usa_comp = any(isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)) for n in ast.walk(tree))
    for cond, txt in [(usa_map, "map()"), (usa_filter, "filter() con lambda"), (usa_comp, "una comprehension")]:
        ok(f"Usa {txt}") if cond else fallo(f"No se encuentra {txt}")
    en_pruebas = {id(x) for p in tree.body if isinstance(p, ast.If) and "__name__" in ast.unparse(p.test)
                  for x in ast.walk(p)}
    if any(n.func.id == "print" and id(n) not in en_pruebas for n in llamadas):
        aviso("transformacion.py tiene print fuera del bloque de pruebas: las funciones deben ser PURAS")

    print("\n6) Paquete y clases")
    sys.path.insert(0, AQUI)
    try:
        import etl
        if getattr(etl, "__version__", None) == "1.0.0":
            ok("__version__ = \"1.0.0\"")
        else:
            fallo("Falta __version__ = \"1.0.0\" en etl/__init__.py")
        if {"ejecutar_pipeline", "exportar_csv"} <= set(getattr(etl, "__all__", [])) and \
                hasattr(etl, "ejecutar_pipeline") and hasattr(etl, "exportar_csv"):
            ok("__init__.py expone ejecutar_pipeline y exportar_csv en __all__")
        else:
            fallo("__init__.py debe importar ejecutar_pipeline y exportar_csv y ponerlos en __all__")
        from etl.modelos import Reserva
        for prop in ["es_socio", "importe_total"]:
            if isinstance(getattr(Reserva, prop, None), property):
                ok(f"Reserva.{prop} es una @property")
            else:
                fallo(f"Reserva.{prop} debe ser una @property")
        if "__repr__" in Reserva.__dict__:
            ok("Reserva tiene __repr__")
        else:
            fallo("Falta Reserva.__repr__")
        from etl.carga import InformeHoteles
        faltan = [m for m in ["cargar", "__len__", "por_hotel", "total"]
                  if m not in InformeHoteles.__dict__]
        ok("InformeHoteles tiene cargar, __len__, por_hotel y total") if not faltan \
            else fallo(f"A InformeHoteles le faltan: {faltan}")
    except Exception as e:
        fallo(f"Error al importar el paquete: {type(e).__name__}: {e}")

    print("\n7) python main.py")
    csv_path = os.path.join(AQUI, "informe_hoteles.csv")
    if os.path.exists(csv_path):
        os.remove(csv_path)
    out, err = ejecutar("main.py")
    if err.strip():
        fallo("main.py lanza un error:\n" + err.strip()[-800:])
    else:
        dif = comparar(out, SALIDA_MAIN)
        ok("La salida es idéntica a la del notebook") if dif is None else fallo("La salida no coincide. " + dif)
    if os.path.exists(csv_path):
        with open(csv_path, encoding="utf-8") as f:
            dif = comparar(f.read(), CSV)
        ok("informe_hoteles.csv tiene el contenido correcto") if dif is None else fallo("El CSV no coincide. " + dif)
    else:
        fallo("No se ha generado informe_hoteles.csv")

    print("\n8) python pruebas_manuales.py")
    out, err = ejecutar("pruebas_manuales.py")
    if err.strip():
        fallo("pruebas_manuales.py lanza un error:\n" + err.strip()[-800:])
    else:
        dif = comparar(out, SALIDA_PRUEBAS)
        ok("True / False / False / 185.0") if dif is None else fallo("No coincide. " + dif)

    total = len(resultados)
    bien = sum(resultados)
    print(f"\n{'=' * 50}\nResultado: {bien}/{total} comprobaciones superadas", "🎉" if bien == total else "")


if __name__ == "__main__":
    main()
