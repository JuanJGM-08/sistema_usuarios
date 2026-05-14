from . import validaciones as val

class GestorUsuarios:
    """
    Clase para gestionar el registro, listado y búsqueda de usuarios.
    """
    
    def __init__(self):
        # Lista de diccionarios para almacenar usuarios
        self.usuarios = []
    
    def registrar_usuario(self, nombre, edad, email):
        """
        Registra un nuevo usuario después de validar los datos.
        Retorna el usuario registrado.
        """
        try:
            nombre_validado = val.validar_nombre(nombre)
            edad_validada = val.validar_edad(edad)
            email_validado = val.validar_email(email)
        except ValueError as e:
            raise e
        
        usuario = {
            "nombre": nombre_validado,
            "edad": edad_validada,
            "email": email_validado
        }
        
        self.usuarios.append(usuario)
        return usuario
    
    def listar_usuarios(self):
        """
        Retorna la lista completa de usuarios.
        """
        return self.usuarios.copy()
    
    def buscar_por_nombre(self, nombre):
        """
        Busca usuarios que coincidan parcialmente con el nombre.
        """
        nombre_busqueda = nombre.strip().lower()
        resultados = []
        
        for usuario in self.usuarios:
            if nombre_busqueda in usuario["nombre"].lower():
                resultados.append(usuario)
        
        return resultados
    
    def buscar_por_email(self, email):
        """
        Busca un usuario por email exacto.
        """
        email_busqueda = email.strip().lower()
        
        for usuario in self.usuarios:
            if usuario["email"].lower() == email_busqueda:
                return usuario
        
        return None
    
    def total_usuarios(self):
        """
        Retorna el número total de usuarios registrados.
        """
        return len(self.usuarios)