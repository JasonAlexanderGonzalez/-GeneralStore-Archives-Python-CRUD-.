class MetodosOrden:
    def __init__(self, archivo):
        self.archivo = archivo
        self.codigo = 0
        
    def add(self, nombre, presentacion, stock, precio):
        with open(self.archivo, "a") as f:
            f.write(f"{self.codigo},{nombre},{presentacion},{stock},{precio}\n")
            self.codigo += 1
        print('Producto agregado correctamente a la orden de compra.')
        
    def mostrar_productos(self):
        with open(self.archivo, "r") as f:
            for linea in f:
                codigo, nombre, presentacion, stock, precio = linea.strip().split(",")
                print(f"Código: {codigo}\nNombre: {nombre}\nPresentación: {presentacion}\nStock: {stock}\nPrecio: {precio}\n")
                
    def update(self, codigo, nombre, presentacion, stock, precio):
        productos_actualizados = []
        with open(self.archivo, "r") as f:
            for linea in f:
                codigo_producto, _, _, _, _ = linea.strip().split(",")
                if codigo_producto == codigo:
                    productos_actualizados.append(f"{codigo},{nombre},{presentacion},{stock},{precio}\n")
                else:
                    productos_actualizados.append(linea)
        with open(self.archivo, "w") as f:
            for linea in productos_actualizados:
                f.write(linea)
        print("El producto ha sido actualizado con éxito.")
        
    def delete(self, codigo):
        productos_actualizados = []
        with open(self.archivo, "r") as f:
            for linea in f:
                codigo_producto, _, _, _, _ = linea.strip().split(",")
                if codigo_producto != codigo:
                    productos_actualizados.append(linea)
        with open(self.archivo, "w") as f:
            for linea in productos_actualizados:
                f.write(linea)
        print("El producto ha sido eliminado con éxito.")

