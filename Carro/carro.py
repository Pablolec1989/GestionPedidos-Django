class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        carro = self.session.get("carro") # Al agregar articulo al carro se identifica con la sesion del user
        
        if not carro:
           carro = self.session["carro"]={} # Si no tiene carro se le crea uno.
            
        self.carro = carro # Si ya tiene carro es igual al que tenía.

    # METODOS
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()): # Si la clave del producto no existe en el carro, la crea.
            
            self.carro[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1 #Actualiza cantidad
                    value["precio"] = float(value["precio"])+producto.precio #Actualiza precio
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"] = self.carro # Cambio en la sesion y guardado.
        self.session.modified = True
            
    def eliminar(self, producto):
        producto.id = str(producto.id)
            
        if (producto.id in self.carro): # Si el producto esta en el carro lo elimina ('del')
            del self.carro[producto.id]
        
        self.guardar_carro()
        
    def restar_producto(self, producto): # Verificar si el producto existe en el carro y resta su cantidad.
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"]-1
                value["precio"] = float(value["precio"])-producto.precio
                if value["cantidad"] < 1: # En caso de tener cantidad 0, el producto se elimina del carro.
                    self.eliminar(producto)
                    break
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.sesion["carro"]={}
        self.session.modified = True
            