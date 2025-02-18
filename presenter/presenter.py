from models.models import libro, usuario

class presenter :
  
      def __init__(self, serviceLib, serviceUser, view):
        self.services_libros = serviceLib
        self.services_usuarios = serviceUser
        self.view_main =  view
  
      def mostrar_menu(self) :
          self.view_main.mostrar_mensaje("0-Alta de socio")
          self.view_main.mostrar_mensaje("1-Baja de socio")
          self.view_main.mostrar_mensaje("2-Alta de libro")
          self.view_main.mostrar_mensaje("3-Baja de libro")
          self.view_main.mostrar_mensaje("4-Prestar libro")
          self.view_main.mostrar_mensaje("5-Devolver libro")
          self.view_main.mostrar_mensaje("6-Consultar libros")
          self.view_main.mostrar_mensaje("7-Consultar usuarios")
          self.view_main.mostrar_mensaje("8-Salir")

      def elegir_opcion(self)    :
          return self.view_main.devolver_dato("Introduce opción :  ") 
      
      def  menu_opciones(self, opcion) :
            if opcion == "0" :
                 self.alta_socio()
            if opcion == "1" : 
                 self.baja_socio()
            elif opcion =="2" :
                 self.alta_libro()
            elif opcion =="3" :  
                 self.baja_libro()
            elif opcion =="4" :  
                 self.prestar_libro()
            elif opcion =="5" :  
                 self.devolver_libro() 
            elif opcion =="6" :   
                self.listar_libros()
            elif opcion =="7" :
                 self.listar_usuarios()
            elif opcion =="8" :                   
                self.view_main.mostrar_mensaje("Fin de programa")     
            else :
               self.view_main.mostrar_mensaje("Opción no válida")

      def alta_socio(self):
        dni = self.view_main.devolver_dato("Ingrese DNI: ")
        nombre = self.view_main.devolver_dato("Ingrese nombre: ")
        correo = self.view_main.devolver_dato("Ingrese correo electrónico: ")
        telefono = self.view_main.devolver_dato("Ingrese teléfono: ")
        domicilio = self.view_main.devolver_dato("Ingrese domicilio: ")
        usuario_generado = usuario(
            dni=int(dni), 
            nombre=nombre, 
            correo_electronico=correo,
            telefono=telefono, 
            domicilio=domicilio)  
        try:
            mensaje = self.services_usuarios.registrar_usuario(usuario_generado)
            self.view_main.mostrar_mensaje(mensaje)
        except ValueError as e:
            self.view_main.mostrar_mensaje(e)

      def baja_socio(self):

        dni = self.view_main.devolver_dato("Ingrese DNI del usuario a eliminar: ")
        try:
            usuario = self.services_usuarios.buscar_usuario(int(dni))
            if usuario:
               mensaje = self.services_usuarios.eliminar_usuario(usuario)
               self.view_main.mostrar_mensaje(mensaje)
        except ValueError as e:
            self.view_main.mostrar_mensaje(e)

      def alta_libro(self):
            isbn = self.view_main.devolver_dato("Introduce ISBN: ")
            titulo = self.view_main.devolver_dato("Introduce título: ")
            autor = self.view_main.devolver_dato("Introduce autor: ")
            genero = self.view_main.devolver_dato("Introduce género: ")
            portada = self.view_main.devolver_dato("Introduce URL de portada: ")
            sinopsis = self.view_main.devolver_dato("Introduce sinopsis: ")
            libroAgenerar = libro(
                   ISBN=isbn,
                   titulo=titulo,
                   autor=autor,
                   genero=genero,
                   portada=portada,
                   sinopsis=sinopsis,)
            try:
                mensaje =self.services_libros.registrar_libro(libroAgenerar)
                self.view_main.mostrar_mensaje(mensaje)
            except ValueError as e:
                self.view_main.mostrar_mensaje(e)

      def baja_libro(self):
         """Elimina un libro."""
         isbn = self.view_main.devolver_dato("Ingrese ISBN del libro a eliminar: ")
         try:
            libro = self.services_libros.buscar_libro(int(isbn))
            mensaje= self.services_libros.eliminar_libro(libro)
            self.view_main.mostrar_mensaje(mensaje)
         except ValueError as e:
               self.view_main.mostrar_mensaje(e)

      def listar_libros(self):
          libros = self.services_libros.listar_libros()
          if libros:
             for libro in libros:
                 self.view_main.mostrar_mensaje(libro.titulo)
          else: 
              self.view_main.mostrar_mensaje("No hay libros registrados.")

              
      def listar_usuarios(self):
          usuarios = self.services_usuarios.listar_usuarios()
          if usuarios:
             for usuario in usuarios:
                 self.view_main.mostrar_mensaje(usuario.nombre)  
          else:
              self.view_main.mostrar_mensaje("No hay usuarios registrados.")      

      def mostrar_libros_no_prestados(self):
            libros = self.services_libros.obtener_libros_no_prestados()
            for libro in libros:
                self.view_main.mostrar_mensaje(f"{libro.ISBN} - {libro.titulo} de {libro.autor}")
         
      def prestar_libro(self):
        try:
            dni = self.view_main.devolver_dato("Introduce DNI del usuario: ")
            usuario = self.services_usuarios.buscar_usuario(dni)
            if usuario:
                self.mostrar_libros_no_prestados()     
                isbn = self.view_main.devolver_dato("Introduce ISBN del libro a prestar: ")
                libro = self.services_libros.buscar_libro(isbn)
                if libro.prestado == False:              
                      libro.prestado = True
                      libro.usuario_dni = usuario.dni       
                      self.services_libros.modificar_libro(libro)
                      print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
                else:
                    raise ValueError("El libro no está disponible para préstamo.")
            else:  
                    raise ValueError("Usuario no encontrado.")
        except ValueError as e:
            self.view_main.mostrar_mensaje(e)
    


      def devolver_libro(self):
         try:
             dni = self.view_main.devolver_dato("Introduce DNI del usuario: ")
             usuario = self.services_usuarios.buscar_usuario(dni)
             if usuario:
               if usuario.libros: 
                self.view_main.mostrar_mensaje("Libros del usuario:")
                for libro in usuario.libros:
                    self.view_main.mostrar_mensaje(f"- {libro.titulo} (ISBN: {libro.ISBN})")
                
                isbn = self.view_main.devolver_dato("Introduce ISBN del libro a devolver: ")
                libro = self.services_libros.buscar_libro(isbn)
                if libro and libro.prestado and libro.usuario_dni == usuario.dni:
                    libro.prestado = False
                    libro.usuario_dni = None               
                    self.services_libros.modificar_libro(libro)  
                    self.view_main.mostrar_mensaje(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
                else:
                    self.view_main.mostrar_mensaje("Este libro no está prestado a este usuario.")
               else:
                 self.view_main.mostrar_mensaje("El usuario no tiene libros prestados.")
             else:
                  self.view_main.mostrar_mensaje("Usuario no encontrado.")
         except ValueError as e:
           self.view_main.mostrar_mensaje(e)


      def programaEntero(self) :
            opcion = -1
            while opcion!=8 :
             self.mostrar_menu()
             opcion = self.elegir_opcion()
             self.menu_opciones(opcion)
      
          