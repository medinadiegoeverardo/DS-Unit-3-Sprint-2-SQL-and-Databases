import sqlite3
import pandas as pd
# cd Documents/lambda_sql_databases/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/

# make empty sqlite3 file 
# con = sqlite3.connect('buddymove_holiday.sqlite3')

'''
# import dataset into dataframe
# names = ['user_id', 'sports', 'religious', 'nature', 'theater', 'shopping', 'picnic']
# df = pd.read_csv('buddymove_holidayiq.csv', names=names)
# df = df.drop([0], axis=0)

# convert dataframe into sql and import data to conn
# df.to_sql('buddymove_holiday', con)
'''
# make cursor to execute
# cursor = con.cursor()

# def execute_fetch(question, query):
    
#     a = cursor.execute(query).fetchall()
#     print (question, a)

def execute_fetch(question, query):
    for col in cursor.execute(query).fetchall():
        print (question, col)

question = 'What are the average number of reviews for each category?'
while x == True:
    one = select avg(_) FROM buddymove_holiday;
execute_fetch(question, one)
# shopping, sports, religious, theater, picnic

# con.commit()
# con.close()