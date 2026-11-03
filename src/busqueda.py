from Producto import Producto


def buscar_por_codigo(productos, codigo):
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None


def buscar_por_nombre(productos, texto):
    resultados = []
    for producto in productos:
        if texto.lower() in producto.nombre.lower():
            resultados.append(producto)
    return resultados


if __name__ == "__main__":
    inventario = [
        Producto("P001", "Teclado mecánico", 899.50, 25),
        Producto("P002", "Mouse inalámbrico", 349.00, 40),
        Producto("P003", "Teclado inalámbrico", 599.90, 15),
    ]

    print("Búsqueda por código: P002")
    encontrado = buscar_por_codigo(inventario, "P002")
    if encontrado:
        encontrado.mostrar_informacion()
    else:
        print("Producto no encontrado")

    print("\nBúsqueda por nombre: 'teclado'")
    for p in buscar_por_nombre(inventario, "teclado"):
        p.mostrar_informacion()