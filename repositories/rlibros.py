from sqlmodel import Session, select
from models.models import libro

class rlibros:

    def __init__(self, session: Session):
        self.session = session

    def agregar_libro(self, libro: libro):
        """Agrega un nuevo libro a la base de datos."""
        self.session.add(libro)
        self.session.commit()
        self.session.refresh(libro)
        return libro

    def obtener_libros(self):
        """Obtiene todos los libros."""
        return self.session.exec(select(libro)).all()
    
    def obtener_libros_no_prestados(self):
                return self.session.exec(select(libro).where(libro.prestado == False)).all()


    def obtener_libro_por_isbn(self, isbn: int):
        """Obtiene un libro por su ISBN."""
        return self.session.exec(select(libro).where(libro.ISBN == isbn)).first()

    def eliminar_libro(self, isbn: int):
        """Elimina un libro por su ISBN."""
        libro = self.obtener_libro_por_isbn(isbn)
        if libro:
            self.session.delete(libro)
            self.session.commit()
            return True
        return False

    def actualizar_libro(self, libro: libro):
            self.session.commit()
            self.session.refresh(libro)

   
