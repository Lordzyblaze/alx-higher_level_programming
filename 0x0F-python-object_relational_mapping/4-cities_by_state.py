#!/usr/bin/python3
# Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
# Usage: ./4-cities_by_state.py <mysql username> \
#                               <mysql password> \
#                               <database name>
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user="root", port=3306,
                                 passwd="1Lordzy@123", db="hbtn_0e_0_usa")

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name  FROM  cities JOIN  states ON cities.state_id = state.id ORDER BY cities.id = states.id ASC" )
    [print(city) for city in c.fetchall()]
