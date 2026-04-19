from fastapi import HTTPException

clientes = []
contador = 1


def get_clientes():
    return clientes


def create_cliente(cliente):
    global contador

    for c in clientes:
        if c["email"] == cliente.email:
            raise HTTPException(
                status_code=400,
                detail="El email ya está registrado"
            )
        
    if cliente.nombre.lower() == "admin":
        raise HTTPException(
            status_code=400,
            detail="Nombre no permitido"
    )    

    nuevo = {
        "id": contador,
        "nombre": cliente.nombre,
        "email": cliente.email
    }

    clientes.append(nuevo)
    contador += 1

    return nuevo

def get_cliente_by_id(id: int):
    for c in clientes:
        if c["id"] == id:
            return c

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


def filter_clientes(nombre: str = None, email: str = None):
    resultado = clientes

    if nombre:
        resultado = [c for c in resultado if nombre.lower() in c["nombre"].lower()]

    if email:
        resultado = [c for c in resultado if email.lower() in c["email"].lower()]

    return resultado