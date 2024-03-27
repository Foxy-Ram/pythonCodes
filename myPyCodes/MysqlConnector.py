from mysql import connector as c

conn = c.connect(user="root", password="awe123", host="localhost", database="to_learn")
cursor = conn.cursor()


def insert_row(cursor_, table_name="students", **column):
    query = f"insert into {table_name} values\
            ({column.get('suc')},'{column.get('name')}' , {column.get('age')}); "
    cursor.execute(query)


dict_ = {'name': 'sindh', 'suc': 119, 'age': 18}
insert_row(cursor_=cursor, **dict_)
cursor.execute("SELEct * from  students;")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
cursor.close()
conn.close()
