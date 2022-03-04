### Overview

- Setup a cloud9 instance on AWS 
- Choose ubunut as OS
- Run `apt-get update` in the terminal
- Run `sudo apt install mysql-server` in the terminal
- Run `sudo systemctl status mysql`in the terminal
- Become root user `sudo su` 
- Run `mysql` to confirm you can access mysql DB

### To run a SQL query in file format 
- Create a file in cloud9 with .sql extenstion
- Login to mysql terminal
- Then you can run `source <file-name>.sql`

### Free PostgresSQL 

- [ElephentSQL](https://www.elephantsql.com/)

### Docker setup 

- Enable docker and make sure docker process is running 

```
docker run --name mysql-training -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<Some-password> -d mysql
```

- Download mysql editor and then connect to mysql editor with details of username and password. It will connect to the docker container 
