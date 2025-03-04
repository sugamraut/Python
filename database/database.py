import sqlite3

conn = sqlite3.connect('test.db')
print ("open database successfully");
conn.execute('''create Table company( Id int PRIMARY KEY NOT NULL,
              name TEXT NOT NULL,
              age INT NOT NULL,
              ADDRESS CHAR(50),
              salary REAL
              );''')

print ("Table create sucessfully")

conn.close()