import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
lite_cursor = conn.cursor()

lite_cursor.execute('SELECT productname, MAX(unitprice) FROM product;').fetchall()