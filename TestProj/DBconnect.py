import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SGATLA-T440\SQLEXPRESS;'
                      'Database=data;'
                      'Trusted_Connection=yes;')

print("success")
cursor = conn.cursor()
cursor.execute('SELECT * FROM data.dbo.SalesAndMarketing')
result=cursor.fetchall()
for row in result:
    print(row.City,row.State)