# import mysql.connector as mysql
import mysql.connector as mysql

def conn():
    return mysql.connect(
        host="127.0.0.1",
        user="root",
        password="Inacap.2024",
        database="hola"
    )