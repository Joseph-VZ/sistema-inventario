# Procedimiento de despliegue — Sistema de Inventario

## 1. Requisitos del entorno de ejecución

| Requisito | Valor | Comprobación |
|---|---|---|
| Sistema operativo | Windows 10/11 (local) o Ubuntu (runner `ubuntu-latest` de GitHub Actions) | `uname -a` / `winver` |
| Python | 3.10 o superior, sin librerías externas | `python --version` |
| Herramienta para extraer ZIP | Explorador de Windows / `unzip` | `unzip -v` |
| Acceso al repositorio | Navegador y cuenta de GitHub | — |

Entorno de destino utilizado: **runner de GitHub Actions** (máquina Ubuntu temporal que GitHub crea para cada ejecución). Por indicación de la profesora no se utiliza máquina virtual ni servidor SSH, por lo que no se configuran los secretos `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY` y `DEPLOY_PORT`.

## 2. Versión que se instalará

Paquete publicado en **GitHub Releases** por el workflow `release.yml`: `sistema-inventario-vX.Y.Z.zip` (contiene la carpeta `src/`). No se vuelve a generar: se usa el artefacto publicado.

| Versión | Archivo principal | Contenido |
|---|---|---|
| v1.0.2 | `src/busqueda.py` | Clase Producto y búsqueda por código y por nombre (versión estable) |
| v1.1.0 | `src/main.py` | Menú: registrar, mostrar y buscar productos |

## 3. Descarga del paquete

1. Abrir `https://github.com/Joseph-VZ/sistema-inventario/releases`.
2. En la versión deseada, sección *Assets*, descargar `sistema-inventario-vX.Y.Z.zip`.
3. Guardarlo en la carpeta `despliegue-inventario/`.

## 4. Extracción de archivos

- Windows: clic derecho → *Extraer todo…* o `Expand-Archive sistema-inventario-v1.0.2.zip -DestinationPath .`
- Linux: `unzip sistema-inventario-v1.0.2.zip -d despliegue`

## 5. Configuración necesaria

No requiere variables de entorno, base de datos ni librerías adicionales. Solo es necesario ejecutar el programa desde la carpeta raíz del paquete (la que contiene `src/`).

## 6. Comando para ejecutar el sistema

```
python src/busqueda.py   # v1.0.2
python src/main.py       # v1.1.0
```

## 7. Despliegue automatizado (GitHub Actions)

*Actions → Despliegue del Sistema de Inventario → Run workflow*, escribir la versión (por ejemplo, `v1.0.2`) y ejecutar. El workflow `.github/workflows/deploy.yml`:

1. Descarga el paquete publicado en GitHub Releases.
2. Prepara el entorno de ejecución (Python 3.12) y verifica los requisitos.
3. Crea la carpeta `despliegue/<versión>/` y extrae ahí el paquete.
4. Verifica que estén los archivos necesarios.
5. Ejecuta el sistema y comprueba que muestre los productos (en v1.1.0 registra, muestra y busca un producto).
6. Publica un resumen del despliegue y conserva la carpeta desplegada como artefacto.

La opción **simular_falla** elimina `src/Producto.py` antes de ejecutar el sistema, para reproducir un despliegue defectuoso.

## 8. Comprobación del funcionamiento

- El job termina en verde (✓).
- El paso *Ejecutar y verificar* muestra los datos de los productos (código, nombre, precio, existencia).
- El *Summary* de la ejecución muestra la versión, el resultado y la salida del programa.
- Localmente: `python src/busqueda.py` muestra los productos sin errores.

## 9. Recuperación de la versión anterior (rollback)

Si la versión desplegada falla:

1. Ir a *Actions → Despliegue del Sistema de Inventario → Run workflow*.
2. Escribir la versión estable anterior (`v1.0.2`) y dejar *simular_falla* desactivado.
3. Ejecutar y comprobar que el job termina en verde y que el programa muestra los productos.

Esto funciona porque cada versión liberada se conserva como paquete en GitHub Releases. Localmente basta con volver a extraer `sistema-inventario-v1.0.2.zip`.

## 10. Problemas frecuentes

| Problema | Causa | Solución |
|---|---|---|
| `python: command not found` | Python no instalado | Instalar Python 3.10+ / paso `setup-python` |
| `ModuleNotFoundError: No module named 'Producto'` | Falta un archivo o se ejecuta desde otra carpeta | Ejecutar desde la raíz del paquete; volver a extraer el ZIP o desplegar la versión anterior |
| `can't open file 'src/main.py'` | La versión no incluye ese archivo (v1.0.x) | Usar `src/busqueda.py` |
| `Release not found` / `Asset not found` | Tag o nombre de archivo incorrecto | Revisar la versión exacta en Releases |
| El botón *Run workflow* no aparece | `deploy.yml` no está en la rama `main` | Hacer push del archivo a `main` |
| Caracteres raros (acentos) en Windows | Codificación de la consola | `chcp 65001` |
