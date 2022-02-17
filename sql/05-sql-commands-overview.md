### Aggregation with SQL

- Count
- Group By
- Min and Max
- Sum
- Avg


### Count function in SQL

- Using count function to get row count etc
- Also using LIKE + COUNT

```
SELECT COUNT(*) FROM books;
SELECT COUNT(author_fname) FROM books;
SELECT COUNT(*) FROM books WHERE title LIKE '%the%';
```

### Group By

- Use to group results works well with count

```
SELECT title, author_lname FROM books GROUP BY author_lname;
SELECT author_fname, author_lname, COUNT(*) FROM books GROUP BY author_lname, author_fname;
```

### Min and Max 

```
SELECT MIN(pages) FROM books;
SELECT MAX(released_year) FROM books;
```

Let's say we need the book with max pages 
```
select title, max(pages) from books;
```
But the above query will fail. Hence we need to also use subquery here.

```
SELECT title, pages FROM books WHERE pages = (SELECT Min(pages) FROM books); 
```

Also we can use 
```
select * from books order by pages desc limit 1;
```

Min and Max with Group by

- If we want to know the first released year of the authors then we can use min() with group by

```
SELECT author_fname, 
       author_lname, 
       Min(released_year) 
FROM   books 
GROUP  BY author_lname, 
          author_fname;
```

```
SELECT
  author_fname,
  author_lname,
  Max(pages)
FROM books
GROUP BY author_lname,
         author_fname;
```

### SUM

- Quick sum of column

```
select sum(pages) from books;
```
- Group by can be used to group the data. 
- A point to note is groupby 1st arg, 2nd arg are important mentions.

```
SELECT author_fname,
       author_lname,
       Sum(released_year)
FROM books
GROUP BY
    author_lname,
    author_fname;
```

### AVG

```
SELECT AVG(stock_quantity) FROM books GROUP BY released_year;
```

