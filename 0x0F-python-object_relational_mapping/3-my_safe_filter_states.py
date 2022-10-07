#!/usr/bin/python3
"""
filter data free from sql injection
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], conn=argv[3], charset="utf8")
    mycursor = conn.cursor()
    mycursor.excute("SELECT * FROM states WHERE state LIKE %s ORDER BY \
                     id ASC", argv[4])
    rows = mycursor.fetchall()
    for row in rows:
        print(rows)
    mycursor.close()
    conn.close
