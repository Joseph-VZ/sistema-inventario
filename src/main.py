"""Punto de entrada del Sistema de Inventario (v1.1.0).

Menú de consola para registrar, consultar y buscar productos.
Ejecutar desde la carpeta raíz del paquete:
    python3 src/main.py
"""
from Producto import Producto
from busqueda import buscar_por_codigo, buscar_por_nombre

VERSION = "1.1.0"


def registrar(inventario):
    codigo = input("Código: ").strip()
    if buscar_por_codigo(inventario, codigo):
        print("Ya existe un producto con ese código.")
        return
    nombre = input("Nombre: ").strip()
    try:
        precio = float(input("Precio: "))
        existencia = int(input("Existencia: "))
    except ValueError:
        print("Precio o existencia no válidos.")
        return
    inventario.append(Producto(codigo, nombre, precio, existencia))
    print("Producto registrado correctamente.")


def listar(inventario):
    if not inventario:
        print("No hay productos registrados.")
        return
    for producto in inventario:
        producto.mostrar_informacion()
        print("-" * 30)


def buscar(inventario):
    texto = input("Código o parte del nombre: ").strip()
    encontrado = buscar_por_codigo(inventario, texto)
    resultados = [encontrado] if encontrado else buscar_por_nombre(inventario, texto)
    if not resultados:
        print("Producto no encontrado.")
    for producto in resultados:
        producto.mostrar_informacion()


def main():
    inventario = []
    opciones = {"1": registrar, "2": listar, "3": buscar}
    print(f"=== Sistema de Inventario v{VERSION} ===")
    while True:
        print("\n1. Registrar producto\n2. Mostrar productos\n3. Buscar producto\n4. Salir")
        try:
            opcion = input("Opción: ").strip()
        except EOFError:
            break
        if opcion == "4":
            break
        accion = opciones.get(opcion)
        if accion:
            accion(inventario)
        else:
            print("Opción no válida.")
    print("Hasta luego.")


if __name__ == "__main__":
    main()
