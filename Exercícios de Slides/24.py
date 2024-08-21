import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()


sql.execute("INSERT INTO teste (nome,telefone) VALUES ('RK','9999-9999')")
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('Maria','2222-2222')")
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('Marcos','3333-3333')")

sql.execute("SELECT * FROM teste")

registros = sql.fetchall()

#print(type(registros))
#print(registros)

for reg in registros:
    print(reg)


sql.execute("SELECT telefone FROM teste WHERE nome = 'Maria'")

registros2 = sql.fetchone()

print(registros2[0])


print()


sql.execute("DELETE FROM teste WHERE nome = 'Maria'")

sql.execute("SELECT * FROM teste")

registros3 = sql.fetchall()

for reg in registros3:
    print(reg)

sql.execute("UPDATE teste SET telefone = '5555-5555' WHERE nome = 'RK'")

print()

sql.execute("SELECT * FROM teste")

registros4 = sql.fetchall()

for reg in registros4:
    print(reg)


con.commit()
con.close()
