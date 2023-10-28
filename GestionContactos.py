def __init__(self):
        self.contactos = {}
def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

def buscar_contacto(self, nombre):
    if nombre in self.contactos:
        return f"{nombre}: {self.contactos[nombre]}"
    else:
        return "Contacto no encontrado."