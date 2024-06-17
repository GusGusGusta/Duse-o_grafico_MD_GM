# -*- coding: utf-8 -*-
import sqlite3
import csv
from datetime import datetime

global tipo, cantidad, total
global producto, categoria, precio

fecha = datetime.today().strftime('%Y-%m-%d')
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
tucarro = []  # Inicializar la lista del carrito fuera de la función


def buscar_producto_por_id(producto_id):
    cursor.execute('SELECT * FROM productos WHERE id = ?', (producto_id,))
    producto = cursor.fetchone()
    if producto:
        return {
            'id': producto[0],
            'nombre': producto[1],
            'categoria': producto[2],
            'precio': producto[3]
        }
    return None

def insertToDb(ventas):
    cursor.execute('''
    INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', ventas)
    #conexion.commit()

def leer_datos():
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    return ventas

def buscar_por_fecha(fecha):
    cursor.execute('SELECT * FROM ventas WHERE fecha = ?', (fecha,))
    ventas = cursor.fetchall()
    ventas = [dict(id=venta[0], fecha=venta[1], producto=venta[2], categoria=venta[3], precio=venta[4], cantidad=venta[5], total=venta[6]) for venta in ventas]
    return ventas

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            producto TEXT,
            categoria TEXT,
            precio INTEGER,
            cantidad INTEGER,
            total REAL
        )''') # Se eliminó el punto y coma y se separaron las sentencias

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            categoria TEXT,
            precio INTEGER
        )''')  # Se eliminó el punto y coma y se separaron las sentencias
    
   # conexion.commit()
crear_tablas()

#menu principal
def inicio():
    print("===================================")
    print("   ✔️   MENU PRINCIPAL LYDER  ✔️")
    print("====================================")
    print("🔵 1️⃣  🏷️  MANTENEDOR PRODUCTOS 🏷️")
    print("🔵 2️⃣         🛒 CAJA 🛒")
    print("🔵 3️⃣       📑 EXPORTAR 📑")
    print("🔵 4️⃣         🚪 SALIR 🚪")
    print("=====================================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            mantenedor_productos()
        elif ops == '2':
            ingresar_caja()
        elif ops == '3':
            exportar()
        elif ops == '4':
            print("Saliendo del programa...")
            salir()
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            inicio()
#Opcion 1
def mantenedor_productos():
    print("====================================")
    print("     🏷️ MANTENEDOR PRODUCTOS 🏷️    ")
    print("====================================")
    print("====================================")
    print("🔵 1️⃣  🏷️  INGRESAR PRODUCTOS 🏷️")
    print("🔵 2️⃣  🏷️  ACTUALIZAR PRODUCTOS 🏷️")
    print("🔵 3️⃣  🏷️  ELIMINAR PRODUCTOS 🏷️")
    print("🔵 4️⃣        🔙 VOLVER 🔙")
    print("🔵 5️⃣         🚪 SALIR 🚪")
    print("=====================================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            ingresar_producto()
        elif ops == '2':
            actualizar_producto()            
        elif ops == '3':
            eliminar_producto()
        elif ops == '4':
            inicio()
        elif ops == '5':
            print("Saliendo del programa...")
            salir()
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            mantenedor_productos()
            break
def insertProductoToDb(producto):
    cursor.execute('''
    INSERT INTO productos (nombre, categoria, precio)
    VALUES (?, ?, ?)
    ''', producto)
    #conexion.commit()
def eliminarProductoToDb(producto):
    cursor.execute('''
    DELETE from productos where id = ?  
    ''', producto)
    conexion.commit()
def actualizarProductoToDb(id, nombre, categoria, precio):
    cursor.execute('''
    UPDATE productos
    SET nombre = ?, categoria = ?, precio = ?
    WHERE id = ?
    ''', (nombre, categoria, precio, id))
    #conexion.commit()
#Mantenedor Ops 1
def ingresar_producto():
    print("============================")
    print("   🏷️ INGRESO PRODUCTO 🏷️  ")
    print("============================")
    Producto = input("Ingresa el nombre del producto ==> ")
    categoria = input("Ingresa la categoría del producto ==> ")
    try:
        precio = float(input("Ingresa el precio del producto ==> "))
    except ValueError:
        print("❗ Entrada inválida. El precio debe ser un número.")
        ingresar_producto()
    producto = (Producto, categoria, precio)
    insertProductoToDb(producto)
    print(f"Producto {Producto} ingresado con éxito.")
    mantenedor_productos()
#Mantenedor Ops 2
def actualizar_producto():
    print("===============================")
    print("   ✏️ ACTUALIZAR PRODUCTO ✏️  ")
    print("===============================")
    try:
        id = int(input("Ingresa el Codigo del producto a actualizar ==> "))
    except ValueError:
        print("❗ Entrada inválida. El ID debe ser un número.")
        print("Saliendo del programa...")
        actualizar_producto()

    nombre = input("Ingresa el nuevo nombre del producto ==> ")
    categoria = input("Ingresa la nueva categoría del producto ==> ")
    try:
        precio = int(input("Ingresa el nuevo precio del producto ==> "))
    except ValueError:
        print("❗ Entrada inválida. El precio debe ser un número.")
        print("Saliendo del programa...")
        actualizar_producto()

    actualizarProductoToDb(id, nombre, categoria, precio)
    print("=========================================")
    print(f"Producto {nombre} actualizado con éxito.")
    print("=========================================")
    mantenedor_productos()
#Mantenedor Ops 3
def eliminar_producto():
    print("=====================================")
    print("   🏷️ ELIMINAR PRODUCTO 🏷️  ")
    print("=====================================")
    codigo = input("Ingresa Codigo del producto ==> ")
    eliminarProductoToDb((int(codigo),)) 
    print("=====================================")
    print(f"Producto {codigo} Eliminado con éxito.")
    print("=====================================")
    mantenedor_productos()
#Opcion 2 
def ingresar_caja():
    print("")
    print("============================")
    print("        🛒 CAJA 🛒         ")
    print(f" 🗓️  FECHA {fecha} 🗓️")
    print("============================")
    print("  🕵️‍♂️ SELECCIONA PRODUCTO 🕵️‍♀️ ")
    print("============================") 

    while True:
        print("          TU CARRO         ")
        print("_____Para finalizar teclear 'fin'_____")
        for item in tucarro:
            print(f"{item['tipo']} - Cantidad: {item['cantidad']} - Total: {item['total']}")
        print("____________________________")
        print("============================") 

        producto_id = input("Ingresa código del producto ==> ")

        if producto_id.lower() == "fin":
            total_carrito = sum(item['total'] for item in tucarro)
            print("============================")
            print("          TOTAL            ")            
            print(f"Total de la compra: {total_carrito}")
            print("============================")
            inicio()
            break
              

        if not producto_id.isdigit():
            print("❗ Entrada inválida. El código del producto debe ser un número.")
            print("Volviendo al programa...")
            inicio()
            break

        producto_id = int(producto_id)
        cantidad = input("Ingresa cantidad ==> ")
        if not cantidad.isdigit():
            print("❗ Entrada inválida. La cantidad debe ser un número.")
            print("Volviendo al programa...")
            inicio()
            break

        cantidad = int(cantidad)
        producto_seleccionado = buscar_producto_por_id(producto_id)

        if producto_seleccionado:
            tipo = producto_seleccionado['nombre']
            categoria = producto_seleccionado['categoria']
            precio = producto_seleccionado['precio']
            total = cantidad * precio
            print(f"Producto Seleccionado: {tipo} UN: {cantidad} Total: {total}")

            # Agregar la selección al carrito
            tucarro.append({
                'tipo': tipo,
                'cantidad': cantidad,
                'total': total
            })

            ventas = [(fecha, tipo, categoria, precio, cantidad, total)]
            for venta in ventas:
                insertToDb(venta)
        else:
            print("============================")
            print()
            print("❗ PRODUCTO NO ENCONTRADO ❗")
            print("❗  INTÉNTALO NUEVAMENTE ❗")
#Opcion 3
def exportar():
    print("=====================================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("=====================================")
    print("🔵 1️⃣      📑 EXCEL 📑")
    print("🔵 2️⃣    📊 POWER BI 📊")
    print("🔵 3️⃣     🔙 VOLVER 🔙")
    print("🔵 4️⃣      🚪 SALIR 🚪")
    print("=====================================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            exportar_excel()
        elif ops == '2':
            #informe()
            exportar_powerbi()
            break
        elif ops == '3':
            inicio()
        elif ops == '4':
            print("Saliendo del programa...")
            salir()
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            inicio()
#Exportar Excel Opc 1
def exportar_excel():
    print("=====================================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("=====================================")
    print("🔵 1️⃣      🏷️ PRODUCTOS 🏷️")
    print("🔵 2️⃣       🛒 VENTAS 🛒")
    print("🔵 3️⃣       🔙 VOLVER 🔙")
    print("🔵 4️⃣        🚪 SALIR 🚪")
    print("=====================================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            exportar_productos_csv()
            print("=====================================")
            print("Excel Exportado con exito ! ")
            print("=====================================")
            inicio()
        elif ops == '2':
            exportar_ventas_csv()
            print("=====================================")
            print("Excel Exportado con exito ! ")
            print("=====================================")
            inicio()
        elif ops == '3':
            exportar()
        elif ops == '4':
            print("Saliendo del programa...")
            salir()
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            exportar_excel()
#Exportar Exc Ops 1 
def exportar_productos_csv():
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    #conexion.close()
    with open('productos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'producto', 'categoria', 'precio'])
        writer.writerows(productos)
#Exportar Exc Ops 2           
def exportar_ventas_csv():
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    #conexion.close()
    with open('ventas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])
        writer.writerows(ventas)
#Exportar Power Bi Opc 2
def exportar_powerbi():
    print("=====================================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("=====================================")
    print("🔵 1️⃣      🏷️ PRODUCTOS ❗ En Desarrollo ❗ 🏷️")
    print("🔵 2️⃣       🛒 VENTAS   ❗ En Desarrollo ❗ 🛒")
    print("🔵 3️⃣       🔙 VOLVER 🔙")
    print("🔵 4️⃣        🚪 SALIR 🚪")
    print("=====================================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            print("Volviendo a Exportar...")
            exportar()
        elif ops == '2':
            print("Volviendo a Exportar...")
            exportar()
        elif ops == '3':
            print("Volviendo a Exportar...")
            exportar()
        elif ops == '4':
            print("Saliendo del programa...")
            salir()
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            exportar_excel()
#Opcion 4 Salir
def salir():
    conexion.commit()
    exit()



if __name__ == "__main__":
    inicio()