import csv
import datetime
import sqlite3

sqldb=sqlite3.connect('db1')
sqldb.text_factory= str
cur = sqldb.cursor()
cur.execute('''DROP TABLE IF EXISTS qualys''')

cur.execute (''' create table if not exists qualys (ip varchar(20), dns varchar(70), netbios varchar(70), os varchar(50), ip_status varchar(30),
qid int(10), title varchar(100), type varchar(10), severity varchar(10), port int(7), protocol varchar(5), first_detected text, cve_id text,
vendor_ref text, cvss_base int, threat text, impact text, solution text, exploitable text, malware text, results text, category text )''')

sqldb.commit()

reader = csv.DictReader(open('c:\\temp\\filename.csv', 'r'), delimiter=',', quotechar='"')

for row in reader:
  if row['First Detected']:
    temp = row['First Detected']
    temp2 = temp[:10]
    #cutting off HH:SS:MM
    row['First Detected'] = datetime.datetime.strptime(temp2, "%m/%d/%Y").strftime("%Y-%m-%d")
    
    
