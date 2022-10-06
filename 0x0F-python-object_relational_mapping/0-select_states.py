#!/usr/bin/python3
"""
list all states from database
"""
import MySQLdb

from sys import argv

if __name__ == "__main__"
  db = MYSQLdb.connect(host="localhost", port="3306", user=argv[1], password=argv[2],db=argv[3], charset="utf8")
  cursor = db.cursor()
  cursor.execute("SELECT * FROM states ORDDER BY ID ASC")
  rows = cursor.fetchall()
  for row in rows:
      print(row)
  cursor.close()
  db.close()




