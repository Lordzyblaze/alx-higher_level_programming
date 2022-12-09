#!/usr/bin/python3

# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="root", port=3306,
                         passwd="1Lordzy@123", db="hbtn_0e_0_usa")
    c = db.cursor()
    c.execute("SELECT *  FROM states  WHERE name LIKE BINARY '{}' ORDER BY states.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
