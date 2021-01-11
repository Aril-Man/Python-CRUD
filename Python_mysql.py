import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',
                             password='', database='pyton_data')


cur = db.cursor()

cur.execute('SELECT * FROM tb_data')

for row in cur.fetchall():
    print(row)

db.close()

# sql = "INSERT INTO tb_data (nama, jk, nis) VALUE (%s, %s, %s)"
# val = ("Ragetha Prameswari Kirana", "P", "11907067")
# cur.execute(sql, val)

# db.commit()
# print("{} data ditambahkan". format(cur.rowcount))
