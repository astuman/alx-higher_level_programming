#!/usr/bin/python3

import MySQLdb

from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4]))
    rows = myCursor.fetchall()
    for row in rows:
        print(row)
    myCursor.close()
    db.close()