from sqlmodel import Session
from models.models import usuario
from repositories.rusuarios import rusuarios

class services_Usuarios:

    def __init__(self, session: Session):
        self.session = session
        self.repositorio_usuarios = rusuarios(session)

    def registrar_usuario(self, usuario: usuario):
        if self.repositorio_usuarios.obtener_usuario_por_dni(usuario.dni):
            return "El usuario con este DNI ya existe."
        else :
            self.repositorio_usuarios.agregar_usuario(usuario)
            return "Usuario registrado con éxito."

    def listar_usuarios(self):
        return self.repositorio_usuarios.obtener_usuarios()

    def buscar_usuario(self, dni: int):
        usuario = self.repositorio_usuarios.obtener_usuario_por_dni(dni)
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        return usuario

    def modificar_usuario(self, usuario: usuario):
        self.repositorio_usuarios.actualizar_usuario(usuario)
      

    def eliminar_usuario(self, usuario: usuario):
        if  len(usuario.libros) > 0:
            return "No se puede eliminar un usuario con libros prestados."
        if len(usuario.libros) == 0:
           if self.repositorio_usuarios.eliminar_usuario(usuario.dni):
               return f"Usuario {usuario.nombre} eliminado correctamente."
        else:
            return "No se pudo eliminar el usuario."