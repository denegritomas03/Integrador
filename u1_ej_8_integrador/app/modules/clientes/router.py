from fastapi import APIRouter
from typing import List, Optional
from .schemas import ClienteCreate, ClienteResponse
from .service import get_clientes, create_cliente, get_cliente_by_id, filter_clientes

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/", response_model=List[ClienteResponse])
def listar(nombre: Optional[str] = None, email: Optional[str] = None):
    if nombre or email:
        return filter_clientes(nombre, email)
    return get_clientes()


@router.post("/", response_model=ClienteResponse, status_code=201)
def crear(cliente: ClienteCreate):
    return create_cliente(cliente)


@router.get("/{id}", response_model=ClienteResponse)
def obtener(id: int):
    return get_cliente_by_id(id)