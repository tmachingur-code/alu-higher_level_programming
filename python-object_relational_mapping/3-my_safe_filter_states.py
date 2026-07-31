#!/usr/bin/python3
"""Displays states matching a user input safely from SQL injection."""

import MySQLdb
import sys


def main():
    """Connects to MySQL and displays matching states safely."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY id ASC"
    )

    cursor.execute(query, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
