import mysql.connector
from mysql.connector import Error,errorcode

def search(number):
    try:
        connection=mysql.connector.connect(host='sql12.freesqldatabase.com',database='sql12381368',user='sql12381368',password='wneBZXrIU1')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    try:
        sql_select_Query = f"SELECT * FROM cars WHERE Number = '{number}';"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        reclist=[]
        for row in records:
            print("Number ", row[0], )
            reclist.append(row[0])
            print("Owner: ", row[1])
            reclist.append(row[1])
            print("Address: ", row[2])
            reclist.append(row[2])
            print("Model: ", row[3])
            reclist.append(row[3])
            print("Insurance No.: ", row[4])
            reclist.append(row[4])
            print(reclist)
            if len(reclist) == 0:
                return None
            else:
                return reclist

    except Error as e:
        print("Error reading data from MySQL table", e)
