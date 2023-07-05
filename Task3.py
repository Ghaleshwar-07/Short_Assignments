import datetime
import mysql.connector

def get_orders():
    mydb = mysql.connector.connect(
      host="localhost",
      user="Task3",
      password="your_password",
      database="orders"
    )

    now = datetime.datetime.now()
    week_ago = now - datetime.timedelta(days=7)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM orders WHERE createdAt BETWEEN %s AND %s", (week_ago, now))
    orders = mycursor.fetchall()

    mydb.close()

    return orders
