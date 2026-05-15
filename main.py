import sys
import os

# Agregar el directorio actual al path para poder importar los módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.config.settings import Settings
from app.usuarios.gestor import GestorUsuarios


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "=" * 50)
    print(f"  {Settings.APP_NAME} v{Settings.APP_VERSION}")
    print("=" * 50)
    print("1. Registrar usuario")
    print("2. Listar todos los usuarios")
    print("3. Buscar usuario por nombre")
    print("4. Buscar usuario por email")
    print("5. Mostrar configuración del sistema")
    print("6. Salir")
    print("-" * 50)


def main():
    """Función principal del sistema"""
    gestor = GestorUsuarios()
    
    print(f"\n✅ Bienvenido al {Settings.APP_NAME}")
    print(f"📧 Administrador: {Settings.ADMIN_EMAIL}")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            # Registrar usuario
            print("\n--- REGISTRO DE USUARIO ---")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            email = input("Email: ")
            
            try:
                usuario = gestor.registrar_usuario(nombre, edad, email)
                print(f"\n✅ Usuario registrado exitosamente: {usuario['nombre']}")
            except ValueError as e:
                print(f"\n❌ Error: {e}")
        
        elif opcion == "2":
            # Listar usuarios
            print("\n--- LISTA DE USUARIOS ---")
            usuarios = gestor.listar_usuarios()
            if not usuarios:
                print("📭 No hay usuarios registrados aún.")
            else:
                print(f"Total: {gestor.total_usuarios()} usuarios\n")
                for i, u in enumerate(usuarios, 1):
                    print(f"{i}. {u['nombre']} | {u['edad']} años | {u['email']}")
        
        elif opcion == "3":
            # Buscar por nombre
            print("\n--- BÚSQUEDA POR NOMBRE ---")
            nombre = input("Ingrese el nombre (o parte) a buscar: ")
            resultados = gestor.buscar_por_nombre(nombre)
            
            if not resultados:
                print(f"❌ No se encontraron usuarios con: '{nombre}'")
            else:
                print(f"✅ Se encontraron {len(resultados)} usuario(s):")
                for u in resultados:
                    print(f"   • {u['nombre']} | {u['edad']} años | {u['email']}")
        
        elif opcion == "4":
            # Buscar por email
            print("\n--- BÚSQUEDA POR EMAIL ---")
            email = input("Ingrese el email exacto: ")
            usuario = gestor.buscar_por_email(email)
            
            if usuario:
                print(f"✅ Usuario encontrado:")
                print(f"   Nombre: {usuario['nombre']}")
                print(f"   Edad: {usuario['edad']} años")
                print(f"   Email: {usuario['email']}")
            else:
                print(f"❌ No se encontró usuario con email: '{email}'")
        
        elif opcion == "5":
            # Mostrar configuración
            Settings.show_config()
        
        elif opcion == "6":
            print(f"\n👋 Gracias por usar {Settings.APP_NAME}. ¡Hasta luego!")
            break
        
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()