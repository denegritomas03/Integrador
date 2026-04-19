from pydantic import BaseModel, EmailStr, Field

class ClienteCreate(BaseModel):
    nombre: str = Field(min_length=3)
    email: EmailStr

class ClienteResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr