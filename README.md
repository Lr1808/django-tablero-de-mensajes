# Tablero de Mensajes (Django)

Este proyecto es una aplicación web simple construida con Django que muestra un tablero de mensajes (message board) y un modelo adicional de ejemplo para productos. Su objetivo principal es servir como una aplicación didáctica para entender cómo funcionen los modelos, vistas basadas en clases (Class Based Views), plantillas y el panel de administración de Django.

## Contrato breve
- Entrada: posts (objetos `Posr`) almacenados en la base de datos SQLite incluida.
- Salida: página principal que lista los posts (`/`) usando la plantilla `home.html`.
- Error: la app asume que la base de datos y las migraciones están aplicadas; si faltan migraciones, Django mostrará errores hasta que se ejecuten.

## Pila tecnológica
- Python 3.x
- Django 5.2.7 (ver `requirements.txt`)
- Base de datos por defecto: SQLite (`db.sqlite3`)

## Requisitos
- Tener Python 3 instalado.
- Es recomendable crear y usar un entorno virtual (venv).

## Instalación (Windows - PowerShell)
1. Clonar o colocar el repositorio en una carpeta local.
2. Abrir PowerShell y situarse en la carpeta del proyecto (la que contiene `manage.py`).
3. Crear y activar un entorno virtual (opcional, recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

5. Aplicar migraciones:

```powershell
python manage.py migrate
```

6. (Opcional) Crear un superusuario para acceder al admin:

```powershell
python manage.py createsuperuser
```

7. Ejecutar el servidor de desarrollo:

```powershell
python manage.py runserver
```

Luego abrir http://127.0.0.1:8000/ en el navegador para ver la página principal.

## Uso
- Ruta principal `/`: muestra la lista de posts creados (modelo `Posr`).
- Panel de administración `/admin/`: permite crear/editar `Posr` y `product` si se ha creado un superusuario.

## Estructura principal del proyecto
- `manage.py` - script de gestión de Django.
- `django_project/` - configuración del proyecto (settings, urls, wsgi/asgi).
- `django_app/` - aplicación principal con modelos, vistas y configuración de admin.
	- `models.py` - define los modelos `Posr` y `product`.
	- `views.py` - contiene `HomeView` (ListView) que provee `all_posts_list` a la plantilla `home.html`.
	- `urls.py` - mapea la ruta raíz al `HomeView`.
	- `admin.py` - registra `Posr` y `product` en el admin.
- `templates/home.html` - plantilla que muestra la lista de posts.
- `db.sqlite3` - base de datos SQLite (si existe en el repo).

## Modelos (resumen)
- `Posr`:
	- `text` (TextField): contenido del post.
	- Método `__str__` devuelve los primeros 50 caracteres del texto.
	- Nota: el nombre de la clase es `Posr` en el código; probablemente se quería `Post` pero funciona tal como está.

- `product`:
	- `name` (CharField)
	- `price` (DecimalField)
	- `description` (TextField)
	- Este modelo parece un ejemplo/demo y también está registrado en el admin.

## Vistas y plantillas
- `HomeView` (ListView): carga todos los objetos `Posr` y los pasa a `home.html` como `all_posts_list`.
- `templates/home.html` itera `all_posts_list` y muestra cada post en una lista.

## Administración
Los modelos `Posr` y `product` están registrados en el panel de administración (ver `django_app/admin.py`). Una vez creado un superusuario se puede gestionar contenido desde `/admin/`.

## Pruebas
Si se añaden tests en `django_app/tests.py`, se pueden ejecutar con:

```powershell
python manage.py test
```

## Sugerencias y mejoras
- Corregir el nombre `Posr` a `Post` si se desea consistencia.
- Añadir formularios y vistas CRUD (crear/editar/eliminar posts desde la interfaz pública).
- Añadir paginación y validación de entradas.
- Añadir internacionalización y estilos CSS para una mejor UI.

## Contribuir
Si quieres contribuir, crea un fork, añade cambios y abre un pull request. Para cambios significativos, crea primero un issue describiendo la propuesta.

## Licencia
Incluye una licencia si deseas permitir uso/redistribución (no se ha incluido una en este repositorio por defecto).

---

Si quieres, puedo:
- Añadir instrucciones para desplegar en producción (Gunicorn + Nginx).
- Añadir ejemplos de datos iniciales o un archivo `fixtures`.
- Corregir automáticamente el nombre del modelo `Posr` a `Post` y propagar cambios (con migración).

Indícame qué prefieres y lo hago.

