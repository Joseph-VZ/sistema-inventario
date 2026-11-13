class Producto: #Antes: class Producto: 
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print("Producto disponible")
        print(f"Código:     {self.codigo}")
        # PASO 6 - PUNTO DE ERROR (nombre): para provocar el error, cambiar esta línea
        # para que el nombre no se muestre correctamente, por ejemplo:
        #     print(f"Nombre:     {self.nombre.upper()}")
        # Detectan el error: test_cp03_nombre, test_cp06_mostrar_informacion_completa.
        # Después de comprobarlo, regresar la línea a como está ahora.
        print(f"Nombre:     {self.nombre}")
        # PASO 6 - PUNTO DE ERROR (precio): para provocar el error, cambiar esta línea
        # para que muestre un valor diferente al almacenado, por ejemplo:
        #     print(f"Precio:     ${self.precio + 100:.2f}")
        # Detectan el error: test_cp04_precio, test_cp06_mostrar_informacion_completa
        # y test_cp07_segundo_producto_independiente.
        # Después de comprobarlo, regresar la línea a como está ahora.
        print(f"Precio:     ${self.precio + 100:.2f}")
        print(f"Existencia: {self.existencia} unidades")


if __name__ == "__main__":
    producto = Producto("P001", "Teclado mecánico", 899.50, 25)
    producto.mostrar_informacion()