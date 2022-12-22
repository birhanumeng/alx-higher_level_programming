#!/usr/bin/python3
"""Lists all cities of that state, using the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id", [argv[4]])
    query_rows = cur.fetchall()
    for row in query_rows:
        print(", ".join(row[0]))
    cur.close()
    conn.close()
