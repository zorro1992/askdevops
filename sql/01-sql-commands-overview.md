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

