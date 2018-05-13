import sqlite3
conn =sqlite3.connect('korea.db');
cursor=conn.execute('select * from sample')
rows=cursor.fetchall();
row_counter=0;
for row in rows:
    print(row);
    row_counter+=1;
print("Number of rows:{}".format(row_counter))
cursor.close();