import sqlite3 as sql 

def CrearDataBase():
    conn = sql.connect("dbTiendadePedro.db")
    conn.commit()
    conn.close()

def CrearDateTable():
    conn =sql.connect("dbTiendadePedro.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE tblProductos(
        IDprod text PRIMARY KEY, 
        nombre text,
        cantidad int,
        preciou float
        )"""
    )
    conn.commit()
    conn.close()

def InsertarDatos(IDprod, nombreprod, cantprod, precioprod):
    conn =sql.connect("dbTiendadePedro.db")
    cursor = conn.cursor()
    consultaDb = f"INSERT INTO tblproductos VALUES('{IDprod}', '{nombreprod}', '{cantprod}', '{precioprod}')"
    cursor.execute(consultaDb)
    conn.commit()
    conn.close()

def SelecDatos():
    conn =sql.connect("dbTiendadePedro.db")
    cursor = conn.cursor()
    consultaDb = f"SELECT * FROM tblProductos"
    cursor.execute(consultaDb)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)



if __name__ == "__main__":
    CrearDataBase()
    CrearDateTable()
    InsertarDatos("001", "Leche", 10, 3400)
    InsertarDatos("002", "Arepa", 25, 2500)
    InsertarDatos("003", "Panela", 50, 4500)
    SelecDatos()

