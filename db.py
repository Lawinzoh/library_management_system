from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        port=3308,
        user="demo_user",
        password="demo_pass",
        database="demo_db"
    ) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        for row in cursor.fetchall():
            print(f"Type: {type(row)} | {row}")
    pass
except Error as e:
    print(e)