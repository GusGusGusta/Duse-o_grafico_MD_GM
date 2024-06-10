# -*- coding: utf-8 -*-
import sqlite3
import csv
from datetime import datetime

global tipo, cantidad, total
global producto, categoria, precio

fecha = datetime.today().strftime('%d-%m-%y')
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()

def exportar_ventas_csv():
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    with open('ventas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])
        writer.writerows(ventas)

def exportar_productos_csv():
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conexion.close()
    with open('productos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'producto', 'categoria', 'precio'])
        writer.writerows(productos)

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
    conexion.commit()

def insertProductoToDb(producto):
    cursor.execute('''
    INSERT INTO productos (nombre, categoria, precio)
    VALUES (?, ?, ?)
    ''', producto)
    conexion.commit()

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
    
    conexion.commit()
crear_tablas()

def inicio():
    print("============================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("============================")
    print("🔵 1️⃣  🏷️ INGRESAR PRODUCTO 🏷️")
    print("🔵 2️⃣       🛒 CAJA 🛒")
    print("🔵 3️⃣     📑 EXPORTAR 📑")
    print("🔵 4️⃣       🚪 SALIR 🚪")
    print("============================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            ingresar_producto()
        elif ops == '2':
            ingresar_caja()
        elif ops == '3':
            exportar()
        elif ops == '4':
            print("Saliendo del programa...")           
            break
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            inicio()

def exportar():
    print("============================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("============================")
    print("🔵 1️⃣      📑 EXCEL 📑")
    print("🔵 2️⃣    📊 POWER BI 📊")
    print("🔵 3️⃣     🔙 VOLVER 🔙")
    print("🔵 4️⃣      🚪 SALIR 🚪")
    print("============================")
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
            break
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            inicio()

def exportar_excel():
    print("============================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("============================")
    print("🔵 1️⃣      🏷️ PRODUCTOS 🏷️")
    print("🔵 2️⃣       🛒 VENTAS 🛒")
    print("🔵 3️⃣       🔙 VOLVER 🔙")
    print("🔵 4️⃣        🚪 SALIR 🚪")
    print("============================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            exportar_productos_csv()
            print("============================")
            print("Excel Exportado con exito ! ")
            print("============================")
            inicio()
        elif ops == '2':
            exportar_ventas_csv()
            print("============================")
            print("Excel Exportado con exito ! ")
            print("============================")
            inicio()
        elif ops == '3':
            exportar()
        elif ops == '4':
            print("Saliendo del programa...")
            break
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            exportar_excel()

def exportar_powerbi():
    print("============================")
    print("✔️ SELECCIONA UNA OPCION ✔️")
    print("============================")
    print("🔵 1️⃣      🏷️ PRODUCTOS 🏷️")
    print("🔵 2️⃣       🛒 VENTAS 🛒")
    print("🔵 3️⃣       🔙 VOLVER 🔙")
    print("🔵 4️⃣        🚪 SALIR 🚪")
    print("============================")
    ops = input("Ingresa opcion ==> ")

    while True:
        if ops == '1':
            exportar_productos_csv()
            print("============================")
            print("Excel Exportado con exito ! ")
            print("============================")
            inicio()
        elif ops == '2':
            exportar_ventas_csv()
            print("============================")
            print("Excel Exportado con exito ! ")
            print("============================")
            inicio()
        elif ops == '3':
            exportar()
        elif ops == '4':
            print("Saliendo del programa...")
            break
        else:
            print("❗ Opción no válida. Por favor, selecciona una opción válida. ❗")
            exportar_excel()

  
def ingresar_producto():
    print("============================")
    print("   🏷️ INGRESO PRODUCTO 🏷️  ")
    print("============================")
    Producto = input("Ingresa el nombre del producto ==> ")
    categoria = input("Ingresa la categoría del producto ==> ")
    precio = int(input("Ingresa el precio del producto ==> "))

    productos = (Producto, categoria, precio)

    insertProductoToDb(productos)
    print("============================")
    print(f"Producto {Producto} ingresado con éxito.")
    print("============================")
    inicio()
    
def ingresar_caja():
    print("")
    print("============================")
    print("        🛒 CAJA 🛒         ")
    print(" 🗓️  FECHA " + fecha + " 🗓️")
    print("============================")
    print("  🕵️‍♂️ SELECCION PRODUCTO 🕵️‍♀️ ")
    print("============================") 
    producto_id = int(input("Ingresa código del producto ==> "))
    cantidad = int(input("Ingresa cantidad ==> "))
    producto_seleccionado = buscar_producto_por_id(producto_id)

    if producto_seleccionado:
        tipo = producto_seleccionado['nombre']
        categoria = producto_seleccionado['categoria']
        precio = producto_seleccionado['precio']
        total = cantidad * precio
        print(f"Producto Seleccionado: {tipo} UN: {cantidad} Total: {total}")

        ventas = [(fecha, tipo, categoria, precio, cantidad, total)]
        for venta in ventas:
            insertToDb(venta)
    else:
        print("============================")
        print()
        print("❗ PRODUCTO NO ENCONTRADO ❗")
        print("❗  INTÉNTALO NUEVAMENTE ❗")    



# Llamar a la función inicio para empezar el proceso
#print(leer_datos())

#inicio()
