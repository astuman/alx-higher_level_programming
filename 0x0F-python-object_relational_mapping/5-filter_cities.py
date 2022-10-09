#!/usr/bin/python3
"""
print cities using parametr state name
"""
import MySQLdb

from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    mycursor = db.cursor()
    mycursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s ORDEDR BY \
    cities.id ASC", (argv[4]),)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
