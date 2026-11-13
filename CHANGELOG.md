# Registro de cambios

Todos los cambios importantes del Sistema de Inventario se documentan en este archivo.

## [v1.0.2] - 2026-11-12

### Corregido
- Corregido el error en la visualización del precio de los productos.
- Se restauró la presentación del precio almacenado originalmente.

### Pruebas
- 7 de 7 pruebas unitarias satisfactorias.
- Workflow de liberación ejecutado correctamente.
- Paquete ZIP generado y publicado en GitHub Releases.

## [v1.0.1] - 2026-11-12

### Validación de errores
- Se introdujo intencionalmente un error en la visualización del precio.
- 3 pruebas unitarias detectaron el error.
- El workflow de GitHub Actions falló durante la ejecución de las pruebas.
- La versión no fue publicada debido al fallo de validación.

## [v1.0.0] - 2026-11-12

### Agregado
- Clase Producto para representar productos del inventario.
- Método mostrar_informacion() para mostrar los datos de cada producto.
- Funcionalidad de búsqueda de productos por código exacto.
- Búsqueda de productos por nombre sin distinguir mayúsculas y minúsculas.
- Pruebas unitarias para validar la funcionalidad del sistema.
- Workflow de GitHub Actions para ejecutar pruebas y generar paquetes de distribución.

### Pruebas
- 7 de 7 pruebas unitarias satisfactorias.
- Liberación automatizada ejecutada correctamente.
- Paquete ZIP generado y publicado en GitHub Releases.