import sqlite3

# mine   
db = sqlite3.connect('buddymove_holiday.sqlite3')
cursor = db.cursor()
# PRAGMA table_info('buddymove_holiday');
# -----

avg_all_q_fillable = """
    SELECT {}
    FROM buddymove_holiday;
"""
get_col_names = "SELECT name FROM PRAGMA_TABLE_INFO('buddymove_holiday')"  # (%s) % table
# print(cursor.execute(get_col_names).fetchall())

# # another method: gives me all info on column (example: (2, 'sports', 'TEXT', 0, None, 0))
# get_col_names = "PRAGMA table_info(buddymove_holiday)" # PRAGMA table_info(%s) % table
# print(cursor.execute(get_col_names).fetchall())

with sqlite3.connect('buddymove_holiday.sqlite3') as db:
    cols = [col[0] for col in db.cursor().execute(get_col_names).fetchall() if col[0] not in ['index', 'user_id']]
print(cols)

call = "PRAGMA table_info('buddymove_holiday')"  # (%s) % table
num_columns = len(cursor.execute(call).fetchall())
# print(num_columns)

# ------

(('AVG({col})' for col in cols]))

avg_all_q = avg_all_q_fillable.format(", ".join([f'AVG({col})' for col in cols]))
print(avg_all_q)

# with sqlite3.connect('buddymove_holiday.sqlite3') as db:
#     avgs = dict(zip(cols, db.cursor().execute(avg_all_q).fetchall()[0]))

# for col, avg in avgs.items():
#     print(f'The average of the {col} category is: '+str(avg)+'\n')



avg_all_q_fillable = """
    SELECT {}
    FROM review;
"""

get_col_names = """
    SELECT name FROM PRAGMA_TABLE_INFO('review');
"""

with sqlite3.connect('module1-introduction-to-sql/buddymove_holidayiq.sqlite3') as db:
    cols = [col[0] for col in db.cursor().execute(get_col_names).fetchall() if col[0] not in ['index', 'User Id']]

avg_all_q = avg_all_q_fillable.format(", ".join([f'AVG({col})' for col in cols]))

with sqlite3.connect('module1-introduction-to-sql/buddymove_holidayiq.sqlite3') as db:
        avgs = dict(zip(cols, db.cursor().execute(avg_all_q).fetchall()[0]))

for col, avg in avgs.items():
        print(f'The average of the {col} category is: '+str(avg)+'\n')

# automate yesterday's assignment