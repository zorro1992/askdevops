### Selection aggregation in SQL (MySQL)

- Distinct
- Order BY
- Like

Insert some new data to books table;

```
INSERT INTO books
    (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);
```
 
 ```
SELECT title FROM books;
```

### Distinct
- Gives `distinct` data and will clear off any duplicate data.
- It will come right after select.

```
select distinct(author_lname) from books;
```

- What if we have 2 columns like author names with same lastname. In this case distinct shall fail right ?
- Below are some examples on how to handle it.

```
SELECT DISTINCT CONCAT(author_fname,' ', author_lname) FROM books;
 
SELECT DISTINCT author_fname, author_lname FROM books;
```

### Order By

- Order by data before displaying
- Order by is also ascending

```
SELECT released_year FROM books ORDER BY released_year;
SELECT released_year FROM books ORDER BY released_year DESC;

SELECT title, author_fname, author_lname 
FROM books ORDER BY 2;
```

```
SELECT author_fname, author_lname FROM books 
ORDER BY author_lname, author_fname;
```
### Limit
- Limit can be used to limit the data that is getting displayed.
- Its helpful in many cases while developing the sql query atleast

```
 
SELECT * FROM books LIMIT 1;

SELECT title, released_year FROM books 
ORDER BY released_year DESC LIMIT 5;

# This is just like adding a random end number so that the limit shows all the data after 95 rows.
SELECT * FROM tbl LIMIT 95,18446744073709551615;
```
### Like

- Like is a simple search option given in SQL where in you can search the data in a column without knowing the complete name
- Let's say "harry" -- from harry potter book
- uses wildcard - %
- If you add %% in between then it will seach the string inside the wildcard
- But if you need something like name starts with ra then you can do ra% meaning the name should start with letter ra but can end with anything.

```
SELECT title, author_fname FROM books WHERE author_fname LIKE '%da%';
 
SELECT title, author_fname FROM books WHERE author_fname LIKE 'da%';
 
SELECT title FROM books WHERE  title LIKE 'the';
 
SELECT title FROM books WHERE  title LIKE '%the';
 
SELECT title FROM books WHERE title LIKE '%the%';
```

- Like also has another wildcard that is "_"
- There _ means that number of char

```
SELECT title, stock_quantity FROM books WHERE stock_quantity LIKE '___
```
