
import sqlite3
# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS new_reg"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno INTEGER,Gender INTEGER,Age INTEGER , password TEXT)")
db.commit()