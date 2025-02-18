from sqlmodel import Session
from models.models import libro , usuario
from repositories.rlibros import rlibros

class services_libros:

    def __init__(self, session: Session):
        self.session = session
        self.repositorio_libros = rlibros(session)

    def registrar_libro(self, libro: libro):
        if self.repositorio_libros.obtener_libro_por_isbn(libro.ISBN):
            return "El libro con este ISBN ya existe."
        else :
            self.repositorio_libros.agregar_libro(libro)
            return "Libro registrado correctamente."

    def listar_libros(self):
        return self.repositorio_libros.obtener_libros()

    def buscar_libro(self, isbn: int):
        libro = self.repositorio_libros.obtener_libro_por_isbn(isbn)
        if not libro:
            raise ValueError("Libro no encontrado.")
        return libro

    def modificar_libro(self, libro: libro):
        self.repositorio_libros.actualizar_libro(libro)
       

    def eliminar_libro(self, libro: libro):
        if libro.prestado:
            return "No se puede eliminar un libro que está prestado."
        if self.repositorio_libros.eliminar_libro(libro.ISBN):
            return f"Libro {libro.titulo} eliminado correctamente."
        else:
            return "No se pudo eliminar el libro."
        

    def obtener_libros_no_prestados(self):
        """Devuelve la lista de libros no prestados."""
        return self.repositorio_libros.obtener_libros_no_prestados()    