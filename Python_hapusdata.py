import mysql.connector
db = mysql.connector.connect(host='localhost', user='root',
                             password='', database='pyton_data')

cur = db.cursor()

sql = "DELETE FROM tb_data WHERE id=%s"
val = (3, )
cur.execute(sql, val)

db.commit()

print("{} data dihapus".format(cur.rowcount))
