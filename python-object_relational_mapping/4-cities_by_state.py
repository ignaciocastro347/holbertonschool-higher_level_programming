#!/usr/bin/python3
""" lists all cities """
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c \
        INNER JOIN states s ON c.state_id = s.id \
        ORDER BY c.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
