import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',
                             password='', database='pyton_data')

cur = db.cursor()
sql = "UPDATE tb_data SET nama=%s, jk=%s , nis=%s WHERE id=%s"
val = ("Ilham Maulana", "L", "11908065", 4)
cur.execute(sql, val)

db.commit()

print("{} data diubah".format(cur.rowcount))
