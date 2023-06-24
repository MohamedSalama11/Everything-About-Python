# A Database :- is a collection of data stored in a format that can easily be accessed, in order to manage our databases we used a software application called DBMS ( Database Management System )

### Difference Between SQL & MySQL ###
    # SQL ( Structured Query Language ) is a programming language used to manage and manipulate relational databases. It is used to perform various tasks such as inserting, updating, deleting
#   or querying data in a database. SQL is not a database management system, but rather a language that database management systems use.
    # MySQL, on the other hand, is a popular Relational Database Management System ( RDBMS ) that uses SQL as it's language for managing and manipulating data.
#     MySQL is open-source and is widely used on the web and in enterprise applications.
    # In summary, SQL is a language used to work with databases while MySQL is a specific type of database management system that uses SQL as its language.
#     Other popular RDBMS that use SQL include Oracle, Microsoft SQL Server, and PostgreSQL.
print("Hello world")
# DBMS Divided To:- 
    # 1- Relational Databases ( SQL )  => like MySQL, SQL Server, Oracle
        # in relatoinal databases we used tables that connected with each others by relationships
        # SQL ( Structured Query Language ) => is the language we use to work with Relational DBMS, or it is the language we use to talk to our databases
    # 2- Non Relational Databases or NoSQL
        # in non relational databases we don't have tables or relationships, don't understand SQL, they have their own query langauge such as MongoDB

# Query => is the line of code you write with SQL language

# When you learn SQL language with any DBMS like mysql it's not that hard to switch to other DBMS that also uses SQL language like ( SQLite or PostgreSQL, Oracle )

# There's alot of data types in mysql like varchar (string), int (numbers)
    # varchar(10)   => this means you can write 10 characters maximum ("Mohamed")
    # int           => is just a number (432)

# CRUD => it stands for Create Read Update Delete 

## String Functions ##
# 1- CONCAT(column_one, column_two, string, ...)                  => Combine data for cleaner output (you should use SELECT before it to work or it will raise an error).
# 2- CONCAT_WS(column_one, column_two, string, ...)               => Stands for concat with separator, it means that it will put a separator you chooose between every values you put.
# 3- SUBSTRING(column_name, start position, length)               => It takes a single larger string and returns a smaller part of that string  == SUBSTR().
# 4- REPLACE(initial_str, old_str, new_str)                       => it replaces old string with new string (Case Sesnsitive ).
# 5- REVERSE(str or int)                                          => Will take whatever string we provide to it and reverse it (When you try to reverse NULL it will gives you NULL).
# 6- CHAR_LENGTH(str)                                             => It's going to tell us the number of characters in a given string.
# 7- LENGTH(str)                                                  => Returns the lenght of the string measured in bytes
# 8- UPPER(str)                                                   => Will make all the characters of the string upper  == UCASE()
# 9- LOWER(str)                                                   => Will make all the characters of the string lower  == LCASE()


# Notes
# 1- is sql case sensitive? It depends on the database management system being used. In general, SQL is not case sensitive for keywords such as SELECT, FROM, WHERE, etc
# However, it may be case sensitive for identifiers such as table and column names, depending on how the database has been configured or the collation sequence being used
    # For example, in some databases, "mytable" and "MyTable" could refer to different tables.
# 2- my sql doesn't care about new lines.
# 3- A database is just really a bunch of tables at least in relational databases, tables holding the data.
# 4- Table is a collection of related data held in a structured format within a database, it contains columns and rows.
# 5- When you put ; in the end of a line you till SQL this is the end of the command or the query.
# 6- Null in SQL doesn't means zero it means no value at all or unknown.
# 7- Before you perform update and delete operations be sure selecting the right data you want to update or delete.

############# Commands #############
# 01- show databases;                                                                                     => To show the databases you created
# 02- CREATE DATABASE <name>;                                                                             => To create a database
# 03- DROP DATABASE   <name>;                                                                             => Will remove the database and it's content
# 04- USE <database name>;                                                                                => To work with the database we choose
# 05- SELECT database();                                                                                  => To show you the database you are working in
# 06- CREATE TABLE table_name (                                                                           => To create a table (create table if not exists)
#   column_name data_type,
#   column_name data_type      
# );
# 07- CREATE TABLE table_name (                                                                           => To create a table, NOT NULL means that this column shouldn't be empty you must
#   column_name data_type NOT NULL,                                                                         write a value into it or it will raise an error
#   column_name data_type NOT NULL      
# );
# 08- CREATE TABLE table_name (                                                                           => To create a table with a default value
#   column_name data_type DEFAULT 'Mohamed',
#   column_name data_type DEFAULT 10
# );
# 09- CREATE TABLE table_name (                                                                           => To create a table, PRIMARY KEY means that this column shouldn't have the same value,
#   column_name data_type PRIMARY KEY,                                                                       the value of this column should be unique
#   column_name data_type
# );
# 10- CREATE TABLE table_name (                                                                           => Another Syntax For Primary Key
#   column_name data_type,                                                                       
#   column_name data_type,
#   PRIMARY KEY(column_name)
# );
# 11- CREATE TABLE table_name (                                                                           => AUTO_INCREMENT will automaticaly generate the numbers (1...100)
#   column_name data_type AUTO_INCREMENT PRIMARY KEY,                                                                        
#   column_name data_type,
# );
# 11- SHOW TABLES;                                                                                        => To show the tables of the database you currently in
# 12- SHOW COLUMNS FROM table_name;                                                                       => To show you information about the columns of the table you choose
# 13- DESC table_name == DESCRIBE table_name;                                                             => To show you information about the columns of the table you choose
# 14- DROP TABLE table_name;                                                                              => To delete the specified table
# 15- --                                                                                                  => To comment your line or query, shortcut key is CTRL + /
# 16- INSERT INTO table_name(columne_one, columne_two) VALUES (value1, value2)                            => To insert data into tables 
# 17- SELECT * FROM table_name                                                                            => This tells SQL give me everything you have in this specified table
# 18- INSERT INTO table_name(columne_one, columne_two) VALUES (value1, value1), (value2, value2)          => This is for multiple inserting
# 19- SELECT * FROM table_name                                                                            => This means give me all the data in all columns
# 20- SELECT column_name FROM table_name                                                                  => This means give me only the data in this column name
# 21- SELECT column_name, column_name2 FROM table_name                                                    => This means give me the data in these two columns
# 22- SELECT * FROM table_name WHERE column_name="value"                                                  => IT will search for "value" and return all the rows that have it
# 23- SELECT column_name AS col FROM table_name                                                           => AS here for aliases and can rename the column name temporary in the output
# 24- UPDATE table_name SET column_name="value"                                                           => This means update everything in column_name to value ( Always use WHERE Clause to specify the value you want to change )
# 25- UPDATE table_name SET column_name="value", column_name2="value"                                     => To update multiple values
# 26- DELETE FROM table_name                                                                              => This will delete every row from the table, will empty the table but it's still exists ( don't use it like this )
# 27- DELETE FROM table_name WHERE column_name="value"                                                    => This will delete only the specified value

