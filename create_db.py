import mysql.connector

# This is used to initialize the mysql database on your computer. You only have to run this once.

mydb = mysql.connector.connect(host="localhost", user="root", passwd="pass")

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS course_resource_hub")