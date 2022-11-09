#!/usr/bin/python3
""" lists all states """
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name = '{}'\
        ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
