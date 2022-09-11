#!/usr/bin/python3
"""
0-select_states: used to select states from a database
"""
import MySQLdb
import sys
if __name__ = "__main__":
	db = MySQLdb.connect(user=sys.argv[1], 
				passwd=sys.argv[2], 
				db=sys.argv[3],
				host="localhost",
				port=3306)
	cur = db.cursor()

	cur.execute("SELECT * FROM states ORDER BY id ASC")
	data = cur.fetchall()
	for datum in data:
		print(datum)
	cur.close()
	db.close()


