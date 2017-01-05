# 06_read_data.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# lendo os dados
#cursor.execute("""
#SELECT * FROM clientes;
#""")
cursor.execute("""
SELECT * FROM clientes WHERE id = 1
""")

for linha in cursor.fetchall():
    print(linha)



conn.close()
