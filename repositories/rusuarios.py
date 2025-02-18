from sqlmodel import Session, select
from models.models import usuario

class rusuarios:

    def __init__(self, session: Session):
        self.session = session

    def agregar_usuario(self, usuario: usuario):
        """Agrega un nuevo usuario a la base de datos."""
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def obtener_usuarios(self):
        """Obtiene todos los usuarios."""
        return self.session.exec(select(usuario)).all()

    def obtener_usuario_por_dni(self, dni: int):
        """Obtiene un usuario por su DNI."""
        return self.session.exec(select(usuario).where(usuario.dni == dni)).first()

    def eliminar_usuario(self, dni: int):
        """Elimina un usuario por su DNI."""
        usuario = self.obtener_usuario_por_dni(dni)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return True
        return False

    def actualizar_usuario(self, usuario : usuario):
          self.session.commit()
          self.session.refresh(usuario)

    