import sqlite3

conn = sqlite3.connect('games.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games(
        назва TEXT,
        рік випуску INTEGER,
        оцінка REAL)""")
cursor.execute("DELETE FROM games")
cursor.execute("INSERT INTO games (назва, рік, оцінка) VALUES (?,?,?)", ("Cyberpunk 2077", "2023", "5/5"))
cursor.execute("INSERT INTO games (назва, рік, оцінка) VALUES (?,?,?)", ("Grid-Autosport", "2014", "4.8/5"))
cursor.execute("INSERT INTO games (назва, рік, оцінка) VALUES (?,?,?)", ("Minecraft", "2009", "4.3/5"))
cursor.execute("SELECT * FROM games")
result = cursor.fetchall()
for row in result:
    print(f"Назва: {row[0]}, Рік Випуску: {row[1]} Оцінка: {row[2]}")
conn.commit()
conn.close()