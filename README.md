# Bloodia Regression Testing

Este repositorio contiene un conjunto de pruebas funcionales de regresión para el sitio web estático `Bloodia`.

## Descripción

Las pruebas verifican el comportamiento clave de la aplicación, incluyendo:
- Apertura del menú móvil
- Navegación entre páginas
- Retorno al inicio mediante el logo
- Carga correcta de imágenes
- Validación de enlaces internos

## Requisitos

- Python 3.10 o superior.
- Google Chrome instalado

## Instalación

1. Crear un entorno virtual opcional:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## URL de GitHub Pages

El sitio Bloodia está disponible en GitHub Pages. Las pruebas usan por defecto la URL del sitio desplegado.

Para ejecutar las pruebas contra esa URL, no es necesario levantar un servidor local.

## Ejecutar las pruebas

Para ejecutar todos los tests:

```bash
pytest tests -v
```

Para ejecutar los tests en modo headless (sin UI de Chrome):

```bash
pytest tests -v --headless
```


## Estructura del proyecto

- `index.html` - Página principal
- `imagenes.html` - Página de galería
- `vocabulario.html` - Página de vocabulario
- `bibliografia.html` - Página de bibliografía
- `tests/` - Pruebas de regresión
  - `conftest.py` - Configuración de Pytest y Selenium
  - `test_bloodia_regression.py` - Casos de prueba
- `requirements.txt` - Dependencias para ejecutar las pruebas

## Resultados de errores

Si un test falla, el fixture `driver` guarda una captura de pantalla con el nombre `failure_<nombre_del_test>.png` en la raíz del proyecto.
