def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío y tenga al menos 2 caracteres.
    """
    if not nombre or len(nombre.strip()) == 0:
        raise ValueError("El nombre no puede estar vacío")
    if len(nombre.strip()) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres")
    return nombre.strip().title()


def validar_edad(edad):
    """
    Valida que la edad sea un número entre 1 y 120.
    """
    try:
        edad_int = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número válido")
    
    if edad_int < 1 or edad_int > 120:
        raise ValueError("La edad debe estar entre 1 y 120 años")
    
    return edad_int


def validar_email(email):
    """
    Validación básica de email (contiene @ y .)
    """
    if not email or len(email.strip()) == 0:
        raise ValueError("El email no puede estar vacío")
    
    email_limpio = email.strip()
    
    if "@" not in email_limpio or "." not in email_limpio:
        raise ValueError("El email no es válido (debe contener @ y .)")
    
    return email_limpio