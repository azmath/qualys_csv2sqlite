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
    
    to_db = [row['IP'], row['DNS'], row['NETBIOS'], row['OS'], row['IP STATUS'], row['QID'], row['TITLE'], row['Type'], row['Severity'], 
         row['Port'], row['Protocol'], row['First Detected'], row['CVE ID'], row['Vendor Reference'], row['CVSS'], row['Threat'], 
         row['Impact'], row['Solution'], row['Exploitability'], row['Associated Malware'], row['Results'], row['Category'] ]
    for x in range(0, 21):
      if to_db[x] == "":
        to_db[x] = unicode("0", "utf8")
    cur.execute("insert into qualys (IP, DNS, Netbios, OS, IP_Status, QID, Title, Type, Severity, Port, Protocol, First_Detected, CVE_ID,
            Vendor_ref, CVSS_base, Threat, Impact, Solution, Exploitable, Malware, Results, Category) Values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (to_db, ))
  sqldb.commit()
  sqldb.close()
  
