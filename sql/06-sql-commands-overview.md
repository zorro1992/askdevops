## More about data types

- char and varchar


### Char and Varchar

- Usually used to store text.
- char has a fixed length --> Let's say you need to make sure the coloumn needs to be limited.
  - Using for abbreviation 
- Chart(4) ---> 4 bytes irrespective of how much char you store this is not true with varchar it will only take the space required varchar(4) -> Data is 'ab' then its only 2-3 bytes.

Example :

```
create table dogs (name char(4) breed varchar(10));
insert into dogs (name,breed) values ('bob','beagle');
insert into dogs (name,breed) values ('robby','corgi');
insert into dogs (name,breed) values ('Princess Jane','Retreiver');
```

You will get the warning in with the last insert because `Princess Jane` is more than char(4) length.

### Int, Float, Decimal 
- Here decimal has a special intreset here. When you define decimal you can say DECIMAL(5,2) --> You can insert 999.99 (Total 5 and after decimal 2)

```
CREATE TABLE items(price DECIMAL(5,2));
 
INSERT INTO items(price) VALUES(7);
 
INSERT INTO items(price) VALUES(7987654);
 
INSERT INTO items(price) VALUES(34.88);
 
INSERT INTO items(price) VALUES(298.9999);
 
INSERT INTO items(price) VALUES(1.9999);
 
SELECT * FROM items;
```

### Date Time 

- We have few options here , DATE, TIME, DATETIME

```
CREATE TABLE people (name VARCHAR(100), birthdate DATE, birthtime TIME, birthdt DATETIME);
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Padma', '1983-11-11', '10:07:35', '1983-11-11 10:07:35');
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Larry', '1943-12-25', '04:10:42', '1943-12-25 04:10:42');
 
SELECT * FROM people;
```


