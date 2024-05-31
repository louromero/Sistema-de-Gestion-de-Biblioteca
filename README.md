# SISTEMA DE GESTIÓN DE BIBLIOTECA

## Descripción

Este proyecto es un sistema de gestión de biblioteca que proporciona funcionalidades para administrar libros y usuarios. Está diseñado para facilitar el manejo de una biblioteca pequeña o mediana, permitiendo registrar y prestar libros, así como gestionar la información de los usuarios.

## Clases Principales

- **Clases `Libro` y `Usuario`**: Modelan los datos de los libros y los usuarios respectivamente.

- **Clase `Biblioteca`**: Contiene los métodos para gestionar la biblioteca, incluyendo agregar libros, prestar libros, registrar usuarios, guardar y cargar datos, y listar libros y usuarios.

## Métodos Principales: 

- **agregar_libro**: Agrega un libro nuevo o incrementa la cantidad de un libro existente.
- **mostrar_libros**: Muestra todos los libros disponibles en la biblioteca junto con su disponibilidad.
- **prestar_libro**: Permite prestar un libro a un usuario registrado si el libro está disponible.
- **registrar_usuario**: Registra un nuevo usuario en el sistema.
- **guardar_datos**: Guarda el estado actual de la biblioteca en un archivo utilizando el módulo `pickle` para la serialización.
- **cargar_datos**: Carga el estado de la biblioteca desde un archivo previamente guardado.
- **listar_usuarios**: Lista todos los usuarios registrados en la biblioteca.
- **listar_libros_de_usuario**: Lista todos los libros que un usuario específico ha prestado.
- **devolver_libro**: Permite a un usuario devolver un libro que ha prestado.

## Manejo de Archivos

El sistema utiliza el módulo `pickle` para serializar y deserializar los datos de la biblioteca, lo que permite guardar y cargar el estado del sistema de manera persistente.

## Funcionalidades

1. **Agregar Libro**
   - Permite agregar un nuevo libro a la biblioteca o incrementar la cantidad de un libro existente.

2. **Mostrar Libros**
   - Muestra todos los libros disponibles en la biblioteca junto con su cantidad disponible.

3. **Prestar Libro**
   - Permite prestar un libro a un usuario registrado si el libro está disponible.

4. **Registrar Usuario**
   - Permite registrar un nuevo usuario en el sistema.

5. **Guardar Datos**
   - Guarda el estado actual de la biblioteca en un archivo para su posterior recuperación.

6. **Cargar Datos**
   - Carga el estado de la biblioteca desde un archivo previamente guardado.

7. **Listar Usuarios**
   - Lista todos los usuarios registrados en la biblioteca.

8. **Listar Libros de Usuario**
   - Lista todos los libros que un usuario específico ha prestado.

9. **Devolver Libro**
   - Permite a un usuario devolver un libro prestado a la biblioteca.

## Uso

Este sistema de gestión de biblioteca proporciona una base sólida para administrar los libros y usuarios de una biblioteca. Se pueden agregar funcionalidades adicionales según sea necesario.

## Requisitos

- Python 3.x

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/louromero/Sistema-de-Gestion-de-Biblioteca.git
   ```

2. Navegar al directorio del proyecto:

   ```bash
   cd sistema-gestion-biblioteca
   ```

3. Ejecutar el script principal:

   ```bash
   python main.py
   ```
