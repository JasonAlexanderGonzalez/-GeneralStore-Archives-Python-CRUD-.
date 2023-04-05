from Producto import Metodos
from Orden import MetodosOrden

archivo = "productos.txt"
m = Metodos(archivo)

archivo_ordenes = "ordenes.txt"
dobleM = MetodosOrden(archivo_ordenes)


while True:
    print("Hola Juancito, que deseas hacer!.")
    print("1. Digite 1 para Productos")
    print("2. Digite 2 para Órdenes")
    print("3. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        while True:
            print("Menú de los productos")
            print("1. Agregar un producto")
            print("2. Mostrar todos los productos")
            print("3. Buscar un producto")
            print("4. Actualizar un producto")
            print("5. Eliminar un producto")
            print("6. Regresar al menú principal")

            producto_opcion = input("Ingrese su opción: ")

            if producto_opcion == "1":
                nombre = input("Ingrese el nombre del producto: ")
                presentacion = input("Ingrese la presentación del producto: ")
                stock = int(input("Ingrese el stock del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                m.add(nombre, presentacion, stock, precio)
            elif producto_opcion == "2":
                m.mostrar_productos()
            elif producto_opcion == "3":
                codigo = input("Ingrese el código del producto: ")
                producto = m.buscar_producto(codigo)
                if producto:
                    print(producto)
                else:
                    print("El producto no se encuentra en el inventario.")
            elif producto_opcion == "4":
                codigo = input("Ingrese el código del producto: ")
                nombre = input("Ingrese el nuevo nombre del producto: ")
                presentacion = input(
                    "Ingrese la nueva presentación del producto: ")
                stock = int(input("Ingrese el nuevo stock del producto: "))
                precio = float(input("Ingrese el nuevo precio del producto: "))
                m.update(
                    codigo, nombre, presentacion, stock, precio)
            elif producto_opcion == "5":
                codigo = input("Ingrese el código del producto: ")
                m.delete(codigo)
            elif producto_opcion == "6":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    elif opcion == "2":
        while True:
            print("Menú de las órdenes")
            print("1. Agregar una orden")
            print("2. Mostrar todas las órdenes")            
            print("3. Actualizar una orden")
            print("4. Eliminar una orden")
            print("5. Regresar al menú principal")

            orden_opcion = input("Ingrese su opción: ")

            if orden_opcion == "1":
                
                nombre = input("Ingrese el nombre del producto: ")
                presentacion = input("Ingrese la presentación del producto: ")
                stock = int(input("Ingrese el stock del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                dobleM.add(nombre, presentacion, stock, precio)

                
            elif orden_opcion == "2":
                dobleM.mostrar_productos()

                
            elif orden_opcion == "3":
                codigo = input("Ingrese el código del producto: ")
                nombre = input("Ingrese el nuevo nombre del producto: ")
                presentacion = input(
                    "Ingrese la nueva presentación del producto: ")
                stock = int(input("Ingrese el nuevo stock del producto: "))
                precio = float(input("Ingrese el nuevo precio del producto: "))
                dobleM.update(
                    codigo, nombre, presentacion, stock, precio)

                
            elif orden_opcion == "4":
                codigo = input("Ingrese el código del producto: ")
                dobleM.delete(codigo)
                

                
            elif orden_opcion == "5":          
            
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    elif opcion == "3":
        print("Hasta luego.")
        break
    else:
        print("Opción inválida. Intente de nuevo")
