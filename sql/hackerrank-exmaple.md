### Good examples of hacker rank code 


```
select city, length(city) from station order by length(city),city asc limit 1;
select city, length(city) from station order by length(city) desc limit 1;
```

Example 1: we are getting students who have score higher than 75 but ordered by last 3 char's in the name and secondary sort by id asc.

```
select name from students where marks > 75 order by right(name,3), id asc;
```

Example 2 : We are trying to get cities whoes name doesn't start with vowels or end with vowels

```
SELECT DISTINCT city FROM station WHERE city RLIKE '^[^aeiouAEIOU].*[^aeiouAEIOU]$';
```
