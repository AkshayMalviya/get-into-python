import pyodbc
server = 'XXXX'
database = 'XXXXXXX'
username = 'XXXXXXXX'
password = 'XXXXXXXXX'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO table_name (dept_id) VALUES (?);"
with cursor.execute(tsql,7):
    print ('Successfuly Inserted!')


#Update Query
print ('Updating Location for Nikita')
tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
with cursor.execute(tsql,'Sweden','Nikita'):
    print ('Successfuly Updated!')


#Delete Query
print ('Deleting user Jared')
tsql = "DELETE FROM Employees WHERE Name = ?"
with cursor.execute(tsql,'Jared'):
    print ('Successfuly Deleted!')


#Select Query
print ('Reading data from table')
tsql = "SELECT Name, Location FROM Employees;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()
        



# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print(data)
cnxn.close()