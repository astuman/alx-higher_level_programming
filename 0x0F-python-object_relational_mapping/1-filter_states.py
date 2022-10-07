#!/usr/bin/python3

from email import charset
import MySQLdb

from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = myCursor.fetchall()
    for row in rows:
        print(row)
    myCursor.close()
    db.close()
