-- CREATE TABLE people(
-- 	first_name VARCHAR(20),
--     last_name VARCHAR(20),
--     age INT
-- );

-- INSERT INTO people(first_name, last_name, age) VALUES ("Tina", "Bleacher", 13);
-- INSERT INTO people(first_name, last_name, age) VALUES ("Bob", "Bleacher", 42);
-- INSERT INTO people(first_name, last_name, age) VALUES ("Mohamed", "Salama", 14), ("Mona", "Ahmed", 22), ("Abeer", "Salama", 33);

-- SELECT * FROM people;
-- DESC people;
-- DROP TABLE people;

-- CREATE TABLE cats2(
-- 	name VARCHAR(50) NOT NULL,
--     age INT NOT NULL
-- );
-- INSERT INTO cats2(name, age) VALUES("Fathy", 4);
-- INSERT INTO cats2(name) VALUES("Mohamed"); 
-- SELECT name, age FROM cats2 
-- DESCRIBE cats;
-- DESCRIBE cats2;

-- CREATE TABLE cats3(
-- 	name VARCHAR(50) NOT NULL DEFAULT "No_Name",
--     age int NOT NULL DEFAULT 100
-- );
-- INSERT INTO cats3() VALUES ();
-- SELECT * FROM cats3;
-- DESC cats3; 

-- CREATE TABLE unique_cats(
-- 	   cat_id INT NOT NULL PRIMARY KEY,
--     name VARCHAR(100),
--     age INT
-- );
-- INSERT INTO unique_cats(cat_id, name, age) VALUES (1, "Floppy", 3);
-- INSERT INTO unique_cats(cat_id, name, age) VALUES (1, "blay", 5);
-- SELECT * FROM unique_cats;

-- CREATE TABLE employees(
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     middle_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100),
--     age INT NOT NULL,
--     current_status VARCHAR(100) NOT NULL DEFAULT "employed"
-- );

-- INSERT INTO employees(first_name, middle_name, last_name, age, current_status)
-- VALUES ("Mohamed", "Salama", "Youssef", 23, "Single");
-- INSERT INTO employees(first_name, middle_name, last_name, age, current_status)
-- VALUES ("Mohamed", "Salama", "Youssef", 23, "Single");
-- INSERT INTO employees(first_name, middle_name, last_name, age, current_status)
-- VALUES ("Mohamed", "Salama", "Youssef", 23, "Single");
-- desc employees; 
-- SELECT * FROM employees;

-- CREATE TABLE cats (
-- 	cat_id INT AUTO_INCREMENT,
--     name VARCHAR(100),
--     breed VARCHAR(100),
--     age INT,
--     PRIMARY KEY(cat_id)
-- );

-- INSERT INTO cats(name, breed, age) 
-- VALUES ('Ringo', 'Tabby', 4),
--        ('Cindy', 'Maine Coon', 10),
--        ('Dumbledore', 'Maine Coon', 11),
--        ('Egg', 'Persian', 4),
--        ('Misty', 'Tabby', 13),
--        ('George Michael', 'Ragdoll', 9),
--        ('Jackson', 'Sphynx', 7);
-- DESC cats;


-- Large Exercise --
-- CREATE DATABASE shirts_db;
-- use shirts_db;
-- CREATE TABLE shirts (
-- 	   shirt_id INT PRIMARY KEY AUTO_INCREMENT,
--     article VARCHAR(10),
--     color VARCHAR(10),
--     shirt_size VARCHAR(2),
--     last_worn INT
-- );

-- INSERT INTO shirts(article, color, shirt_size, last_worn)
--  VALUES ('t-shirt', 'white', 'S', 10),
-- 		('t-shirt', 'green', 'S', 200),
-- 		('polo shirt', 'black', 'M', 10),
-- 		('tank top', 'blue', 'S', 50),
-- 		('t-shirt', 'pink', 'S', 0),
-- 		('polo shirt', 'red', 'M', 5),
-- 		('tank top', 'white', 'S', 200),
-- 		('tank top', 'blue', 'M', 15);

-- INSERT INTO shirts(article, color, shirt_size, last_worn) 
-- VALUES ("Polo Shirt", "Purple", "M", 50);
-- SELECT * FROM shirts;
-- SELECT article, color FROM shirts;
-- SELECT article, color, shirt_size, last_worn FROM shirts WHERE shirt_size="S";
-- UPDATE shirts SET shirt_size="L" WHERE article="polo shirt" or article="Polo Shirt";
-- UPDATE shirts SET last_worn=0 WHERE last_worn=15;
-- UPDATE shirts SET shirt_size="XS", color="off white" WHERE color="white";

-- DELETE FROM shirts WHERE last_worn=200;
-- DELETE FROM shirts WHERE article="tank top";
-- DELETE FROM shirts;
-- DROP TABLE shirts;
-- DROP DATABASE shirts_db;

-- String Functions --
-- CREATE DATABASE book_shop;
-- use book_shop;
-- CREATE TABLE books 
-- 	(
-- 		book_id INT AUTO_INCREMENT,
-- 		title VARCHAR(100),
-- 		author_fname VARCHAR(100),
-- 		author_lname VARCHAR(100),
-- 		released_year INT,
-- 		stock_quantity INT,
-- 		pages INT,
-- 		PRIMARY KEY(book_id)
-- 	);


-- INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
-- VALUES
-- ('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
-- ('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
-- ('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
-- ('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
-- ('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
-- ('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
-- ('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
-- ('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
-- ('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
-- ('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
-- ('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
-- ("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
-- ('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
-- ('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
-- ('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
-- ('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
-- INSERT INTO books
--     (title, author_fname, author_lname, released_year, stock_quantity, pages)
--     VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
--            ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
--            ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);

-- SELECT * FROM books;
-- SELECT CONCAT(author_fname, " ", author_lname) AS full_name FROM books;
-- SELECT CONCAT_WS("$", "Mohamed", "Salama", "Ali", "Youssef");
-- SELECT CONCAT_WS("-", author_fname, author_lname) FROM books;
-- SELECT SUBSTRING("Mohamed Salama", 1, 4) AS ex;
-- SELECT SUBSTRING(author_lname, 1, 1) AS example, author_lname FROM books;
-- SELECT CONCAT(SUBSTR(title, 1, 10), "...") AS ex FROM books;
-- SELECT SUBSTR(author_fname, 1, 1) AS short_name, SUBSTR(author_lname, 1, 1) AS short_name FROM books;
-- SELECT CONCAT(SUBSTR(author_fname, 1, 1), ".", SUBSTR(author_lname, 1, 1)) AS full_name FROM books;
-- SELECT LEFT(author_fname, 1) FROM books;
-- SELECT CONCAT(LEFT(author_fname, 1), ".", LEFT(author_lname, 1)) from books;
-- SELECT REPLACE("Mohamed Salama", " ", " $ ") AS result;
-- SELECT REPLACE(title, " ", "$") FROM books;
-- SELECT REVERSE(123);
-- SELECT REVERSE(NULL);
-- SELECT REVERSE(author_fname) FROM books;
-- SELECT 
--     CONCAT(author_fname, REVERSE(author_fname))
-- FROM
--     books;
-- SELECT CHAR_LENGTH(title), title FROM books;
-- SELECT UPPER("Mohamed");
-- SELECT LOWER("MOHAMED");
-- SELECT CONCAT("I LOVE ", UCASE(title), " !!!") FROM books;
-- SELECT INSERT("Mohamed Salama", 8, 2, "$"); 
-- SELECT TRIM("   Mohamed Salama    ");
-- SELECT TRIM(LEADING "." FROM ".....Mohamed Salama....");
-- SELECT TRIM(TRAILING "." FROM ".....Mohamed Salama....");
-- SELECT TRIM(BOTH "." FROM ".....Mohmamed Salama....");

-- Exercise
-- SELECT REVERSE(UCASE("Why does my cat look at me with such hatred?"));
-- SELECT REPLACE(title, " ", "->") AS title FROM books;
-- SELECT author_lname AS forwards, REVERSE(author_lname) AS backwards FROM books;
-- SELECT UCASE(CONCAT(author_fname, " ", author_lname)) AS full_name_in_caps FROM books;
-- SELECT CONCAT(title, " Was Released In ", released_year) AS blurb FROM books;
-- SELECT title AS title, CHAR_LENGTH(title) AS character_count FROM books; 
-- SELECT * FROM books;
-- SELECT CONCAT(SUBSTR(title, 1, 10), "...") AS short_title,
-- 	   CONCAT(author_lname, ",", author_fname) AS author,
--        CONCAT(stock_quantity, " in stock") AS quantity
--        FROM books;

-- Refinning Selections --
-- SELECT DISTINCT author_fname FROM books;  -- will remove duplicates
-- SELECT DISTINCT CONCAT(author_fname, " ", author_lname) FROM books;
-- SELECT DISTINCT author_fname, author_lname FROM books;
-- SELECT author_fname, author_lname FROM books ORDER BY author_fname ASC;   -- will order the results ( a-z )
-- SELECT author_fname FROM books ORDER BY author_fname DESC;  -- will order the results (z-a)
-- SELECT title, pages FROM books ORDER BY pages DESC;
-- SELECT author_fname, author_lname, pages FROM books ORDER BY 2;
-- SELECT CONCAT(author_fname, " ", author_lname) AS author_full_name FROM books ORDER BY author_full_name ASC;
-- SELECT * FROM books LIMIT 5;
-- SELECT * FROM books LIMIT 0,5;
-- SELECT author_fname, author_lname, released_year FROM books ORDER BY released_year LIMIT 1, 3;  -- first number is where we begin, second number is how much results we want
-- SELECT * FROM books ORDER BY released_year DESC LIMIT 3;
-- SELECT author_fname FROM books WHERE author_fname LIKE "%da%";
-- SELECT author_fname FROM books WHERE author_fname LIKE "%";
-- SELECT author_fname FROM books WHERE author_fname LIKE "_____";
-- SELECT author_fname FROM books WHERE author_fname LIKE "%n";
-- SELECT title FROM books WHERE title LIKE "%\%%";
-- SELECT title FROM books WHERE title LIKE "%\_%";

-- Exercise Refinning Selections --
-- SELECT title FROM books WHERE title like "%stories%";
-- SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;
-- SELECT CONCAT(title, " - ", released_year) AS summary FROM books ORDER BY released_year DESC LIMIT 3;
-- SELECT title author_lname FROM books WHERE author_lname LIKE "% %";
-- SELECT title, released_year, stock_quantity FROM books ORDER BY 3 LIMIT 3;
-- SELECT title, author_lname FROM books ORDER BY 2, 1;
-- SELECT UCASE(CONCAT("My Favourite Author Is ", author_fname, " ", author_lname)) AS yell FROM books ORDER BY yell DESC;


-- Aggregate Functions --
-- SELECT count(author_fname) FROM books;
-- SELECT COUNT(DISTINCT author_fname) FROM books;
-- SELECT COUNT(title) AS title FROM books WHERE title LIKE "%the%";

-- SELECT author_fname, COUNT(author_fname) FROM books GROUP BY author_fname;
-- SELECT COUNT(DISTINCT author_fname) FROM books GROUP BY author_fname;
-- SELECT * FROM books GROUP BY author_lname; -- Will raise an error

-- SELECT COUNT(released_year), MIN(released_year) FROM books;
-- SELECT MAX(pages) FROM books;
-- SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1; -- find the title of the longest books
-- SELECT title, pages FROM books WHERE pages=(SELECT MAX(pages) FROM books); -- find the title of the longest books
-- SELECT MIN(released_year) FROM books; -- find the title of the book that was released earliest
-- SELECT title, released_year FROM books ORDER BY released_year ASC LIMIT 1; -- find the title of the book that was released earliest
-- SELECT title, released_year FROM books WHERE released_year=(SELECT MIN(released_year) FROM books); -- find the title of the book that was released earliest

-- SELECT author_fname, author_lname, COUNT(*) FROM books GROUP BY author_fname, author_lname;
-- SELECT author_lname, MIN(released_year), MAX(released_year) FROM books GROUP BY author_lname; 

-- SELECT SUM(pages) FROM books;
-- SELECT author_fname, SUM(pages) FROM books GROUP BY author_fname;
-- SELECT author_fname, COUNT(*), SUM(released_year) FROM books GROUP BY author_fname;

-- SELECT AVG(pages), AVG(released_year) FROM books;
-- SELECT released_year, AVG(stock_quantity), COUNT(*) FROM books GROUP BY released_year;

-- -- Exercise --
-- SELECT COUNT(*) FROM books;
-- SELECT released_year, COUNT(*) FROM books GROUP BY released_year;
-- SELECT SUM(stock_quantity) FROM books;
-- SELECT CONCAT(author_fname, " ", author_lname) AS full_name, AVG(released_year) FROM books GROUP BY full_name;
-- SELECT CONCAT(author_fname, " ", author_lname) AS full_name, pages FROM books WHERE pages=(SELECT MAX(pages) FROM books);
-- SELECT CONCAT(author_fname, " ", author_lname) AS full_name, pages FROM books ORDER BY pages DESC LIMIT 1;
-- SELECT released_year AS year, COUNT(*) AS "# books", AVG(pages) AS "avg pages" FROM books GROUP BY released_year ORDER BY released_year;

-- Data Types
-- CREATE TABLE parents (
-- 	childrens_num TINYINT UNSIGNED
-- );
-- INSERT INTO parents(childrens_num) VALUES (-10);

-- SELECT * FROM parents;
-- CREATE TABLE Example(
-- 	num DECIMAL(5,2)
-- );

-- INSERT INTO Example VALUES (25.365);
-- SELECT * FROM Example;

-- CREATE TABLE people (
-- name VARCHAR(50),
-- the_date DATE,
-- the_time TIME,
-- the_datetime DATETIME
-- );
-- INSERT INTO people (name, the_date, the_time, the_datetime) VALUES ("Mohamed", "2000-8-7", "12:10:22", "2000-8-7 12:10:22");
-- INSERT INTO people (name, the_date, the_time, the_datetime) VALUES ("baby", CURDATE(), CURTIME(), NOW());

-- SELECT * FROM people;
-- SELECT CURDATE();
-- SELECT CURTIME();
-- SELECT NOW();

-- SELECT the_date, DATE_FORMAT(the_date, "Born on: %a %b %D") FROM people;
-- SELECT the_date, DATEDIFF(CURDATE(), the_date) FROM people; /* this is my table */
-- SELECT the_date, YEAR(the_date + INTERVAL 10 year) AS year FROM people;

-- CREATE TABLE insta_cap (
-- 	text VARCHAR(300),
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );
-- INSERT INTO insta_cap (text) VALUES ("Hi this is me mohamed salama");
-- UPDATE insta_cap SET text="Hi this is me mohamed salama after being updated";
-- SELECT * FROM insta_cap;

-- Exercises
-- SELECT CURTIME();  -- to print out the current time
-- SELECT CURDATE();  -- to print out the current date
-- SELECT DAYOFWEEK(CURDATE());  -- print out the day of the week as a number
-- SELECT DAYNAME(NOW());  -- print out the current day of the week as a day name
-- SELECT DAYNAME(CURDATE());  -- print out the current day of the week as a day name
-- SELECT DAYNAME(CURTIME());  -- print out the current day of the week as a day name
-- SELECT DATE_FORMAT(NOW(), "%W");  -- print out the current day of the week as a day name
-- SELECT DATE_FORMAT(CURDATE(), "%m/%d%/%Y")  -- print out the current date with this format mm/dd/yy

-- Logical Operators
-- SELECT * FROM books WHERE released_year=2017;
-- SELECT * FROM books WHERE released_year!=2017;
-- SELECT * FROM books WHERE author_lname!="Gaiman";

-- SELECT * FROM books WHERE title LIKE "% %";
-- SELECT title FROM books WHERE title NOT LIKE "% %";
-- SELECT title, author_fname, author_lname FROM books WHERE author_fname NOT LIKE "Da%";

-- SELECT 1 > 1;
-- SELECT title, released_year FROM books WHERE released_year > 2015;
-- SELECT title, pages FROM books WHERE pages > 500;

-- SELECT title, released_year FROM books WHERE released_year < 2000 ORDER By 2 ASC;
-- SELECT title, pages FROM books WHERE pages < 200;

-- SELECT title, released_year FROM books WHERE released_year >= 2000 ORDER BY 2 ASC;

-- SELECT title, released_year FROM books WHERE released_year <= 2000 ORDER BY 2 ;

-- SELECT title, author_lname, released_year FROM books WHERE author_lname="Eggers" AND released_year > 2010;
-- SELECT title, author_lname FROM books WHERE author_lname="Eggers" AND released_year > 2010 AND title LIKE "%novel%";
-- SELECT title, author_lname, pages FROM books WHERE CHAR_LENGTH(title) > 30 AND pages > 635;

-- SELECT title, author_lname, pages FROM books WHERE author_lname = "Eggers" OR released_year > 2010;

-- SELECT title, released_year FROM books WHERE released_year BETWEEN 2010 AND 2015;
-- SELECT title, pages FROM books WHERE pages BETWEEN 200 AND 300 ORDER BY pages;
-- SELECT title, pages FROM books WHERE pages NOT BETWEEN 200 AND 300 ORDER BY pages;

-- SELECT * FROM people WHERE the_date < "2023-01-01";  # the date here is a string but SQL cna recognize it as a date
-- SELECT * FROM people WHERE YEAR(the_date) < 2023;

-- SELECT * FROM people WHERE the_time BETWEEN "12:00:00" AND "18:00:00";
-- SELECT * FROM people WHERE the_time BETWEEN CAST("12:00:00" AS TIME) AND CAST("18:00:00" AS TIME);
-- SELECT * FROM people WHERE HOUR(the_time) BETWEEN 12 AND 18;

-- SELECT title, author_lname FROM books WHERE author_lname IN ("Carver", "Lahiri", "Smith");
-- SELECT title, author_lname FROM books WHERE author_lname NOT IN ("Carver", "Lahiri", "Smith");
-- SELECT title, released_year FROM books WHERE released_year >= 2000 AND released_year NOT IN (2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016) ORDER BY 2;
-- SELECT title, released_year FROM books WHERE released_year >= 2000 AND released_year % 2 != 0;

-- SELECT title, released_year,
-- 	CASE 
-- 		WHEN released_year >= 2000 THEN "Modern Book"
-- 		ELSE "Old Book"
-- 	END AS book_age
-- FROM books ORDER BY released_year;

-- SELECT title, stock_quantity,
-- 	CASE
-- 		WHEN stock_quantity BETWEEN 0 AND 50 THEN "*"
-- 		WHEN stock_quantity <= 100 THEN "**"
-- 		ELSE "***"
-- 	END AS Stock
-- FROM books ORDER BY stock_quantity LIMIT 17;

-- SELECT author_lname FROM books WHERE author_lname IS NULL;
-- SELECT author_lname FROM books WHERE 1 IS NOT NULL;
-- DELETE FROM books WHERE author_lname IS NULL; 

########### Exercise ###########
-- SELECT title, released_year FROM books WHERE released_year < 1980;
-- SELECT title, author_lname FROM books WHERE author_lname="Eggers" OR author_lname="Chabon";
-- SELECT title, author_lname, released_year FROM books WHERE author_lname="Lahiri" AND released_year > 2000;
-- SELECT title, pages FROM books WHERE pages BETWEEN 100 AND 200 ORDER BY pages;
-- SELECT title, author_lname FROM books WHERE author_lname LIKE "C%" OR "S%";

-- SELECT title, author_lname, 
-- 	CASE 
-- 		WHEN title LIKE "%stories%" THEN "Short Stories"
--         WHEN title LIKE "Just Kids" OR title LIKE "%A Heartbreaking Work%" THEN "Memoir"
-- 		ELSE "Novel"
-- 	END AS TYPE
-- FROM books;

-- SELECT author_fname, author_lname,
-- 	CASE
--  		WHEN COUNT(*) = 1 THEN "1 book"
--  		ELSE CONCAT(COUNT(*), " books")
--  	END AS Count
-- FROM books GROUP BY author_fname, author_lname;

-- SELECT author_fname, author_lname,
-- 	IF(COUNT(*) > 1, CONCAT(COUNT(*), " Books"), "1 Book") AS "Count"
-- FROM books
-- GROUP BY author_fname, author_lname;


-- Constraints & ALTER TABLE
-- CREATE TABLE contacts (
-- 	name VARCHAR(50) NOT NULL, 
--     phone CHAR(11) UNIQUE CHECK (CHAR_LENGTH(phone) = 11)
-- );
-- INSERT INTO contacts (name, phone) VALUES ("Mohamed", "01012342353");
-- INSERT INTO contacts (name, phone) VALUES ("Mona", "12342353");
-- SELECT * FROM contacts;

-- CREATE TABLE palindromes (  # palindromes means that the word equal it's reverse
-- 	word VARCHAR(50) CHECK (REVERSE(word) = word)
-- );
-- INSERT INTO palindromes (word) VALUES ("racecar");
-- SELECT * FROM palindromes;

-- CREATE TABLE users (
-- 	name VARCHAR(50), 
--     age INT,
--     CONSTRAINT age_over_18 CHECK (age > 18)
-- );
-- INSERT INTO users (name, age) VALUES ("Mohamed", 18);
-- SELECT * FROM users;

-- CREATE TABLE companies (
-- 	name VARCHAR(150) NOT NULL, 
--     address VARCHAR(250) NOT NULL,
--     CONSTRAINT name_address UNIQUE (name, address)   # this will check if the name and address are the same and will prevent duplicates with nama and address together
-- );
-- iNSERT INTO companies (name, address) VALUES ("The Wolf Of Wall Street", "San Fransisco In America");
-- iNSERT INTO companies (name, address) VALUES ("The Wolf Of Wall Street", "San Fransisco In America");


# ALTER TABLE 
-- ALTER TABLE companies
-- ADD COLUMN employee_count INT NOT NULL DEFAULT 1;
-- SELECT * FROM companies;

-- ALTER TABLE companies
-- DROP COLUMN employee_count;
-- DESC companies;

-- RENAME TABLE companies TO suppliers;
-- DESC suppliers;
-- ALTER TABLE suppliers RENAME companies;
-- DESC companies;

-- ALTER TABLE companies
-- RENAME COLUMN name TO the_name;
-- DESC companies;

-- ALTER TABLE companies
-- MODIFY the_name VARCHAR(250) DEFAULT "unknown";
-- DESC companies;


############ Relationships And Joins ############ 
-- CREATE DATABASE shop;
-- USE shop;

-- CREATE TABLE customers (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     email VARCHAR(50)
-- );

-- CREATE TABLE orders (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     order_date DATE,
--     amount DECIMAL(8,2),
--     customer_id INT,
--     FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE  -- on delete cascade means that if you delete a customer it will also delete every data related with it in another database
-- );

-- INSERT INTO customers (first_name, last_name, email) 
-- VALUES ('Boy', 'George', 'george@gmail.com'),
--        ('George', 'Michael', 'gm@gmail.com'),
--        ('David', 'Bowie', 'david@gmail.com'),
--        ('Blue', 'Steele', 'blue@gmail.com'),
--        ('Bette', 'Davis', 'bette@aol.com');
--        
--        
-- INSERT INTO orders (order_date, amount, customer_id)
-- VALUES ('2016-02-10', 99.99, 1),
--        ('2017-11-11', 35.50, 1),
--        ('2014-12-12', 800.67, 2),
--        ('2015-01-03', 12.50, 2),
--        ('1999-04-11', 450.25, 5);

-- SELECT id FROM customers WHERE last_name="George" AND first_name="Boy";
-- SELECT * FROM orders WHERE customer_id=1;
-- SELECT * FROM orders WHERE customer_id = (SELECT id FROM customers WHERE last_name="George" AND first_name="Boy");  # with subqueries

-- SELECT * FROM customers, orders; # this is called cross join and it will join customer and orders databases together

-- ## joins ##
-- -- NOTE:- you can use WHERE CLUSE instead of ON
-- -- INNER JOIN == JOIN
-- SELECT * FROM customers                                                      # to know the orders of every customer 
-- JOIN orders ON orders.customer_id = customers.id;

-- SELECT first_name, last_name, order_date, amount FROM customers              # to know the orders of every customer 
-- JOIN orders WHERE orders.customer_id = customers.id;

-- SELECT * FROM orders                                                         # to know the orders of every customer 
-- JOIN customers WHERE customers.id = orders.customer_id;

-- SELECT first_name, last_name, SUM(amount) AS total FROM customers            # to know the total amount of every customer
-- JOIN orders ON customers.id = orders.customer_id
-- GROUP BY first_name, last_name
-- ORDER BY total;

-- -- LEFT JOIN
-- # Note:- if there's no matches it will represents as NULL
-- SELECT * FROM customers
-- LEFT JOIN orders ON customers.id = orders.customer_id;

-- SELECT first_name, last_name, IFNULL(SUM(amount), 0) FROM customers          # to know the total amount of every customer and put 0 if there's NULL
-- LEFT JOIN orders ON customers.id = orders.customer_id
-- GROUP BY first_name, last_name;

-- Exercises
-- CREATE DATABASE university;
-- USE university;

-- CREATE TABLE students (
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
--     first_name VARCHAR(100)
-- );

-- CREATE TABLE papers (
-- 	student_id INT,
-- 	title VARCHAR(150),
--     grade VARCHAR(150),
--     FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
-- );

-- INSERT INTO students (first_name) VALUES 
-- ('Caleb'), ('Samantha'), ('Raj'), ('Carlos'), ('Lisa');

-- INSERT INTO papers (student_id, title, grade) VALUES
-- (1, 'My First Book Report', 60),
-- (1, 'My Second Book Report', 75),
-- (2, 'Russian Lit Through The Ages', 94),
-- (2, 'De Montaigne and The Art of The Essay', 98),
-- (4, 'Borges and Magical Realism', 89);

-- SELECT first_name, title, grade FROM students 
-- JOIN papers ON students.id = papers.student_id ORDER BY grade DESC;

-- SELECT first_name, title, grade FROM students
-- LEFT JOIN papers ON papers.student_id = students.id;

-- SELECT first_name, IFNULL(title, "MISSING"), IFNULL(grade, 0) FROM students
-- LEFT JOIN papers ON students.id = papers.student_id ORDER BY grade DESC;

-- SELECT first_name, IFNULL(AVG(grade), 0) AS average FROM students
-- LEFT JOIN papers ON students.id = papers.student_id
-- GROUP BY first_name
-- ORDER BY average DESC;

-- SELECT first_name,
-- 	   IFNULL(AVG(grade), 0) AS average,
--        CASE
-- 			WHEN IFNULL(AVG(grade), 0) >= 75 THEN "Passed"
--             ELSE "Failed"
--        END AS passing_status
-- FROM students 
-- LEFT JOIN papers ON students.id = papers.student_id
-- GROUP BY first_name
-- ORDER BY average DESC;


-- ######## Many To Many Relationship ########
-- CREATE DATABASE TV_Shows;
-- USE TV_Shows;

-- CREATE TABLE reviewers (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE series (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     title VARCHAR(100),
--     released_year YEAR,
--     genre VARCHAR(100)
-- );

-- CREATE TABLE reviews (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     rating DECIMAL(2, 1),
--     series_id INT,
--     reviewer_id INT,
--     FOREIGN KEY (series_id) REFERENCES series(id),
--     FOREIGN KEY (reviewer_id) REFERENCES reviewers(id)
-- );

-- INSERT INTO series (title, released_year, genre) VALUES
--     ('Archer', 2009, 'Animation'),
--     ('Arrested Development', 2003, 'Comedy'),
--     ("Bob's Burgers", 2011, 'Animation'),
--     ('Bojack Horseman', 2014, 'Animation'),
--     ("Breaking Bad", 2008, 'Drama'),
--     ('Curb Your Enthusiasm', 2000, 'Comedy'),
--     ("Fargo", 2014, 'Drama'),
--     ('Freaks and Geeks', 1999, 'Comedy'),
--     ('General Hospital', 1963, 'Drama'),
--     ('Halt and Catch Fire', 2014, 'Drama'),
--     ('Malcolm In The Middle', 2000, 'Comedy'),
--     ('Pushing Daisies', 2007, 'Comedy'),
--     ('Seinfeld', 1989, 'Comedy'),
--     ('Stranger Things', 2016, 'Drama');
--  
--  
-- INSERT INTO reviewers (first_name, last_name) VALUES
--     ('Thomas', 'Stoneman'),
--     ('Wyatt', 'Skaggs'),
--     ('Kimbra', 'Masters'),
--     ('Domingo', 'Cortes'),
--     ('Colt', 'Steele'),
--     ('Pinkie', 'Petit'),
--     ('Marlon', 'Crafford');
--     
--  
-- INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
--     (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
--     (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
--     (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
--     (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
--     (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
--     (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
--     (7,2,9.1),(7,5,9.7),
--     (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
--     (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
--     (10,5,9.9),
--     (13,3,8.0),(13,4,7.2),
--     (14,2,8.5),(14,3,8.9),(14,4,8.9);

-- SELECT title, rating FROM series
-- JOIN reviews ON series.id = reviews.series_id;

-- SELECT title, AVG(rating) AS avg_rating FROM series
-- INNER JOIN reviews ON series.id = reviews.series_id
-- GROUP BY title
-- ORDER BY avg_rating;

-- SELECT first_name, last_name, rating FROM reviewers
-- JOIN reviews ON reviewers.id = reviews.reviewer_id;

-- SELECT title AS Un_Reviewed_Series FROM series
-- LEFT JOIN reviews ON series.id =  reviews.series_id
-- WHERE rating IS NULL;

-- SELECT genre, ROUND(AVG(rating), 2) AS avg_rating FROM series
-- JOIN reviews ON series.id = reviews.series_id
-- GROUP BY genre;

-- SELECT first_name,
-- 	   last_name, 
--        COUNT(rating) AS COUNT, 
--        IFNULL(MIN(rating), 0) AS MIN_RATING, 
--        IFNULL(MAX(rating), 0) AS MAX_RATING,
--        IFNULL(ROUND(AVG(rating), 2), 0) AS average,
--        IF (COUNT(rating) > 0, "ACTIVE", "NOT ACTIVE")
-- FROM reviewers
-- LEFT JOIN reviews ON reviewers.id = reviews.reviewer_id
-- GROUP BY first_name, last_name;

-- SELECT title, rating, CONCAT(first_name, " ", last_name) AS reviewer
-- FROM reviewers
-- INNER JOIN reviews ON reviewers.id = reviews.reviewer_id
-- INNER JOIN series ON reviews.series_id = series.id;


######## VIEWS ########
-- CREATE VIEW full_review AS
-- SELECT title, released_year, genre, rating, first_name, last_name
-- FROM reviews
-- JOIN series ON series.id = reviews.series_id
-- JOIN reviewers ON reviewers.id = reviews.reviewer_id;

-- # update the view name 
-- CREATE VIEW full_reviews AS SELECT * FROM full_review;
-- SELECT * FROM full_reviews;

-- show tables;
-- SELECT * FROM full_review;

-- ## HAVING CLAUSE ##
-- SELECT title,
-- 	   AVG(rating),
--        COUNT(rating) AS review_count
-- FROM full_review
-- GROUP BY title HAVING COUNT(rating) > 1;

-- ## ROLLUP ##
-- SELECT title, COUNT(rating) FROM full_reviews GROUP BY title WITH ROLLUP;  # WITH ROLLUP it will gives you the summary of the count aggregate function

-- SELECT released_year, genre, AVG(rating)
-- FROM full_reviews
-- GROUP BY released_year, genre WITH ROLLUP;


## Modes in MySQL ##
-- SELECT @@GLOBAL.sql_mode;
-- SELECT @@SESSION.sql_mode;

-- SET SESSION sql_mode = "ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ENGINE_SUBSTITUTION";  # this will remove the warning of zero division
-- SELECT 2 / 0;
-- SHOW WARNINGS;


##### Window Functions #####
-- CREATE TABLE employees (
--     emp_no INT PRIMARY KEY AUTO_INCREMENT,
--     department VARCHAR(20),
--     salary INT
-- );

-- INSERT INTO employees (department, salary) VALUES
-- ('engineering', 80000),
-- ('engineering', 69000),
-- ('engineering', 70000),
-- ('engineering', 103000),
-- ('engineering', 67000),
-- ('engineering', 89000),
-- ('engineering', 91000),
-- ('sales', 59000),
-- ('sales', 70000),
-- ('sales', 159000),
-- ('sales', 72000),
-- ('sales', 60000),
-- ('sales', 61000),
-- ('sales', 61000),
-- ('customer service', 38000),
-- ('customer service', 45000),
-- ('customer service', 61000),
-- ('customer service', 40000),
-- ('customer service', 31000),
-- ('customer service', 56000),
-- ('customer service', 55000);

-- SELECT department, AVG(salary) FROM employees GROUP BY department;

-- SELECT department, salary, AVG(salary) OVER() FROM employees; # will give you the average of every single row from the table
-- SELECT department, salary, MIN(salary) OVER(), MAX(salary) OVER() FROM employees;
-- SELECT department, salary, AVG(salary) OVER(PARTiTION BY department) AS dept_AVG, AVG(salary) OVER() AS comp_AVG FROM employees;

-- SELECT department, salary, SUM(salary) OVER (PARTITION BY department ORDER BY salary) FROM employees;

-- SELECT emp_no, 
-- 	   department, 
-- 	   salary, 
--        RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dept_salary_rank,
--        RANK() OVER(ORDER BY salary DESC) AS overall_salary_rank
-- FROM employees ORDER BY department;


######### INSTAGRAM Clone #########
CREATE DATABASE instagram;
use instagram;
CREATE TABLE users (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() # we used timestamp because it's easirer to store
);
DESC users;

CREATE TABLE photos (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(user_id) REFERENCES users(id)
);
SHOW TABLES;




























