# -*- coding: utf-8 -*-
import sqlite3
import csv

def crear_tabla():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        producto TEXT,
        categoria TEXT,
        precio REAL,
        cantidad INTEGER,
        total REAL
    )
    ''')
    conexion.commit()
    conexion.close()

def insertToDb(ventas):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO ventas (fecha, producto, categoria, precio, cantidad, total)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', ventas)
    conexion.commit()
    conexion.close()

def leer_datos():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def buscar_por_fecha(fecha):
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas WHERE fecha = ?', (fecha,))
    ventas = cursor.fetchall()
    #devolver diccionario con key nombre del campo:
    ventas = [dict(id=venta[0], fecha=venta[1], producto=venta[2], categoria=venta[3], precio=venta[4], cantidad=venta[5], total=venta[6]) for venta in ventas]
    conexion.close()
    return ventas

crear_tabla()

# Datos de ejemplo
ventas = [
('2024-01-20', 'Pan Integral', 'Panadería', 1400, 1, 1400*1),
('2024-01-21', 'Arroz', 'Abarrotes', 990, 1, 990*1),
('2024-01-22', 'Detergente Líquido', 'Hogar', 3500, 1, 3500*1),

('2024-02-20', 'Microondas', 'Electrodoméstico', 49990, 1, 49990*1),
('2024-02-21', 'Lámpara LED', 'Eléctrico', 4990, 1, 4990*1),
('2024-02-22', 'Harina', 'Abarrotes', 990, 1, 990*1),

('2024-03-20', 'Café Instantáneo', 'Abarrotes', 2590, 1, 2590*1),
('2024-03-21', 'Sartén Antiadherente', 'Hogar', 29990, 2, 29990*2),
('2024-03-2', 'Licuadora', 'Electrodoméstico', 29990, 2, 22990*2),

('2024-04-20', 'alargador de Enchufes', 'Eléctrico', 3990, 2, 3990*2),
('2024-04-21', 'Fideos', 'Abarrotes', 990, 2, 990*2),
('2024-04-22', 'Tarro Salmon', 'Abarrotes', 1200, 2, 1200*2),

('2024-05-20', 'Cubre Camas', 'Hogar', 19990, 2, 19990*2),
('2024-05-21', 'Sabanas', 'Hogar', 20990, 2, 20990*2),
('2024-05-22', 'Pan Molde', 'Panadería', 1300, 2, 1300*2)

('2024-06-01', 'Galleta', 'Panadería', 1300, 2, 1300*2)
('2024-06-01', 'Palta', 'Verdureria', 1300, 2, 1300*2)
('2024-06-01', 'Bebida', 'Bebidas', 1300, 2, 1300*2)
('2024-06-01', 'Leche', 'Abarrotes', 1300, 2, 1300*2)
('2024-06-01', 'Jamon', 'Fiambreria', 1300, 2, 1300*2)

]



#for venta in ventas:
#    insertToDb(venta)

#leer data:
#data = leer_datos()
#print(data)

#UTF8:
print('Ventas del día:')
texto = "¡Hola, mundo!"
bytes_utf8 = texto.encode('utf-8')
print(bytes_utf8.decode('utf-8'))  # b'\xc2\xa1Hola, mundo!'



#buscar por fecha:
ventas_hoy = buscar_por_fecha('2024-05-20')

for venta in ventas_hoy:
    print(int(venta['total']))

#Necesito Exportar todos los datos a csv desde el SQLITE:
def exportar_csv():

    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()
    conexion.close()
    with open('ventas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])
        writer.writerows(ventas)

exportar_csv()