class GestionContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            return f"{nombre}: {self.contactos[nombre]}"
        else:
            return "Contacto no encontrado."

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            return f"{nombre} ha sido eliminado."
        else:
            return "Contacto no encontrado."

    def listar_contactos(self):
        return "\n".join([f"{nombre}: {telefono}" for nombre, telefono in self.contactos.items()])

if __name__ == "__main__":
    agenda = GestionContactos()

    while True:
        print("Opciones:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Listar contactos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agenda.agregar_contacto(nombre, telefono)
            print("Contacto agregado.")

        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            resultado = agenda.buscar_contacto(nombre)
            print(resultado)

        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            resultado = agenda.eliminar_contacto(nombre)
            print(resultado)

        elif opcion == "4":
            lista_contactos = agenda.listar_contactos()
            print("Contactos:")
            print(lista_contactos)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
