import sqlite3
conn =sqlite3.connect('korea.db');
cur=conn.cursor();

cur.execute('''
    create table stocks
    (data text,trens text,symbol text,qty real,price real)''')
cur.execute("insert into stocks values ('2005-01-05','buy','rhat',150,35.2)")
cur.execute("insert into stocks values ('2006-01-06','buy','rhat',170,35.17)")
conn.commit();
cur.execute('select * from stocks order by price')
for row in cur.fetchall():
    print(row);

cur.close();