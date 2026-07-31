#!/usr/bin/python3
"""Lists all cities of a given state from a MySQL database."""

import MySQLdb
import sys


def main():
    """Connects to MySQL and displays cities of a specified state."""
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (sys.argv[4],))

    cities = []

    for row in cursor.fetchall():
        cities.append(row[0])

    print(", ".join(cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
