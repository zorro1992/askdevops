### Understanding different CRUD operations 

C - CREATE
R - READ
U - UPDATE
D - DELETE

Let's create some tables and insert data (commands from colte steel)

```
CREATE TABLE cats 
  ( 
     cat_id INT NOT NULL AUTO_INCREMENT, 
     name   VARCHAR(100), 
     breed  VARCHAR(100), 
     age    INT, 
     PRIMARY KEY (cat_id) 
  ); 
```

```
INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);
```

### Select command (R)

- select * from cats;
- select name from cats;
- select age from cats;
- select name,age from cats;
- select age,name from cats;

### WHERE command 

- select * from cats where age > 4;
- select * from cats where name = "Misty";
Case-insensitve 
- select * from cats where name = "MISTY";

### Alias with select command

- select cat_id as id from cats;

### Update 

```
update cats set breed = "shorthair" where breed = "Tabby"
```

### Delete 

```
delete from cats where name="Egg"
```
Here you can see that cat_id won't be changed or re-arranged.
