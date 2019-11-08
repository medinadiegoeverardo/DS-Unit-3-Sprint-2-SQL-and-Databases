import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
lite_cursor = conn.cursor()

print(lite_cursor.execute('SELECT productname, MAX(unitprice) FROM product;').fetchall())
print(lite_cursor.execute('select city, avg(hiredate - BirthDate) from employee group by city;').fetchall())
print(lite_cursor.execute('select productname, unitprice from product order by unitprice desc limit 10;').fetchall())
print(lite_cursor.execute('SELECT prod.ProductName, sup.CompanyName, prod.unitprice FROM Product as prod \
   JOIN Supplier as sup ON sup.id = prod.supplierid\
   ORDER BY prod.unitprice DESC LIMIT 10;').fetchall())

print(lite_cursor.execute('select prod.Id as product_id, prod.CategoryId as category_id, cat.CategoryName as cat_name \
from product as prod join category as cat on cat.Id = prod.CategoryId group by prod.CategoryId order by product_id desc;').fetchall())

lite_cursor.close()
conn.commit()