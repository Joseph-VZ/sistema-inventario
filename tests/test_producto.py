"""Pruebas unitarias de la clase Producto (src/Producto.py).

Ejecutar desde la raíz del proyecto:
    python -m unittest discover -s tests -v
"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

# Permite importar Producto desde la carpeta src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from Producto import Producto  # noqa: E402


def capturar_salida(producto):
    """Ejecuta mostrar_informacion() y devuelve lo que imprime."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        producto.mostrar_informacion()
    return buffer.getvalue()


class TestProducto(unittest.TestCase):

    def setUp(self):
        # Datos de entrada de CP01
        self.producto = Producto("P001", "Teclado", 350, 10)

    # 1. Crear un producto con los datos solicitados (CP01)
    def test_cp01_crear_producto(self):
        self.assertIsInstance(self.producto, Producto)
        self.assertEqual(self.producto.codigo, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertEqual(self.producto.precio, 350)
        self.assertEqual(self.producto.existencia, 10)

    # 2. El código se conserva y se muestra (CP02)
    def test_cp02_codigo(self):
        self.assertEqual(self.producto.codigo, "P001")
        self.assertIn("Código:     P001", capturar_salida(self.producto))

    # 3. El nombre corresponde al producto creado (CP03)
    def test_cp03_nombre(self):
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertIn("Nombre:     Teclado", capturar_salida(self.producto))

    # 4. El precio se almacena y se muestra correctamente (CP04)
    def test_cp04_precio(self):
        self.assertEqual(self.producto.precio, 350)
        # El método da formato de moneda con dos decimales
        self.assertIn("Precio:     $350.00", capturar_salida(self.producto))

    # 5. La existencia coincide con el valor proporcionado (CP05)
    def test_cp05_existencia(self):
        self.assertEqual(self.producto.existencia, 10)
        self.assertIn("Existencia: 10 unidades", capturar_salida(self.producto))

    # 6. El método muestra toda la información (CP06)
    def test_cp06_mostrar_informacion_completa(self):
        esperado = (
            "Producto disponible\n"
            "Código:     P001\n"
            "Nombre:     Teclado\n"
            "Precio:     $350.00\n"
            "Existencia: 10 unidades\n"
        )
        self.assertEqual(capturar_salida(self.producto), esperado)

    # Crear un segundo producto sin confundir sus datos (CP07)
    def test_cp07_segundo_producto_independiente(self):
        producto2 = Producto("P002", "Mouse", 180, 5)

        self.assertEqual(producto2.codigo, "P002")
        self.assertEqual(producto2.nombre, "Mouse")
        self.assertEqual(producto2.precio, 180)
        self.assertEqual(producto2.existencia, 5)

        salida2 = capturar_salida(producto2)
        self.assertIn("Código:     P002", salida2)
        self.assertIn("Precio:     $180.00", salida2)
        self.assertNotIn("P001", salida2)

        # El primer producto no debe haber cambiado
        self.assertEqual(self.producto.codigo, "P001")
        self.assertEqual(self.producto.nombre, "Teclado")
        self.assertEqual(self.producto.precio, 350)
        self.assertEqual(self.producto.existencia, 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
