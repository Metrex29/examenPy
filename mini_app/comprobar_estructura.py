"""
Comprueba la estructura mínima de la mini aplicación. No hace falta tocarlo.

    python comprobar_estructura.py
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
IGNORAR = {"__pycache__", ".ipynb_checkpoints", ".venv", "venv"}


def es_paquete(ruta):
    return os.path.isfile(os.path.join(ruta, "__init__.py"))


def subcarpetas(ruta):
    return [os.path.join(ruta, d) for d in sorted(os.listdir(ruta))
            if os.path.isdir(os.path.join(ruta, d)) and d not in IGNORAR and not d.startswith(".")]


def modulos_con_codigo(ruta):
    return [f for f in os.listdir(ruta) if f.endswith(".py") and f != "__init__.py"
            and os.path.getsize(os.path.join(ruta, f)) > 0]


def main():
    bien = True
    print("\n1) main.py")
    if os.path.isfile(os.path.join(AQUI, "main.py")):
        print("  ✅ Existe main.py")
    else:
        print("  ❌ Falta main.py en la carpeta mini_app")
        bien = False

    # Paquetes de primer nivel: los que están junto a main.py, o dentro de un único paquete raíz
    nivel = [d for d in subcarpetas(AQUI) if es_paquete(d)]
    sin_init = [os.path.relpath(d, AQUI) for d in subcarpetas(AQUI) if not es_paquete(d)]
    if len(nivel) == 1 and len([d for d in subcarpetas(nivel[0]) if es_paquete(d)]) >= 3:
        print(f"\n   (Paquete raíz detectado: {os.path.basename(nivel[0])})")
        sin_init += [os.path.relpath(d, AQUI) for d in subcarpetas(nivel[0]) if not es_paquete(d)]
        nivel = [d for d in subcarpetas(nivel[0]) if es_paquete(d)]

    print("\n2) Paquetes de primer nivel (mínimo 3)")
    print(f"  {'✅' if len(nivel) >= 3 else '❌'} {len(nivel)} paquetes: {[os.path.basename(p) for p in nivel]}")
    bien &= len(nivel) >= 3

    print("\n3) Subpaquetes (mínimo 2 por paquete) y módulos (mínimo 1 por subpaquete)")
    for p in nivel:
        subs = [s for s in subcarpetas(p) if es_paquete(s)]
        sin_init += [os.path.relpath(s, AQUI) for s in subcarpetas(p) if not es_paquete(s)]
        marca = "✅" if len(subs) >= 2 else "❌"
        bien &= len(subs) >= 2
        print(f"  {marca} {os.path.basename(p)}: {len(subs)} subpaquetes")
        for s in subs:
            mods = modulos_con_codigo(s)
            bien &= bool(mods)
            print(f"      {'✅' if mods else '❌'} {os.path.basename(s)}: {mods or 'sin módulos con código'}")
    if sin_init:
        print(f"  ⚠️  Carpetas sin __init__.py (no son paquetes): {sin_init}")

    print("\n4) Módulos con if __name__ == \"__main__\": (mínimo 3, sin contar main.py)")
    con_bloque = []
    for raiz, dirs, files in os.walk(AQUI):
        dirs[:] = [d for d in dirs if d not in IGNORAR]
        for f in files:
            if f.endswith(".py") and f not in {"main.py", "comprobar_estructura.py"}:
                with open(os.path.join(raiz, f), encoding="utf-8") as fh:
                    texto = fh.read()
                if "__name__" in texto and "__main__" in texto:
                    con_bloque.append(os.path.relpath(os.path.join(raiz, f), AQUI))
    print(f"  {'✅' if len(con_bloque) >= 3 else '❌'} {len(con_bloque)}: {con_bloque}")
    bien &= len(con_bloque) >= 3

    if os.path.isfile(os.path.join(AQUI, "main.py")):
        print("\n5) python main.py")
        r = subprocess.run([sys.executable, "main.py"], cwd=AQUI, capture_output=True, text=True, encoding="utf-8",
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        if r.returncode == 0:
            print("  ✅ Se ejecuta sin errores")
        else:
            print("  ❌ Error al ejecutar main.py:\n" + r.stderr[-800:])
            bien = False

    print("\n" + "=" * 50)
    print("🎉 Estructura correcta" if bien else "Todavía falta algo (mira los ❌)")


if __name__ == "__main__":
    main()
