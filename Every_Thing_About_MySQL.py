# A Database :- is a collection of data stored in a format that can easily be accessed, in order to manage our databases we used a software application called DBMS ( Database Management System )
### Difference Between SQL & MySQL ###
    # SQL ( Structured Query Language ) is a programming language used to manage and manipulate relational databases. It is used to perform various tasks such as inserting, updating, deleting
#   or querying data in a database. SQL is not a database management system, but rather a language that database management systems use.
    # MySQL, on the other hand, is a popular Relational Database Management System ( RDBMS ) that uses SQL as its language for managing and manipulating data.
#     MySQL is open-source and is widely used on the web and in enterprise applications.
    # In summary, SQL is a language used to work with databases while MySQL is a specific type of database management system that uses SQL as its language.
#     Other popular RDBMS that use SQL include Oracle, Microsoft SQL Server, and PostgreSQL.
# DBMS Divided To:- 
    # 1- Relational Databases ( SQL)  => like MySQL, SQL Server, Oracle
        # in relatoinal databases we used tables that connected with each others by relationships
        # SQL ( Structured Query Language ) => is the language we use to work with Relational DBMS, or it is the language we use to talk to our databases
    # 2- Non Relational Databases or NoSQL
        # in non relational databases we don't have tables or relationships, don't understand SQL, they have their own query langauge such as MongoDB

# Query => is the line of code you write with sql language

# When you learn sql language with any DBMS like mysql it's not that hard to switch to other DBMS that also uses sql language like ( SQLite or PostgreSQL, Oracle )

# There's alot of data types in mysql like varchar (string), int (numbers)
    # varchar(10)   => this means you can write 10 characters maximum ("Mohamed")
    # int           => is just a number (432)

# Notes
# 1- is sql case sensitive? It depends on the database management system being used. In general, SQL is not case sensitive for keywords such as SELECT, FROM, WHERE, etc
# However, it may be case sensitive for identifiers such as table and column names, depending on how the database has been configured or the collation sequence being used
# For example, in some databases, "mytable" and "MyTable" could refer to different tables.
# 2- my sql doesn't care about new lines
# 3- A database is just really a bunch of tables at least in realtional databases, tables holding the data
# 4- Table is a collection of related data held in a structured format within a database, it contains columns and rows
# 5- When you put ; in the end of a line you till SQL this is the end of the line or the query
# 6- Null in SQL doesn't means zero it means no value at all or unknown

############# Commands #############
# 01- show databases;                                                                                     => to show the databases you created
# 02- CREATE DATABASE <name>;                                                                             => to create a database
# 03- DROP DATABASE   <name>;                                                                             => will remove the database and it's content
# 04- USE <database name>;                                                                                => to work with the database we choose
# 05- SELECT database()                                                                                   => to show you the database you are working in
# 06- CREATE TABLE table_name (                                                                           => to create a table (create table if not exists)
#   column_name data_type,
#   column_name data_type      
# );
# 07- CREATE TABLE table_name (                                                                           => to create a table and not null means that this column shouldn't be empty you must
#   column_name data_type NOT NULL,                                                                         write a value into it or it will raise an error
#   column_name data_type NOT NULL      
# );
# 08- # 06- CREATE TABLE table_name (                                                                     => to create a table with a default value
#   column_name data_type DEFAULT 'Mohamed',
#   column_name data_type DEFAULT 10
# );
# 09- # 06- CREATE TABLE table_name (                                                                     => to create a table, primary key means that this column shouldn't have the same value
#   column_name data_type PRIMARY KEY,                                                                       the value of this column should be unique
#   column_name data_type
# );
# 10- # 06- CREATE TABLE table_name (                                                                     => Another Syntax For Primary Key
#   column_name data_type,                                                                       
#   column_name data_type,
#   PRIMARY KEY(column_name)
# );
# 11- # 06- CREATE TABLE table_name (                                                                     => Auto_increment will automaticaly generate the numbers (1...100)
#   column_name data_type AUTO_INCREMENT PRIMARY KEY,                                                                        
#   column_name data_type,
# );
# 11- SHOW TABLES;                                                                                        => to show the tables of the database you currently in
# 12- SHOW COLUMNS FROM table_name;                                                                       => to show you information about the columns of the table you choose
# 13- DESC table_name == DESCRIBE table_name;                                                             => to show you information about the columns of the table you choose
# 14- DROP TABLE table_name;                                                                              => to delete the specified table
# 15- --                                                                                                  => to comment your line or query, shortcut key is CTRL + /
# 16- INSERT INTO table_name(columne_one, columne_two) VALUES (value1, value2)                            => to insert data into tables 
# 17- SELECT * FROM table_name                                                                            => this tells SQL give me everything you have in this specified table
# 18- INSERT INTO table_name(columne_one, columne_two) VALUES (value1, value1), (value2, value2)          => this is for multiple inserting
# 17- 
# 18- 
# 19- 
# 20- 
# 20- 
# 21- 
# 22- 
# 23- 
# 24- 
# 25- 
# 26- 
# 27- 
# 28- 
# 29- 
# 30- 
