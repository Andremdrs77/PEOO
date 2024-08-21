import sqlite3

con = sqlite3.connect('escolainternacional.db')
sql = con.cursor()

sql.execute('CREATE TABLE alunos (nome, nota1, nota2, nota3, nota4)')

con.commit()
con.close()