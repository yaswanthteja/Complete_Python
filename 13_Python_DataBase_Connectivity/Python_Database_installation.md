

# Setting Up JupyterLab with Database Connections

This guide will walk you through the process of installing JupyterLab, setting up database drivers, and running SQL queries for MySQL, PostgreSQL, SQLite, MongoDB, and SQLAlchemy.

## Prerequisites
- Ensure you have Python installed on your system.
- Install any Database like mysql,postgresql,mongodb..

## Installation

-  Open your terminal and run the below commands.
- If your using mac repalce pip with pip3 and python with python3

### Step 1: Install JupyterLab
First, you need to install JupyterLab using pip:

```bash
pip install jupyterlab
```

### step 2: Start JupyterLab with:

```
jupyter lab
```

### 3. Installing SQL module in the notebook

```
 pip install ipython-sql

```

## Based on your database install  sql drivers

### 1.Mysql

### Installing the mysql in notebook

```
pip install mysql-connector-python
```


### Loading the mysql in the notebook

```
# Load the SQL extension
%load_ext sql

# Set the connection string

%sql mysql+mysqlconnector://your_username:your_password@localhost/your_database
          # replace your_database with your sql database name
```

### example:

```
%load_ext sql
%sql mysql+mysqlconnector://root:root@localhost/test         # here test is the database name
```

### Now run magic command %%sql for every shell

```
%%sql

```
### Example : if you want to run any sql command first we need to start including %%sql and following query

```
%%sql
SHOW TABLES;
```


### 2. Postgresql

### 1.Install the postgresql

```
pip install psycopg2-binary ipython-sql

```


### 2 Connecting the driver
```
# Format
# Load the SQL extension

%load_ext sql

# Set the connection string
%sql postgresql://your_username:your_password@localhost/your_database

```

# Example format
``` 
%load_ext sql
%sql postgresql://postgres:password123@localhost/dvdrental
```

- dialect+driver in this case would just be postgresql , but feel free to use a different database software here.
- username:password is where you will substitute your username and password.
- host is usually just localhost.
- In my experience, port does not need to be specified.
- database is the name of the database to connect to.


### 3. Sqlite

### Install the sqlite

```
pip install sqlite ipython-sql
```

### Connect the sqlite

```
# Load the SQL extension
%load_ext sql

# Set the connection string
%sql sqlite:///your_database.db

```

### 4. Mongodb


### Install the Mongodb
```
pip install pymongo

```


### Connecting the Mongodb

```
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.your_database

# Run a sample query
print(db.your_collection.find_one())

```


### SQLAlchemy


#### Install SqlAlchemy

```
pip install sqlalchemy ipython-sql

```

### Connect the sqlAlchemy

```
from sqlalchemy import create_engine

# Set the connection string
engine = create_engine('postgresql://your_username:your_password@localhost/your_database')

# Run a sample query
connection = engine.connect()
result = connection.execute("SELECT * FROM your_table")
for row in result:
    print(row)
connection.close()

```





