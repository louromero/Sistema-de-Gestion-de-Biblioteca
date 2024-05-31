import pickle
from typing import Dict, List

# CREACION DE CLASES
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = 1

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros_prestados: List[str] = []

class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.cargar_datos()

    # AGREGAR LIBRO
    def agregar_libro(self, titulo: str, autor: str):
        # Si el libro ya esta agregado se suma +1
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor)
        print(f'\nLibro "{titulo}" agregado correctamente!')

    # MOSTRAR LIBROS
    def mostrar_libros(self):
        for libro in self.libros.values():
            if libro.cantidad > 0: 
                print(f'\nTítulo: {libro.titulo}')
                print(f"Autor: {libro.autor}")
                print(f"Cantidad: {libro.cantidad}")
                print(f"Disponibilidad: Disponible")
            else:
                print("\nNo hay libros Disponibles")
            

    # PRESTAR LIBRO
    def prestar_libro(self, titulo: str, nombre_usuario: str):
        if titulo not in self.libros:
            print(f'\nEl libro "{titulo}" no está disponible en la biblioteca.')
            return
        if nombre_usuario not in self.usuarios:
            print(f'\nEl usuario "{nombre_usuario}" no está registrado.')
            return
        libro = self.libros[titulo]
        if libro.cantidad > 0:
            libro.cantidad -= 1
            self.usuarios[nombre_usuario].libros_prestados.append(titulo)
            print(f'\nLibro "{titulo}" prestado a: {nombre_usuario}.')
        else:
            print(f'\nEl libro "{titulo}" no está disponible actualmente.')

    # REGISTRAR NUEVO USUARIO
    def registrar_usuario(self, nombre: str):
        if nombre in self.usuarios:
            print(f'\nEl usuario "{nombre}" ya está registrado.')
        else:
            self.usuarios[nombre] = Usuario(nombre)
            print(f'\nUsuario "{nombre}" registrado correctamente.')

    # GUARDAR DATOS
    def guardar_datos(self):
        with open('datos_biblioteca.pkl', 'wb') as file:
            pickle.dump({'libros': self.libros, 'usuarios': self.usuarios}, file)
        print('\nDatos de la biblioteca guardados correctamente!')

    # CARGAMOS DATOS DE LA BIBLIOTECA
    def cargar_datos(self):
        try:
            with open('datos_biblioteca.pkl', 'rb') as file:
                datos = pickle.load(file)
                self.libros = datos['libros']
                self.usuarios = datos['usuarios']
            print('Datos de la biblioteca cargados!')
        except FileNotFoundError:
            print('No se encontraron datos previos, inicializando biblioteca vacía.')

    # LISTAR USUARIOS
    def listar_usuarios(self):
        print("\nUsuarios:")
        for usuario in self.usuarios.values():
            print(f' - {usuario.nombre}')

    # LISTAR LIBROS DE UN USUARIO
    def listar_libros_de_usuario(self, nombre_usuario: str):
        if nombre_usuario not in self.usuarios:
            print(f'\nEl usuario "{nombre_usuario}" no está registrado.')
            return
        usuario = self.usuarios[nombre_usuario]
        if usuario.libros_prestados:
            print(f'\nLibros prestados a {nombre_usuario}: ')
            print(f"{"\n - ".join(usuario.libros_prestados)}")
        else:
            print(f'\nEl usuario "{nombre_usuario}" no tiene libros prestados.')

    # DEVOLVER LIBRO
    def devolver_libro(self, titulo: str, nombre_usuario: str):
        if nombre_usuario not in self.usuarios:
            print(f'\nEl usuario "{nombre_usuario}" no está registrado.')
            return
        usuario = self.usuarios[nombre_usuario]
        if titulo in usuario.libros_prestados:
            usuario.libros_prestados.remove(titulo)
            self.libros[titulo].cantidad += 1
            print(f'\nLibro "{titulo}" devuelto por {nombre_usuario}.')
        else:
            print(f'\nEl usuario "{nombre_usuario}" no tiene prestado el libro: "{titulo}".')