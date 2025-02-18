from sqlmodel import SQLModel, Field, Relationship 
from typing import List, Optional



class libro(SQLModel, table=True):
    ISBN: int = Field(primary_key=True)
    titulo: str
    autor: str
    genero: str
    portada: str
    sinopsis: str
    prestado: bool = Field(default=False)

    usuario_dni: Optional[int] = Field(default=None, foreign_key="usuario.dni")
    usuario: Optional["usuario"] = Relationship(back_populates="libros")

class usuario(SQLModel, table=True):
    dni: int = Field(primary_key=True)
    nombre: str
    correo_electronico: str
    telefono: str
    domicilio: str

    libros: List[libro] = Relationship(back_populates="usuario")