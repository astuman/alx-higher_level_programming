#!/usr/bin/python3
"""
print cities order by id ascending order
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
