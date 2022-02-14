### Overview

#### Load the data for some action

- create table 
```
CREATE TABLE books 
	(
		book_id INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);
```
- Insert data into table

```
INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
```


### Concat in SQL

Syntax : 

- concat(x,y,z)
- concat(column,anothercolumn)
- Adding a space in concat
- concat(author_fname, '', author_lname)

```
select concat(author_fname, ' ', author_lname) from books;
```
- Use alias
```
select concat(author_fname, ' ', author_lname) as full_name from books;
```

Using concat_ws
- When using concat_ws you can pass the seperator as the first argument.
```
select concat_ws(' ' , author_fname,author_lname) as full_name from books;
```

### SUBSTRING

Short form **substr**

Example
- Here 1,4 are index and in SQL index starts from 1 
```
select substring('Hello World',1,4);
select substring('Hello World',4);
select substring('Hello World',-4);
```

What is the string is --- Where I'm Calling From: Selected Stories , Here you can see we have ' in the string so this can break

To overcome this we can use "" 
```
select substring("Where I'm Calling From: Selected Storie",1,5);
```
```
select substring(title,1,10) as short_title from books;
```

Mixing substring and concat

```
select concat(substring(title,1,10), '...') as short_title from books;
```

### Replace

- Replace parts of string 
- It is case senstive
- Example
```
select replace('hello world', 'hell', '$%$#$');
select replace('hello world', 'l', '7');
select replace('hello world', 'o', 'O');
select replace('hellO world', 'o', 'O'); --- Case senstive example
```
In the example below you can see I have replacing all letter 'e' in title with number 3
```
select replace(title,'e',3) from books;
```
Combining substring and replace.
```
select substring(replace(title,'e',3),1,6) from books;
```

### Reverse
To reverse the data in a column
```
select reverse(author_fname) from books;
```

### CHAR_LENGTH
```
SELECT CHAR_LENGTH('Hello World');
# CHAR_LENGTH with concat.
SELECT CONCAT(author_lname, ' is ', CHAR_LENGTH(author_lname), ' characters long') FROM books;
```
