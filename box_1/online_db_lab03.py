### insert data to datable

import pymysql

db = pymysql.connect("localhost","root","","guy_online_db",use_unicode = True,charset='utf8')
cursor = db.cursor()

x = "MyWorkPlace"
y = "Fresh Market"
z = "081-8536510"

### insert manual
#sql = '''INSERT INTO custdetail(name,address,tel)
# VALUES ("MyHome","49 ม.9 ต.บ้านแพน อ.เสนา จ.อยุธยา" ,"094-5926126")'''

###insert from varieble
sql = '''INSERT INTO custdetail(name,address,tel)
  VALUES (%s, %s, %s) '''

record_add = (x,y,z)

try:
    cursor.execute(sql,record_add)
    db.commit()
except:
    db.rollback()
    print("fuck")

db.close()