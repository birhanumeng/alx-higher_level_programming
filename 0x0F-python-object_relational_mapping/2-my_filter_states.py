#!/usr/bin/python3
"""Lists all recorde that matchs in states table of hbtn_0e_0_usa db."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='argv[4]' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

