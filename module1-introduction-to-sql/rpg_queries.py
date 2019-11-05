import sqlite3

# cd Documents/lambda_sql_databases/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/

conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()

def execute_fetch(question, query):
    a = cursor.execute(query).fetchall()
    print (question, a)

question_1 = 'How many total characters are there?'
one = ('SELECT character_id, count(*) from charactercreator_character;')
execute_fetch(question_1, one)

question_2 = 'How many characters are clerics?'
two = ('select character_ptr_id, count(*) from charactercreator_cleric;')
execute_fetch(question_2, two)
# cleric; 75

question_3 = 'How many characters are fighters?'
three = ('select character_ptr_id, count(*) from charactercreator_fighter;')
execute_fetch(question_3, three)
# fighter; 68

question_4 = 'How many characters are mages?'
four = ('select character_ptr_id, count(*) from charactercreator_mage;')
execute_fetch(question_4, four)
# mage 108

question_5 = 'How many characters are thiefs?'
five = ('select character_ptr_id, count(*) from charactercreator_thief;')
execute_fetch(question_5, five)
# thief, 51

question_6 = 'How many characters are necromancer?'
six = ('select mage_ptr_id, count(*) from charactercreator_necromancer;')
execute_fetch(question_6, six)
# necromancer 11

question_7 = 'How many total Items?'
seven = ('SELECT item_id, count(*) FROM charactercreator_character_inventory;')
execute_fetch(question_7, seven)

question_8 = 'How many of the Items are weapons? How many are not?'
eight = ('select cci.item_id, aw.item_ptr_id \
from charactercreator_character_inventory as cci \
inner join armory_weapon as aw \
on cci.item_id = aw.item_ptr_id \
group by item_id;')
execute_fetch(question_8, eight)

question_9 = 'How many Items does each character have? (Return first 20 rows)'
nine = ('select character_id, item_id \
from charactercreator_character_inventory \
group by character_id \
limit 20;')
execute_fetch(question_9, nine)

question_10 = 'How many Weapons does each character have? (Return first 20 rows)'
ten = ('SELECT aw.item_ptr_id, COUNT(*) \
FROM armory_weapon as aw, \
armory_item as ai, \
charactercreator_character_inventory as cci \
WHERE aw.item_ptr_id == ai.item_id \
AND ai.item_id == cci.character_id \
GROUP BY aw.item_ptr_id \
LIMIT 20;')
execute_fetch(question_10, ten)

question_11 = 'On average, how many Items does each Character have?'
eleven = ('select avg(distinct item_id) \
from charactercreator_character_inventory;')
execute_fetch(question_11, eleven)
# ('select avg(distinct item_id) \
# from charactercreator_character_inventory \
# group by character_id;')

question_12 = 'On average, how many Weapons does each character have?'
twelve = ('SELECT AVG(item_id) \
FROM charactercreator_character_inventory;')
execute_fetch(question_12, twelve)

# ('SELECT AVG(aw.item_ptr_id) \
# FROM charactercreator_character_inventory as cci, \
# armory_item as ai, \
# armory_weapon as aw \
# WHERE aw.item_ptr_id = ai.item_id \
# AND ai.item_id = cci.character_id;')