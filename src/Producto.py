class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print("Producto registrado")
        print(f"Código:     {self.codigo}")
        print(f"Nombre:     {self.nombre}")
        print(f"Precio:     ${self.precio:.2f}")
        print(f"Existencia: {self.existencia} unidades")


if __name__ == "__main__":
    producto = Producto("P001", "Teclado mecánico", 899.50, 25)
    producto.mostrar_informacion()