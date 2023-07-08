# A Database :- is a collection of data stored in a format that can easily be accessed, in order to manage our databases we used a software application called DBMS ( Database Management System )

### Difference Between SQL & MySQL ###
    # SQL ( Structured Query Language ) is a programming language used to manage and manipulate relational databases. It is used to perform various tasks such as inserting, updating, deleting
#   or querying data in a database. SQL is not a database management system, but rather a language that database management systems use.
    # MySQL, on the other hand, is a popular Relational Database Management System ( RDBMS ) that uses SQL as it's language for managing and manipulating data.
#     MySQL is open-source and is widely used on the web and in enterprise applications.
    # In summary, SQL is a language used to work with databases while MySQL is a specific type of database management system that uses SQL as its language.
#     Other popular RDBMS that use SQL include Oracle, Microsoft SQL Server, and PostgreSQL.

# DBMS Divided To:- 
    # 1- Relational Databases ( SQL )  => like MySQL, SQL Server, Oracle
        # in relatoinal databases we used tables that connected with each others by relationships
        # SQL ( Structured Query Language ) => is the language we use to work with Relational DBMS, or it is the language we use to talk to our databases
    # 2- Non Relational Databases or NoSQL
        # in non relational databases we don't have tables or relationships, don't understand SQL, they have their own query langauge such as MongoDB

# Query    => Is the line of code you write with SQL language
# subquery => It's a query within a larger query, we surround it with parentheses, and this tells MySQL to run subquery first 

# When you learn SQL language with any DBMS like mysql it's not that hard to switch to other DBMS that also uses SQL language like ( SQLite or PostgreSQL, Oracle )

# There's alot of data types in mysql like varchar (string), int (numbers)
    # varchar(10)   => this means you can write 10 characters maximum ("Mohamed")
    # int           => is just a number (432)

# CRUD => it stands for Create Read Update Delete

############# Data Types #############
# 1- CHAR(length)                                                   => To store strings, it has a fixed length, we use char when our data is similar in size, EX CHAR(3) => this means that this column
#                                                                      should always be three characters, but if it's smaller than 3 characters MySQL will exapnd it using whitespace characters to fit 
#                                                                      three characters, and will take 3 bytes of memory.
# 2- VARCHAR(length)                                                => To store strings, we use it when we don't know the length of the string or when we insert long strings, it's more efficient.
# 3- INT or INTEGER                                                 => To store large numbers
# 4- TINYINT                                                        => To store small numbers (up to 127)
# 5- BIGINT                                                         => To store larger numbers
# 6- SMALLINT
# 7- MEDIUMINT
# 8- DECIMAL(total number of digits, digits after decimal)
# 9- FLOAT                                                          => it takes 4 bytes in the memory
# 10- DOUBLE                                                        => DOUBLE is more precsion than float, it takes 8 bytes in the memory
# 11- DATE                                                          => It stores a date with no time involved with format YYYY-MM-DD
# 12- TIME                                                          => It represents the time with no date with format HH:MM:SS
# 13- DATETIME                                                      => It store values with date and time with format YYYY-MM-DD HH:MM:SS

############# Notes #############
# 01- is sql case sensitive? It depends on the database management system being used. In general, SQL is not case sensitive for keywords such as SELECT, FROM, WHERE, etc
# However, it may be case sensitive for identifiers such as table and column names, depending on how the database has been configured or the collation sequence being used
    # For example, in some databases, "mytable" and "MyTable" could refer to different tables.
# 02- my sql doesn't care about new lines.
# 03- A database is just really a bunch of tables at least in relational databases, tables holding the data.
# 04- Table is a collection of related data held in a structured format within a database, it contains columns and rows.
# 05- When you put ; in the end of a line you tell SQL this is the end of the command or the query.
# 06- Null in SQL doesn't means zero it means no value at all or unknown.
# 07- Before you perform update and delete operations be sure selecting the right data you want to update or delete.
# 08- WHERE Clause to specify and select the exact value you want.
# 09- DISTINCT Clause which is used to eliminate duplicate results ( will remove duplicates ), it comes after the SELECT and before the column_name.
# 10- ORDER BY Clause it is used to order the data as we want, it comes at the end of the query, by default it sorted alphapitcally (a-z) (ASC).
# 11- When we use DESC it will describe the table, but when we use it after ORDER BY Clause it will sort the values from (z-a) (DESC).
# 12- LIMIT Clause allows you to control the number of results you get back, followed by a number.
# 13- LIKE Clause you can use it when you serach for something and you don't remember exctly what it is and we use % before and after the value (%moh%), % means zero character or more
#     and it called wildcards, it's optional, ____ (four underscores) means search for four characters because every underscore represents exactly one charcater we can escape them ( %, _ )
#     with escape sequence like this "%\%%", "%\_%". 
# 14- GROUP BY Clause summarizes or aggregates identical data into single rows.
# 15- SIGNED means the number could be negative or positive.
# 16- UNSIGNED means the number must be positive.


############# String Functions #############
# 01- CONCAT(column_one, column_two, string, ...)                  => Combine data for cleaner output ( you should use SELECT before it to work or it will raise an error ).
# 02- CONCAT_WS(separator, column_one, string, ...)                => Stands for concat with separator, it means that it will put a separator you choose between every values you put.
# 03- SUBSTRING(column_name, start position, length)               => It takes a single larger string and returns a smaller part of that string  == SUBSTR().
# 04- REPLACE(initial_str, old_str, new_str)                       => It replaces old string with new string ( Case Sensitive ).
# 05- REVERSE(str or int)                                          => Will take whatever string or int we provide to it and reverse it  (When you try to reverse NULL it will gives you NULL ).
# 06- CHAR_LENGTH(str)                                             => It's going to tell us the number of characters in a given string.
# 07- LENGTH(str)                                                  => Returns the length of the string measured in bytes
# 08- UPPER(str)                                                   => Will make all the characters of the string upper  == UCASE().
# 09- LOWER(str)                                                   => Will make all the characters of the string lower  == LCASE().
# 10- LEFT(string, number_of_chars)                                => Will Return the number of chars you need from left of the string.
# 11- RIGHT(string, number_of_chars)                               => Will Return the number of chars you need from right of the string.
# 12- INSERT()                                                     => It allows us to insert some substring into another string.
# 13- REPEAT(str, number_of_repeats)                               => Will repeat the string number of times.
# 14- TRIM(str)                                                    => Will Remove the spaces in the beginning and the end of the string not spaces between string.
# 15- COUNT(column_name)                                           => This tells you how many values are present in this column, NULL does not enter in the count.
# 16- MIN(column_name)                                             => Will give you the minimum number.
# 17- MAX(column_name)                                             => Will give you the maximum number.
# 18- SUM(column_name)                                             => Will give you the sum of all the values in the column_names, when you use sum with strings it gives you zero.
# 19- AVG(column_name)                                             => Will give you the average number.
# 20- CURRENT_DATE()                                               => Will give you the current date, CURDATE() is the shortkey
# 21- CURRENT_TIME()                                               => Will give you the current time, CURTIME() is the shortkey
# 22- CURRENT_TIMESTAMP()                                          => Will give you the actual datetime now, NOW() is the shortkey
# 23- DAYOFMONTH()                                                 => Will give you only the day of specific date, DAY() is the shortkey
# 24- DAYOFWEEK()                                                  => Will give you only the day of the week as a number 
# 25- MONTHNAME()                                                  => Will give you the name of the month 
# 26- DATE_FORMAT(date, format)                                    => Will give you the format date you want 
# 27- TIME_FORMAT(time, format)                                    => Will give you the format time you want 
# 28- DATEDIFF(exp1, exp2)                                         => Will differ the exp1 - exp2
# 29- CAST(string AS data_type)                                    => It takes a string and convert it to the data type you want

############# Logical Operators #############
# 01- Not Equal                          ( != )                              => Technically it is a comparsion operators.
# 02- NOT LIKE  
# 03- Greater Than                       ( > )                               => Technically it is a comparsion operators.
# 04- Less Than                          ( < )                               => Technically it is a comparsion operators.
# 05- Greater Than or Equal To           ( >= )                              => Technically it is a comparsion operators.
# 06- Less Than or Equal To              ( <= )                              => Technically it is a comparsion operators.
# 07- Logical AND                        ( AND )                             => The two conditions should be True, When one condition is not true sql will evaluate an empty table.
# 08- Logical OR                         ( OR )                              => Only one condition should be True.
# 09- Logical BETWEEN                    ( BETWEEN )
# 10- Logical NOT BETWEEN                ( NOT BETWEEN )
# 11- IN Operator                        ( IN )
# 12- NOT IN Operator                    ( NOT IN )
# 13- IS NULL Operator                   ( IS NULL )
# 14- IS NOT NULL Operator               ( IS NOT NULL )
# 15- 
# 16- 
# 17- 
# 18- 
# 19- 


############# Commands #############
# 01- show databases;                                                                              => To show the databases you created
# 02- CREATE DATABASE <name>;                                                                      => To create a database
# 03- DROP DATABASE   <name>;                                                                      => Will remove the database and it's content
# 04- USE <database name>;                                                                         => To work with the database we choose
# 05- SELECT database();                                                                           => To show you the database you are currently working in
# 06- CREATE TABLE table_name (                                                                    => To create a table (create table if not exists)
#   column_name data_type,
#   column_name data_type      
# );
# 07- CREATE TABLE table_name (                                                                    => To create a table, NOT NULL means that this column shouldn't be empty you must
#   column_name data_type NOT NULL,                                                                         write a value into it or it will raise an error
#   column_name data_type NOT NULL      
# );
# 08- CREATE TABLE table_name (                                                                    => To create a table with a default value
#   column_name data_type DEFAULT 'Mohamed',
#   column_name data_type DEFAULT 10
# );
# 09- CREATE TABLE table_name (                                                                    => To create a table, PRIMARY KEY means that this column shouldn't have the same value,
#   column_name data_type PRIMARY KEY,                                                                       the value of this column should be unique
#   column_name data_type
# );
# 10- CREATE TABLE table_name (                                                                    => Another Syntax For Primary Key
#   column_name data_type,                                                                       
#   column_name data_type,
#   PRIMARY KEY(column_name)
# );
# 11- CREATE TABLE table_name (                                                                    => AUTO_INCREMENT will automaticaly generate the numbers (1...100)
#   column_name data_type AUTO_INCREMENT PRIMARY KEY,                                                                        
#   column_name data_type,
# );
# 11- SHOW TABLES;                                                                                 => To show the tables of the database you currently in
# 12- SHOW COLUMNS FROM table_name;                                                                => To show you information about the columns of the table you choose
# 13- DESC table_name == DESCRIBE table_name;                                                      => To show you information about the columns of the table you choose
# 14- DROP TABLE table_name;                                                                       => To delete the specified table
# 15- --                                                                                           => To comment your line or query, shortcut key is CTRL + /
# 16- INSERT INTO table_name(columne_one, columne_two) VALUES (value1, value2)                     => To insert data into tables 
# 17- SELECT * FROM table_name                                                                     => This tells SQL give me everything you have in this specified table
# 18- INSERT INTO table_name(columne_one, columne_two) VALUES (value1, value1), (value2, value2)   => This is for multiple inserting
# 19- SELECT * FROM table_name                                                                     => This means give me all the data in all columns
# 20- SELECT column_name FROM table_name                                                           => This means give me only the data in this column name
# 21- SELECT column_name, column_name2 FROM table_name                                             => This means give me the data in these two columns
# 22- SELECT * FROM table_name WHERE column_name="value"                                           => IT will search for "value" and return all the rows that have it
# 23- SELECT column_name AS col FROM table_name                                                    => AS here for aliases and can rename the column name temporary in the output
# 24- UPDATE table_name SET column_name="value"                                                    => This means update everything in column_name to value ( Always use WHERE Clause to specify the value you want to change )
# 25- UPDATE table_name SET column_name="value", column_name2="value"                              => To update multiple values
# 26- DELETE FROM table_name                                                                       => This will delete every row from the table, will empty the table but it's still exists ( don't use it like this )
# 27- DELETE FROM table_name WHERE column_name="value"                                             => This will delete only the specified value
# 28- SHOW WARNINGS                                                                                => To show you the warnings you get
