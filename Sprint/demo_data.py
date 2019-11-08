import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
lite_cursor = conn.cursor()

create_table = """
    CREATE TABLE demo (
        s TEXT,
        x INTEGER,
        y INTEGER
    ); """

insert_to_table = """
    INSERT INTO demo
    (s, x, y) VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
    """

lite_cursor.execute(create_table)
lite_cursor.execute(insert_to_table)

lite_cursor.close()
conn.commit()

conn = sqlite3.connect('demo_data.sqlite3')
lite_cursor = conn.cursor()

print(lite_cursor.execute('select * from demo;').fetchall())
print(lite_cursor.execute('select count(*) from demo where x >=5 and y >= 5;').fetchall())
print(lite_cursor.execute('select count(DISTINCT y) from demo;').fetchall())