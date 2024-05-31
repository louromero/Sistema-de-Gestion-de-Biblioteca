from biblioteca import Biblioteca
import os

# FUNCION PARA LIMPIAR TERMINAL
def screen_step():
    os.system('cls' if os.name=='nt' else 'clear')
    
def main():
    biblioteca = Biblioteca()

    while True:
        print("\n------------- MENU -------------------")
        print("1. Agregar Libro")
        print("2. Mostrar Libros")
        print("3. Prestar Libro")
        print("4. Registrar Usuario")
        print("5. Guardar Datos")
        print("6. Listar Usuarios")
        print("7. Listar Libros de Usuarios")
        print("8. Devolver Libro")
        print("9. Salir")
        print("----------------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            screen_step()
            biblioteca.agregar_libro(titulo, autor)
            
        elif opcion == '2':
            screen_step()
            biblioteca.mostrar_libros()
            
        elif opcion == '3':
            titulo = input("Ingrese el título del libro: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            screen_step()
            biblioteca.prestar_libro(titulo, nombre_usuario)
            
        elif opcion == '4':
            nombre = input("Ingrese el nombre del usuario: ")
            screen_step()
            biblioteca.registrar_usuario(nombre)
            
        elif opcion == '5':
            screen_step()
            biblioteca.guardar_datos()
            
        elif opcion == '6':
            screen_step()
            biblioteca.listar_usuarios()
            
        elif opcion == '7':
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            screen_step()
            biblioteca.listar_libros_de_usuario(nombre_usuario)
            
        elif opcion == '8':
            titulo = input("Ingrese el título del libro: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            screen_step()
            biblioteca.devolver_libro(titulo, nombre_usuario)
            
        elif opcion == '9':
            screen_step()
            biblioteca.guardar_datos()
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()