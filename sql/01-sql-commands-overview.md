### SQL Commands overview -- MySQL

Here we are using MySQL which is part of DBMS system

1) DDL -- Data Definition Language
```  
CREATE, ALTER, DROP,TRUNCATE
```  

2) DML -- Data Manipulation Language 
```  
INSERT , UPDATE, DELETE 
```  
3) DCL -- Data Controle Language

4) DRL -- Data Retrival Language
```  
SELECT  
```  

### Databases 

Creating a database
```
create database <name>;
```

Dropping a database
```
drop database <name>;
```

Checking the database we are currently in
```
select database();
```
To use a specifc database (db)
```
use <database name>
```

### Data Types in SQL

For numbers 
- INT
- FLOAT

For string
- VARCHAR(<max length of string>)

### Tables

Normal syntax 

```
CREATE TABLE <table_name>
  (
    column_name data_type,
    column_name data_type
  );
```

Example
  ```
  create table employee (
    emp_id int,
    emp_name varchar(50),
    emp_department varchar(20)
  );
  ```
Drop table
  ```
  drop table <table_name>;
  ```
### Show , Describe table
  ```
  show column from <table_name>;
  ```
  ```
  desc <table_name>
  ```
### Inserting rows to tables
  ```
  insert into employee value (01,"Raghu","Data");
  ```
### Insert multiple rows
  Insert multiple rows to employee table
  ```
    insert into employee 
        value (01,"Raghu","Data"),
              (02,"AJ","Data"),
              (03,"PJ","Data");
  ```

### NULL and NOT NULL

  Create a table with not null options
  ```
  create table department (
    id int NOT NULL,
    dep_name varchar(20),
    dep_location varchar(20)
  );
  ```
  
  Now try to insert but don't add id
  ```
  insert into department(dep_name,dep_location) 
  value ("data","blr");
  ```
  You will get an error 
  `ERROR 1364 (HY000): Field 'id' doesn't have a default value` 
  This is because id column can't be null at any given point of time.
  
  ```
  insert into department(id,dep_name,dep_location) 
  value (01,"data","blr");
  ```
### Setting default value for a table 
  
  Create a table with default value
  ```
  CREATE TABLE products
  (
    name VARCHAR(20) DEFAULT 'random product',
    price INT DEFAULT 99
  );
  ```
  NOT NULL and default can be use together also
  
  Here it doesn't make much sense in the begining why we are using default if column can't be null but the idea is if we need a row with NULL value then the below helps. Read a bit more about it later 
  
  ```
  CREATE TABLE products
  (
    name VARCHAR(20) NOT NULL DEFAULT 'random product',
    price INT NOT NULL DEFAULT 99
  );
 ```
### Primary key and Auto Increment 
  Makes a column unique and can't be null.
  
  Here you can also note we have added auto increment option for our primary key. This is important because it eliminates the need of entering our emp_id everytime.
  ```
   create table employee (
    emp_id int NOT NULL AUTO_INCREMENT,
    emp_name varchar(50),
    emp_department varchar(20),
    primary key (emp_id)
  );
  ```
  Insert details
  ```
      insert into employee (emp_name,emp_department)
        value ("Raghu","Data"),
              ("AJ","Data"),
              ("PJ","Data");
  ```
  
  We can also directly define primary key with the column 
    ```
   create table employee (
    emp_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    emp_name varchar(50),
    emp_department varchar(20)
  );
  ```
  
