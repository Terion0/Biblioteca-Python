from services.services_libros import services_libros
from services.services_Usuarios import services_Usuarios
from views.view import view  
from sqlmodel import SQLModel, create_engine, Session
from presenter.presenter import presenter

DATABASE_URL = "sqlite:///./Bibliotek.db" 
engine = create_engine(DATABASE_URL)
SessionLocal = Session(bind=engine, autocommit=False, autoflush=False)

def crear_tablas():
    SQLModel.metadata.create_all(bind=engine)

def inicializar_servicios():
    servicios_usuarios = services_Usuarios(SessionLocal)
    servicios_libros = services_libros(SessionLocal)
    return servicios_usuarios, servicios_libros

def main():
  
    crear_tablas()
    servU, servL = inicializar_servicios()
    vista_m = view()  
    presenter_m = presenter(servL, servU, vista_m) 
    
    presenter_m.programaEntero()  

if __name__ == "__main__":
    main()