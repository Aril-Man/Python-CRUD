import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',
                             password='', database='pyton_data')

cur = db.cursor()

sql = "INSERT INTO tb_data (nama, jk, nis) VALUE (%s, %s, %s)"
value = [
    ("Azriel Fauzi Hermansyah", "L", "11907065"),
    ("Ragetha Prameswari Kirana", "P", "11907066"),
    ("Lutfi Azizan", "L", "11907077"),
    ("Alfi Ilham", "L", "11907078"),
    ("Ahmad Ikhsan Maulana", "L", "11907055")
]

for val in value:
    cur.execute(sql, val)
    db.commit()

print("{} data ditambahkan". format(len(value)))
