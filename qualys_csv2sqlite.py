import csv
import datetime
import sqlite3

sqldb=sqlite3.connect('db1')
sqldb.text_factory= str
