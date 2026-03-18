import pymysql  # pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="gatodb",
        port=3306
    )