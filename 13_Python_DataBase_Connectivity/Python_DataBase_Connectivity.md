




# Required Installations

- Sql (any flavour)
- connector or driver
- python

You Can reffer Python_Database_installation.md for installation steps.

To work with SQL databases in Python, you will need the following installations:

1. **SQL Database** (any flavor):
    - You need to have an SQL database installed and running. Examples of popular SQL database flavors are MySQL, PostgreSQL, SQLite, Microsoft SQL Server, Oracle Database, etc. Choose the one that suits your requirements and install it on your system or set it up on a remote server.
2. **SQL Connector or Driver**:
    - Depending on the SQL database you are using, you need to install the corresponding connector or driver to allow Python to interact with the database. Here are some common SQL connectors for different database flavors:
        - MySQL: **`mysql-connector-python`**
        - PostgreSQL: **`psycopg2`**
        - SQLite: No additional installation needed (included in Python's standard library)
        - Microsoft SQL Server: **`pyodbc`**
        - Oracle Database: **`cx_Oracle`**
    
    You can install these connectors using **`pip`**. For example, to install the MySQL connector, use **`pip install mysql-connector-python`**.
    
3. **Python**:
    - Ensure you have Python installed on your system. You can download the latest version of Python from the official Python website (**https://www.python.org/downloads/**). Python 3.x is recommended as Python 2.x is no longer supported.

Once you have the SQL database installed and the appropriate connector installed for your database flavor, you can use Python to interact with the database. Depending on the chosen database, you'll need to import the appropriate module in your Python script (e.g., **`import mysql.connector`**, **`import psycopg2`**, etc.).

For example, if you are working with MySQL, you will need both the MySQL database installed and the **`mysql-connector-python`** library installed in Python. Then you can use the connector in your Python script to connect to the MySQL database and perform various operations.

Make sure to have the necessary credentials (such as username and password) to connect to the SQL database, and ensure that your Python environment has network access to the database server (if the database is not on the same machine).

Python offers multiple options for connecting and interacting with databases. Some popular libraries and modules for database connectivity in Python are:

1. **SQLite3**: SQLite is a lightweight, serverless, self-contained database engine. It comes bundled with Python, so there's no need to install any additional modules to use it.
2. **MySQL Connector**: This is a library that allows Python to connect to MySQL databases. You need to install it using **`pip install mysql-connector-python`**.
3. **psycopg2**: This library enables Python to connect to PostgreSQL databases. You can install it using **`pip install psycopg2`**.
4. **pyodbc**: For connecting to Microsoft SQL Server databases, you can use pyodbc. It requires you to install **`pyodbc`** using **`pip install pyodbc`**.
5. **MongoDB Driver (pymongo)**: If you are working with MongoDB, you can use pymongo, which is the official Python driver for MongoDB. You can install it using **`pip install pymongo`**.
6. **SQLAlchemy**: SQLAlchemy is a powerful and versatile ORM (Object-Relational Mapping) library that can connect to various databases, including SQLite, MySQL, PostgreSQL, and others. You can install it using **`pip install SQLAlchemy`**.

## SQLite

Here's a basic example of connecting to an SQLite database and performing a simple query:

```python
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 30))

# Commit the changes to the database
conn.commit()

# Query the database and fetch data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
```

## MySQL

To connect to a MySQL database and perform a simple query in Python, you will need to have the **`mysql-connector-python`** library installed. If you don't have it, you can install it using **`pip install mysql-connector-python`**.

Here's a basic example:

```python
import mysql.connector

def connect_to_mysql():
    try:
        # Connect to the MySQL database (replace the placeholders with your own credentials)
        conn = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )

        if conn.is_connected():
            print("Connected to MySQL database.")

            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Execute a simple query
            query = "SELECT * FROM your_table"
            cursor.execute(query)

            # Fetch and print the query results
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            # Close the cursor and connection
            cursor.close()
            conn.close()
            print("Connection closed.")
        else:
            print("Failed to connect to MySQL database.")

    except mysql.connector.Error as e:
        print(f"Error occurred: {e}")

# Example usage
connect_to_mysql()
```

In this example, replace the placeholders **`your_host`**, **`your_username`**, **`your_password`**, **`your_database`**, and **`your_table`** with your actual MySQL database credentials and table name.

The example connects to the MySQL database, performs a simple SELECT query to fetch all the records from a table, and then prints the results. After executing the query, the connection is closed properly.

Please ensure that you have the necessary credentials to access the MySQL database, and the specified table exists with the appropriate data. Additionally, make sure that your Python environment has network access to the MySQL server if it's not on the same machine.

```python

import mysql.connector
try:
    # Connect to the MySQL server (replace the placeholders with your own credentials
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306
    )
except Exception as obj:
    print("Can't connect")
else:
    print("Connected")
```

## PostgreSQL

To connect to a PostgreSQL database and perform a simple query in Python, you will need to have the **`psycopg2`** library installed. If you don't have it, you can install it using **`pip install psycopg2`**.

Here's a basic example:

```python
import psycopg2

def connect_to_postgresql():
    try:
        # Connect to the PostgreSQL database (replace the placeholders with your own credentials)
        conn = psycopg2.connect(
            host="your_host",
            database="your_database",
            user="your_username",
            password="your_password"
        )

        if conn:
            print("Connected to PostgreSQL database.")

            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Execute a simple query
            query = "SELECT * FROM your_table"
            cursor.execute(query)

            # Fetch and print the query results
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            # Close the cursor and connection
            cursor.close()
            conn.close()
            print("Connection closed.")
        else:
            print("Failed to connect to PostgreSQL database.")

    except psycopg2.Error as e:
        print(f"Error occurred: {e}")

# Example usage
connect_to_postgresql()
```

In this example, replace the placeholders **`your_host`**, **`your_database`**, **`your_username`**, **`your_password`**, and **`your_table`** with your actual PostgreSQL database credentials and table name.

The example connects to the PostgreSQL database, performs a simple SELECT query to fetch all the records from a table, and then prints the results. After executing the query, the connection is closed properly.

Please ensure that you have the necessary credentials to access the PostgreSQL database, and the specified table exists with the appropriate data. Additionally, make sure that your Python environment has network access to the PostgreSQL server if it's not on the same machine.

## Oracle Database

To connect to an Oracle database and perform a simple query in Python, you will need to have the **`cx_Oracle`** library installed. If you don't have it, you can install it using **`pip install cx_Oracle`**.

Here's a basic example:

```python
import cx_Oracle

def connect_to_oracle():
    try:
        # Connect to the Oracle database (replace the placeholders with your own credentials)
        conn = cx_Oracle.connect(
            user="your_username",
            password="your_password",
            dsn="your_dsn"  # Replace with your DSN (Data Source Name)
        )

        if conn:
            print("Connected to Oracle database.")

            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Execute a simple query
            query = "SELECT * FROM your_table"
            cursor.execute(query)

            # Fetch and print the query results
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            # Close the cursor and connection
            cursor.close()
            conn.close()
            print("Connection closed.")
        else:
            print("Failed to connect to Oracle database.")

    except cx_Oracle.Error as e:
        print(f"Error occurred: {e}")

# Example usage
connect_to_oracle()
```

In this example, replace the placeholders **`your_username`**, **`your_password`**, and **`your_dsn`** with your actual Oracle database credentials and Data Source Name (DSN).

The example connects to the Oracle database, performs a simple SELECT query to fetch all the records from a table, and then prints the results. After executing the query, the connection is closed properly.

Please ensure that you have the necessary credentials to access the Oracle database, and the specified table exists with the appropriate data. Additionally, make sure that you have the Oracle Instant Client installed and properly configured on your system, as it's required for **`cx_Oracle`** to connect to the Oracle database.

## How to create connection to Mysql using python

- creating connection between mysql-python
- connect() function
- Using  Exception Handling for handling  connection errors.

## Step:1

```python
import mysql.connector
```

**mysql**: - module

**connector**:- sub module

## step:2  Connect() function

```python
conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        port=3306
    )
```

conn is a obj for the connect method

here we have to give correct credentials else it will raise the exception.

```python
Traceback (most recent call last):
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\connection_cext.py", line 288, in _open_connection
    self._cmysql.connect(**cnx_kwargs)
_mysql_connector.MySQLInterfaceError: Access denied for user 'root'@'localhost' (using password: YES)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "f:\courses\Python\pdbc\main.py", line 3, in <module>
    conn=mysql.connector.connect(
         ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\pooling.py", line 293, in connect
    return CMySQLConnection(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\connection_cext.py", line 118, in __init__
    self.connect(**kwargs)
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\abstracts.py", line 1178, in connect
    self._open_connection()
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\connection_cext.py", line 293, in _open_connection
    raise get_mysql_exception(
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

[Done] exited with code=1 in 0.312 seconds
```

So in order to handle the errors we use exception handling : here are the code for that

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
except Exception as obj:
    print("Error: ",obj)
else:
    print("Connected")
```

if error occurs it will give the output like:

```python
Error:  1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

Another way for connecting data base

```python
import mysql.connector
# create the details as dictionary
config={                             
    'host':'localhost',
    'user':'root',
    'password':'root',
    'port':3306
}
try:
    conn=mysql.connector.connect(**config)

except:
    print("Connection Error")
```

## Check connection Between Python and mysql and close connection

Check connection status: is_connected()

Closing connection: - close()

### is_connected()

Syntax:

```python
connection_object.is_connected()
# It returns boolean value
```

```python
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306
    )
    if conn.is_connected():
        print('Connected to MySQL Server')
except Exception as obj:
    print('Error',obj)
else:
    print("Connected")
```

### Closing connection: - close()

syntax:

```python
objectreference.close()
```

why we have close the connection

- resource consumption’
- Resource Management
- Connection Limits
- security
- Application stability

```python
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306
    )
    if conn.is_connected():
        print('Connected to MySQL Server')
except Exception as obj:
    print('Error',obj)
else:
    print("Connected")

conn.close()
```

## Sql Query Using through Python script

- Cursor object
- execute() method

### Cursor object

It allows python code to execute sql command in a data base session

cursor actually points to results, data etc.

### How to create Cursor object

syntax:

```python
connectobjectreference.cursor()

```

Example:

```python
conn.cursor()  # conn is object reference of connect
```

example for creating  the cursor object

```python
cur=conn.cursor()
# cur is a object reference cursor
# conn is object reference of connect
```

```python
cur.close
```

**`cur.close()`** is used to explicitly close the cursor in Python when working with databases. A cursor is an object that allows you to interact with the database and execute SQL statements.

After you have finished performing database operations using the cursor, you should close it to release any resources associated with it. Similar to closing the connection, closing the cursor ensures proper resource management and helps maintain the stability and efficiency of your application.

### execute() method

syntax:

```python
cursor_object.execute(Query,param=None)  # query is a string argument

```

example:

```python
cur=conn.cursor()
cur.execute("SQL Query")
```

**Example for creating a database** 

```python
import mysql.connector
try:
     # Connect to the MySQL database
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
    
    # checking the data base is connected or not
    if conn.is_connected():
        print("Connected to mysql db")

    # Create a cursor to interact with the database
    cur=conn.cursor()

    # Perform database operations here
    cur.execute("create database if not exists emp")
    

except Exception as obj:
    print("Except",obj)

finally:
    # Close the cursor and connection
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed")
```

**`cur.execute("CREATE DATABASE IF NOT EXISTS emp")`** 

is used to create a new database named "emp" if it does not already exist in the MySQL server. 

The **`IF NOT EXISTS`** clause ensures that the database creation is skipped if the database with the specified name is already present.

With the **`CREATE DATABASE IF NOT EXISTS`** query, the code will create the "emp" database only if it doesn't already exist, ensuring that the operation is safe and won't raise an error if the database is already there.

The **`locals()`** function in Python returns a dictionary containing the current local scope's local variables, where the variable names are the keys, and the variable values are the corresponding values. By using **`'cur' in locals()`**, you are checking if the variable **`cur`** exists in the current local scope.

it prevents a **`NameError`** in case the **`try`** block raises an exception before the **`cur`** variable is defined. If an exception occurs during the database operations and the **`cur`** variable remains undefined, trying to close it directly with **`cur.close()`** would raise an error. The check ensures that the cursor is only closed when it exists.

## Show Database Using python

- Create database connection
- Create cursor object
- Execute the query
- print cursor result

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Connected to mysql Data base")
except:
    print("Cannot connect")

cur=con.cursor()
cur.execute("SHOW DATABASES")
cur.close()
conn.close()
```

<aside>
💡 output:  error because  when the python program and sql database are connected and sql query executed then the result is stored in the memory and cursor object  is pointer of the memory. so to get the data we can print the data  using the cursor object.

</aside>

```python
Connected to mysql Data base
Traceback (most recent call last):
  File "f:\courses\Pythonmod.py", line 29, in <module>
    cur.close()
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\cursor_cext.py", line 495, in close
    self._cnx.handle_unread_result()
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\connection_cext.py", line 921, in handle_unread_result
    raise InternalError("Unread result found")
mysql.connector.errors.InternalError: Unread result found
```

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Connected to mysql Data base")
except:
    print("Cannot connect")

cur=conn.cursor()
cur.execute("SHOW DATABASES")
for data in cur:
    # print(data) #  # Print the entire row as a tuple
    print(data[0]) # Print the value of the first column (index 0)
cur.close()
conn.close()
```

Output

```python
Connected to mysql Data base
emp
information_schema
mysql
performance_schema
sys
world
```

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Connected to mysql Data base")
except:
    print("Cannot connect")

cur=conn.cursor()
cur.execute("SHOW DATABASES")
for data in cur:
    print(data[0]) # Print the value of the first column (index 0)
print(list(cur)) #empty list
cur.close()
conn.close()
```

output

```python
Connected to mysql Data base
emp
information_schema
mysql
performance_schema
sys
world
[]
```

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Connected to mysql Data base")
except:
    print("Cannot connect")

cur=conn.cursor()
cur.execute("SHOW DATABASES")
for data in cur:
    print(data[0])  # Print the value of the first column (index 0)
for data in cur:
    print(data[0])
cur.close()
conn.close()
```

output:

Here even though we have iterated using the for loop 

here the cursor have a list and it has data which is database name and in the first for loop these data is consumed and later  it is deleted by cursor object. so again the for loop is started so there is no data to print so empty 

result is printed

```python
Connected to mysql Data base
emp
information_schema
mysql
performance_schema
sys
world
```

```python
# importing the libraries

import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Connected to mysql Data base")
    
    cur=conn.cursor()
    cur.execute("SHOW DATABASES")
    for data in cur:
        # print(data)  # Print the entire row as a tuple
        print(data[0])
   

except Exception as obj:
    print("Error",obj)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed")
```

output

```python
Connected to mysql Data base
emp
information_schema
mysql
performance_schema
sys
world
```

```python
import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306
    )
    if conn.is_connected():
        print("Connected to MySQL Database")

    cur = conn.cursor()
    cur.execute("SELECT * FROM your_table")

    # Fetch and print data from the cursor
    for data in cur:
        print(data)      # Print the entire row as a tuple
        print(data[0])   # Print the value of the first column (index 0)

except Exception as obj:
    print("Error:", obj)

finally:
    # Close the cursor and connection
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed")
```

# Insert Records into mysql table using python script  Commit() method & Rollback()

- insert records into mysql table.
- commit() method
- rollback() method

**insert records into mysql table.**

- inserting single row at a time.
- inserting multiple rows at a time.

```sql
INSERT INTO table_name(coloumn_names)VALUES(data)
```

### Why we have to use commit()?

suppose we have a sql table we have to update or insert some  data to it, then we write a sql query and execute it, inorder to update or insert the data to a table. we have to send a commit statement to mysql server.

In mysql command line and work bench implicitly takes care about the commit statements. so we explicitly doesn’t require to write commit.

But in python script we have to write this commit() method explicitly

## Commit() Method

- Used to save inserted row in the table.
- It is required to make the changes, otherwise no changes are made to the table.

Syntax:

```python
con.commit()
```

- SQL Server:- AUTOCOMMIT() is there
- Through python script:- AUTOCOMMIT() is’nt there.

## rollback()

- Undo the changes if any error occurs.

if any data transaction is failed then by using rollback we can undo the operation. there will be no data loss

syntax:

```python
con.rollback()
```

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Database is connected to Mysql")
    cur=conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS emp")
    cur.execute("USE emp")
    cur.execute("CREATE TABLE IF NOT EXISTS emp(empno INT,ename VARCHAR(20),sal INT)")
    sql="INSERT INTO emp(empno,ename,sal)VALUES(1,'yash',30000)"
    cur.execute(sql)

except Exception as obj:
    print("Error",obj)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database is disconnected from Mysql")
```

Here no data is inserted into the table because no commit() is used in the code.

```python

output in python:

Database is connected to Mysql
Database is disconnected from Mysql

output: in sql
select * from emp;
Empty set (0.00 sec)
```

By using the commit()

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Database is connected to Mysql")
    cur=conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS emp")
    cur.execute("USE emp")
    cur.execute("CREATE TABLE IF NOT EXISTS emp(empno INT,ename VARCHAR(20),sal INT)")
    sql="INSERT INTO emp(empno,ename,sal)VALUES(1,'yash',30000)"
    cur.execute(sql)
    conn.commit() # by using the commit() we can save the data

except Exception as obj:
    print("Error",obj)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database is disconnected from Mysql")
```

Output:

```python

output in python:

Database is connected to Mysql
Database is disconnected from Mysql

 Output; Mysql

mysql> select * from emp;
+-------+-------+-------+
| empno | ename | sal   |
+-------+-------+-------+
|     1 | yash  | 30000 |
+-------+-------+-------+
1 row in set (0.00 sec)
```

creating a database and inserting the data to it 

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Database is connected to Mysql")
    cur=conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS emp")
    cur.execute("USE emp")
    cur.execute("CREATE TABLE IF NOT EXISTS emp(empno INT PRIMARY KEY,ename VARCHAR(20),sal INT)")
    sql="INSERT INTO emp(empno,ename,sal)VALUES(1,'yash',30000),(2,'teja',30000),(3,'Ayu',40000),(4,'yash',30000)"
    cur.execute(sql)
    conn.commit()
    print("Data successfully Inserted")
    print(f"{cur.rowcount} rows inserted") # for showing how many rows inserted

except Exception as obj:
    print("Error",obj)
    conn.rollback()
    print("Something went wrong!!")

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database is disconnected from Mysql")
```

```python
Database is connected to Mysql
Data successfully Inserted
4 rows inserted
Database is disconnected from Mysql

Output in sql:

mysql> select * from emp;
+-------+-------+-------+
| empno | ename | sal   |
+-------+-------+-------+
|     1 | yash  | 30000 |
|     2 | teja  | 30000 |
|     3 | Ayu   | 40000 |
|     4 | yash  | 30000 |
+-------+-------+-------+
4 rows in set (0.00 sec)
```

rollback()

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Database is connected to Mysql")
    cur=conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS emp")
    cur.execute("USE emp")
    cur.execute("CREATE TABLE IF NOT EXISTS emp(empno INT PRIMARY KEY,ename VARCHAR(20),sal INT)")
    sql="INSERT INTO emp(empno,ename,sal)VALUES(1,'yash',30000),(1,'teja',30000)"
    cur.execute(sql)
    conn.commit()
    print("Data successfully Inserted")
    print(f"{cur.rowcount} rows inserted")

except Exception as obj:
    print("Error",obj)
    conn.rollback()
    print("Something went wrong!!")

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database is disconnected from Mysql")
```

output:

error because there is a duplicate record entered in data base empno is primary key so it should be unique but we  inserted as no to it 

```python
Database is connected to Mysql
Error 1062 (23000): Duplicate entry '1' for key 'emp.PRIMARY'
Something went wrong!!
Database is disconnected from Mysql
```

## Update & Delete

syntax:

```sql
UPDATE table_name SET column_name=new_value
Where condition
```

example:

```sql
 sql="UPDATE emp SET sal=40000 WHERE empno=1"
 cur.execute(sql)
 conn.commit()
 print(f"{cur.rowcount} rows are updated") # for showing how many rows inserted
 
```

```sql
DELETE FROM table_name WHERE condition
```

example:

```sql
sql1="DELETE FROM emp WHERE empno=4"    
 cur.execute(sql1)
    conn.commit()
    print(f"{cur.rowcount} rows deleted")
```

Example:

```python
import mysql.connector

try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port=3306
    )
    if conn.is_connected():
        print("Database is connected to Mysql")
    cur=conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS emp")
    cur.execute("USE emp")
    cur.execute("CREATE TABLE IF NOT EXISTS emp(empno INT PRIMARY KEY,ename VARCHAR(20),sal INT)")
    #sql="INSERT INTO emp(empno,ename,sal)VALUES(1,'yash',30000),(2,'teja',30000),(3,'Ayu',40000)"
    sql="UPDATE emp SET sal=40000 WHERE empno=1"
    sql1="DELETE FROM emp WHERE empno=4"
    cur.execute(sql)
    conn.commit()
    print(f"{cur.rowcount} rows are updated") # for showing how many rows inserted
    cur.execute(sql1)
    conn.commit()
    print(f"{cur.rowcount} rows deleted")

except Exception as obj:
    print("Error",obj)
    conn.rollback()
    print("Something went wrong!!")

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database is disconnected from Mysql")
```

```sql
Database is connected to Mysql
1 rows are updated
1 rows deleted
Database is disconnected from Mysql
```

## Fetch data from Mysql

- fetchall() method
- fetch data using python script

fetch data from mysql:

- fetchall() method
- fetchone() method
- fechmany() method

## fetchall method():

- used to fetch all data generated by SELECT Query
- returns a list of tuples. Tuple represents a row.

syntax

```python
cursor.fetchall()
```

```python
SELECT * FROM table_name
```

example:

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
    cur=db.cursor()
    sql='SELECT * FROM emp'
    cur.execute(sql)
    data=cur.fetchall()
    for ele in data:
        print(ele)

except Exception as obj:
    print("Error",obj)

finally:
    if 'cur'in locals():
        cur.close()
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Database is disconnected from mysql!!")
```

output:

```python
Database is connected  to mysql!!
(1, 'yash', 40000)
(2, 'teja', 30000)
(3, 'Ayu', 40000)
Database is disconnected from mysql!!
```

## fetchone() & fetchmany() methods

fetchone()

- fetchone() is used to fetch the one row from the database

```python
cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
data1=cur.fetchone()
data2=cur.fetchone()
print(data1)

cur.close()
db.close()
```

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
   
except Exception as obj:
    print("Error",obj)

cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
data1=cur.fetchone()
data2=cur.fetchone()
print(data1)

cur.close()
db.close()
```

output: Unread result found error

```python
Database is connected  to mysql!!
(1, 'yash', 40000)
Traceback (most recent call last):
  File "f:\courses\Python\pdbc\main.py", line 25, in <module>
    cur.close()
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\cursor_cext.py", line 495, in close
    self._cnx.handle_unread_result()
  File "C:\Program Files\Python311\Lib\site-packages\mysql\connector\connection_cext.py", line 921, in handle_unread_result
    raise InternalError("Unread result found")
mysql.connector.errors.InternalError: Unread result found
```

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
   
except Exception as obj:
    print("Error",obj)

cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
try:
    data1=cur.fetchone()
    data2=cur.fetchone()
    print(data1)
    print(data2)
    cur.close()
except:
    print(f"Unread result found")

db.close()
```

output:

```python
Database is connected  to mysql!!
(1, 'yash', 40000)
(2, 'teja', 30000)
Unread result found
```

by using fetchone() we can get one row in database but we can also get desired number of rows by iterating the number of  rows

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
   
except Exception as obj:
    print("Error",obj)

cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
try:
    n=int(input("Enter the number of rows:"))
    for i in range(n):
       data1=cur.fetchone()
       print(data1)
    cur.close()
except:
    print(f"Unread result found")

db.close()
```

Output:  

Here only data in database is printed and remaining will  be printed None.

```python
Database is connected  to mysql!!
Enter the number of rows:10
(1, 'yash', 40000)
(2, 'teja', 30000)
(3, 'Ayu', 40000)
None
None
None
None
None
None
None
```

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
   
except Exception as obj:
    print("Error",obj)

cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
try:
    n=int(input("Enter the number of rows:"))
    for i in range(n):
       data1=cur.fetchone()
       if data1==None:
            continue
       print(data1)
    cur.close()
except:
    print(f"Unread result found")

db.close()
```

output

```python
Database is connected  to mysql!!
Enter the number of rows:10
(1, 'yash', 40000)
(2, 'teja', 30000)
(3, 'Ayu', 40000)
```

if we don’t know how many rows in the database we can use the while loop to iterate until the None

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
   
except Exception as obj:
    print("Error",obj)

cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
try:
    while True:
       data1=cur.fetchone()
       if data1==None:
            break
       print(data1)
    cur.close()
except:
    print(f"Unread result found")

db.close()
```

Output:

```python
Database is connected  to mysql!!
(1, 'yash', 40000)
(2, 'teja', 30000)
(3, 'Ayu', 40000)
```

## fetchmany()

fetchmany() returns list with many records and we can specify the no of the rows.

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='emp',
        port=3306
    )
    if db.is_connected():
        print("Database is connected  to mysql!!")
   
except Exception as obj:
    print("Error",obj)

cur=db.cursor()
sql='SELECT * FROM emp'
cur.execute(sql)
try:
    data1=cur.fetchmany(2)
    print(data1)
    cur.close()
except:
    print(f"Unread result found")

db.close()
```

```python
Database is connected  to mysql!!
[(1, 'yash', 40000), (2, 'teja', 30000)]
Unread result found
```

# Parameterized Query

- It is a query in which placeholders(%s) are used for parameters/variables.
- values are supplied at runtime.

example:

```python
sql="UPDATE emp SET sal= %s WHERE id= %s"
cursor.execute(sql,(20000,4))
db.commit()
```

```python
import mysql.connector

def update_employee_salary(empno, new_salary):
    try:
        # Connect to the MySQL database 
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='emp'
        )

        if conn.is_connected():
            print("Connected to MySQL Database")

            # Create a cursor object to interact with the database
            cursor = conn.cursor()

            # Prepare the UPDATE query
            update_query = "UPDATE emp SET sal = %s WHERE empno = %s"

            # Data to be updated in the table
            employee_data = (new_salary, empno)

            # Execute the UPDATE query with the data
            cursor.execute(update_query, employee_data)

            # Commit the changes to the database
            conn.commit()
            print("Salary updated successfully.")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed.")

# Example usage: Updating the salary of employee with empno=1 to 50000
update_employee_salary(1, 50000)

```

output:

```python
Output for python:

Connected to MySQL Database
Salary updated successfully.
Connection closed.

Output for sql:

select * from emp;
+-------+-------+-------+
| empno | ename | sal   |
+-------+-------+-------+
|     1 | yash  | 50000 |
|     2 | teja  | 30000 |
|     3 | Ayu   | 40000 |
+-------+-------+-------+
3 rows in set (0.00 sec)
```

Example: the **`update_employee_salary`** function takes an **`empno`** and a **`new_salary`** as arguments, and it updates the salary of the employee with the given **`empno`**. 

# Prepared statement:

- Query
- Parsing(syntactically & semantically correct)
- Verify privileges

A prepared statement is a way of executing SQL queries in a database with placeholders for parameters. It involves three main steps:

1. **Query**: The query is the SQL statement that you want to execute, but with placeholders for parameters instead of actual values.
2. **Parsing**: The parsing step involves sending the query to the database engine. The database engine parses the query to check its syntax and semantics for correctness. This step ensures that the query is valid and can be executed.
3. **Verify Privileges**: Before executing the prepared statement, the database system verifies the privileges of the user who is trying to execute it. The user must have the necessary permissions to perform the operations specified in the prepared statement.

```python
"update emp SET salary=%s WHERE id=%s"
```

```python
import mysql.connector

def update_employee_salary(empno, new_salary):
    try:
        # Connect to the MySQL database (replace the placeholders with your own credentials)
        conn = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='emp'
        )

        if conn.is_connected():
            print("Connected to MySQL Database")

            # Create a cursor object to interact with the database
            cursor = conn.cursor(prepared=True)

            # Prepare the query with placeholders
            update_query = "UPDATE employees SET sal = %s WHERE empno = %s"

            # Verify privileges (Optional step, handled by the database system)
            cursor.execute("USE your_database")  # Change to your database name

            # Parsing (syntactically & semantically correct)
            cursor.execute(update_query)  # The parsing step is handled when preparing the statement

            # Data to be updated in the table
            employee_data = (new_salary, empno)

            # Execute the prepared statement with the data
            cursor.execute(None, employee_data)

            # Commit the changes to the database
            conn.commit()
            print("Salary updated successfully.")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed.")

# Example usage: Updating the salary of employee with empno=1 to 40000
update_employee_salary(1, 40000)
```

In this example, the **`cursor`** object is created with **`prepared=True`**, which tells the MySQL connector to prepare the statement with placeholders. The parsing step is handled when the statement is prepared.

Before executing the prepared statement, you can optionally verify privileges by using the **`cursor.execute("USE your_database")`** command. This step ensures that the user has the necessary permissions to update the database.

Finally, the **`execute()`** method is used to execute the prepared statement with the actual data (**`employee_data`**). The placeholders **`%s`** in the prepared statement are replaced with the corresponding values from the **`employee_data`** tuple.

Using prepared statements is generally considered more secure and efficient than executing regular SQL queries directly since it helps prevent SQL injection attacks and can improve the performance of repeated similar queries.

**Parameterised Query  example:**

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='medicines',
        port=3306
    )
    if db.is_connected():
        print("Connected To Mysql Database")
except Exception as e:
    print("Error",e)

cur=db.cursor(prepared=True)

sql_query="""INSERT INTO medicines(drug_id,drug_name,price,expiry)VALUES(%s,%s,%s,%s)"""

n=int(input("Enter the no of medicines: "))
for i in range(n):
    drug_id=int(input("Enter the drug id: "))
    drug_name=(input("Enter the drug name: "))
    price=float(input("Enter the price: "))
    date=input("Enter the expiry date:(yyy-mm-dd):")
    cur.execute(sql_query,(drug_id,drug_name,price,date))
    db.commit()
cur.close()
```

output:

```python
Connected To Mysql Database
Enter the no of medicines: 3
Enter the drug id: 101
Enter the drug name: Dolo
Enter the price: 22.0
Enter the expiry date:(yyy-mm-dd):2025-02-01
Enter the drug id: 102
Enter the drug name: Paracetomol
Enter the price: 30.2
Enter the expiry date:(yyy-mm-dd):2024-02-03
Enter the drug id: 103
Enter the drug name: anacine
Enter the price: 25.0
Enter the expiry date:(yyy-mm-dd):2025-05-25
```

# CRUD operations  on the "medicines" table

1. Use of **`commit()`**:
    - **`commit()`** method should be called on the connection, not the cursor. After executing all the queries, call **`conn.commit()`** to commit the changes to the database.
2. Passing parameters to execute() method:
    - When using placeholders in the SQL query, pass the parameters to the **`execute()`** method using a tuple or a dictionary.
3. Retrieving data from cursor:
    - When fetching data from the cursor, use **`fetchone()`** or **`fetchall()`** methods to retrieve the results.
4. Calling undefined variable **`cur`**:
- The **`cur`** variable is defined within the **`database()`** function. To use it in other functions, declare it as a global variable.

```python
import mysql.connector

# Define cur and conn as global variables
cur = None
conn = None

def database():
    global cur, conn  # Declare cur and conn as global variables
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            port=3306
        )
        if conn.is_connected():
            print("Database is connected mysql!!")
        cur = conn.cursor()
        cur.execute("create database if not exists medicines")
        cur.execute("use medicines")
        cur.execute("create table if not exists medicines (drug_id Int Primary key, drug_name varchar(255), price FLOAT, expiry date)")

        # Commit the changes to the database
        conn.commit()
        print("Database and table created successfully")

    except Exception as e:
        print("Error", e)

def insert_to_database(drug_id, drug_name, price, expiry):
    try:
        # SQL query with placeholders
        sql = 'INSERT INTO medicines (drug_id, drug_name, price, expiry) VALUES (%s, %s, %s, %s)'

        # Data to be inserted into the table
        data = (drug_id, drug_name, price, expiry)

        # Execute the query with the data
        cur.execute(sql, data)

        # Commit the changes to the database
        conn.commit()
        print("Data inserted successfully")
        print(f"{cur.rowcount} rows are inserted")

    except Exception as e:
        print("Error", e)

def update_to_database(drug_id, drug_name, price, expiry):
    try:
        # SQL query with placeholders
        sql = 'UPDATE medicines SET drug_name=%s, price=%s, expiry=%s WHERE drug_id=%s'

        # Data to be updated in the table
        data = (drug_name, price, expiry, drug_id)

        # Execute the query with the data
        cur.execute(sql, data)

        # Commit the changes to the database
        conn.commit()
        print("Data updated successfully")
        print(f"{cur.rowcount} rows are updated")

    except Exception as e:
        print("Error", e)

def delete_to_database(drug_id):
    try:
        # SQL query with placeholders
        sql = 'DELETE FROM medicines WHERE drug_id=%s'

        # Data (drug_id) to be deleted from the table
        data = (drug_id,)

        # Execute the query with the data
        cur.execute(sql, data)

        # Commit the changes to the database
        conn.commit()
        print("Data deleted successfully")
        print(f"{cur.rowcount} rows are deleted")

    except Exception as e:
        print("Error", e)

def display_database():
    try:
        # SQL query to fetch all records
        sql = 'SELECT * FROM medicines'

        # Execute the query
        cur.execute(sql)

        # Fetch all records from the cursor
        records = cur.fetchall()

        # Print the fetched records
        for row in records:
            print(row)

    except Exception as e:
        print("Error", e)

def search_database(drug_id):
    try:
        # SQL query with placeholders
        sql = 'SELECT * FROM medicines WHERE drug_id=%s'

        # Data (drug_id) to be searched in the table
        data = (drug_id,)

        # Execute the query with the data
        cur.execute(sql, data)

        # Fetch the matching record from the cursor
        record = cur.fetchone()

        # Print the fetched record
        print(record)

    except Exception as e:
        print("Error", e)

# Call the database function to set up the database and table
database()

#  Inserting a new record
insert_to_database(1, 'pst', 100, '2025-02-24')
insert_to_database(2, 'pst', 100, '2025-02-24')

#  Updating the record with drug_id=1
update_to_database(1, 'paracetomol', 200, '2025-02-24')

#  Deleting the record with drug_id=1
delete_to_database(2)

#  Display all records
display_database()

#  Search for a specific record with drug_id=1
search_database(1)

cur.close()
if conn.is_connected():
    conn.close()
    print("MySQL connection is closed")
```

Output:

```python
Database is connected mysql!!
Database and table created successfully
Data inserted successfully
1 rows are inserted
Data inserted successfully
1 rows are inserted
Data updated successfully
1 rows are updated
Data deleted successfully
1 rows are deleted
(1, 'paracetomol', 200.0, datetime.date(2025, 2, 24))
(1, 'paracetomol', 200.0, datetime.date(2025, 2, 24))
MySQL connection is closed
```

# Parameterized Query for Dynamic program

- In parameterized query  we used tuple  so we need to maintain the order while inserting the data even if we passed  with keyword arguments the position is fixed and we need to pass the same way the positions of the keyword argument
- ex- This is the order drug_name, price, expiry, drug_id when we pass to the query. if the position durg_id is written first  even through we pass keyword argument the postion must be same
- if we don’t want to follow the positions we can use dictnoary

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='medicines',
        port=3306
    )
    if db.is_connected():
        print("Connected To Mysql Database")
except Exception as e:
    print("Error",e)

cur=db.cursor(prepared=True)

sql_query="""INSERT INTO medicines(drug_id,drug_name,price,expiry)VALUES(%(drug_id),%(drug_name),%(price),%(date))"""

n=int(input("Enter the no of medicines: "))
for i in range(n):
    drug_id=int(input("Enter the drug id: "))
    drug_name=(input("Enter the drug name: "))
    price=float(input("Enter the price: "))
    date=input("Enter the expiry date:(yyy-mm-dd):")
    cur.execute(sql_query,{'drug_name':drug_name,'drug_id':drug_id,'price':price,'date':date}) # here you can use any order
    db.commit()
cur.close()
```

```python
import mysql.connector

try:
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='medicines',
        port=3306
    )
    if db.is_connected():
        print("Connected To Mysql Database")
except Exception as e:
    print("Error",e)

cur=db.cursor(prepared=True)

sql_query="""INSERT INTO medicines(drug_id,drug_name,price,expiry)VALUES(%(drug_id),%(drug_name),%(price),%(date))"""

n=int(input("Enter the no of medicines: "))
while True:
    drug_id=int(input("Enter the drug id: "))
    drug_name=(input("Enter the drug name: "))
    price=float(input("Enter the MRP price: "))
    expiry_date=input("Enter the expiry date:(yyy-mm-dd):")
    cur.execute(sql_query,{'drug_name':drug_name,'drug_id':drug_id,'price':price,'expiry_date':expiry_date}) # here you can use any order
    db.commit()
    ans= input("Do you have more medicines:(y/n):").lower()
    if ans!='y':
        break
    print("-"*50)
cur.close()

if db.is_connected():
    db.close()
    print("Disconnected from mysql database")
```

How to insert json data to mysql table.

data.json

```json
[
{
    "name":"yaswanth Teja",
    "age":23,
    "salary":50000
},
{
    "name":"Teja",
    "age":22,
    "salary":45000

},
{
    "name":"ravi",
    "age":21,
    "salary":40000
},
{
    "name":"sai",
    "age":20,
    "salary":35000
},
{
    "name":"siva",
    "age":19,
    "salary":30000
},
{
    "name":"sai",
    "age":18,
    "salary":25000
},
{
    "name":"surya",
    "age":17,
    "salary":20000
},
{
    "name":"suri",
    "age":16,
    "salary":15000
},
{
    "name":"sesi",
    "age":15,
    "salary":10000
},
{
    "name":"miku",
    "age":14,
    "salary":5000
}
]
```

create a table 

```sql
create table info(name varchar(255),age int, salary float);
```

```python
import json
import mysql.connector

with open('Data.json','r')as f:
    data=json.load(f) # load used to read the data

print(data)

try:
    con=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        port='3306',
        database='emp'
    )
    if con.is_connected():
        print("Data base is connected!!")
except Exception as e:
    print("Error",e)

cur=con.cursor()
for item in data:
    print(item)
    val=(item['name'],item['age'],item['salary'])
    sql="insert into info(name,age,salary)VALUES(%s,%s,%s)"
    cur.execute(sql,val)
    con.commit()
    print(cur.rowcount,"rows got inserted")
cur.close()
con.close()
```

Output:

```python
Data base is connected!!
{'name': 'yaswanth Teja', 'age': 23, 'salary': 50000}
1 rows got inserted
{'name': 'Teja', 'age': 22, 'salary': 45000}
1 rows got inserted
{'name': 'ravi', 'age': 21, 'salary': 40000}
1 rows got inserted
{'name': 'sai', 'age': 20, 'salary': 35000}
1 rows got inserted
{'name': 'siva', 'age': 19, 'salary': 30000}
1 rows got inserted
{'name': 'sai', 'age': 18, 'salary': 25000}
1 rows got inserted
{'name': 'surya', 'age': 17, 'salary': 20000}
1 rows got inserted
{'name': 'suri', 'age': 16, 'salary': 15000}
1 rows got inserted
{'name': 'sesi', 'age': 15, 'salary': 10000}
1 rows got inserted
{'name': 'miku', 'age': 14, 'salary': 5000}
1 rows got inserted
```

```python
mysql> select * from info;
+---------------+------+--------+
| name          | age  | salary |
+---------------+------+--------+
| yaswanth Teja |   23 |  50000 |
| Teja          |   22 |  45000 |
| ravi          |   21 |  40000 |
| sai           |   20 |  35000 |
| siva          |   19 |  30000 |
| sai           |   18 |  25000 |
| surya         |   17 |  20000 |
| suri          |   16 |  15000 |
| sesi          |   15 |  10000 |
| miku          |   14 |   5000 |
+---------------+------+--------+
10 rows in set (0.00 sec)
```

























