#!/usr/bin/python3
"""Displays all values in the states table matching the searched name."""

import MySQLdb
import sys


def main():
    """Connects to the database and displays matching states."""
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
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
