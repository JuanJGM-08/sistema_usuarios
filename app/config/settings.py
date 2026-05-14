import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Settings:
    """
    Clase para gestionar la configuración de la aplicación
    usando variables de entorno.
    """
    
    APP_NAME = os.getenv("APP_NAME", "Sistema Usuarios")
    APP_VERSION = os.getenv("APP_VERSION", "1.0")
    ADMIN_USER = os.getenv("ADMIN_USER", "admin")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
    
    @classmethod
    def show_config(cls):
        """Muestra la configuración actual del sistema"""
        print("\n=== CONFIGURACIÓN DEL SISTEMA ===")
        print(f"App Name: {cls.APP_NAME}")
        print(f"App Version: {cls.APP_VERSION}")
        print(f"Admin User: {cls.ADMIN_USER}")
        print(f"Admin Email: {cls.ADMIN_EMAIL}")
        print("===================================\n")