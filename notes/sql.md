# sql-rep

# EXPLAIN SELECT изучить

nosql распределенные бд , быстрый доступ

Включить логирование запросов:
```sql
SET GLOBAL log_output = 'TABLE';
SET GLOBAL general_log = 'ON';
-- Дальше смотрим : mysql.general_log
```

```sql
SHOW WARNINGS;
select user(),version(),database();
```

```sql
CREATE VIEW my_view 
AS 
  SELECT id_video, 
         alias, 
         dataset_size_x, 
         dataset_size_y 
  FROM   videos; 
```


```sql
SET @a:=556 , @b:=404;
SELECT * 
FROM my_view 
WHERE dataset_size_x IN (@a , @b);
```

```sql

SELECT NOW(); -- date and time
SELECT VERSION() ; -- version
```


```sql
SELECT *,
       CASE
           WHEN substr(dataset_size_x, 1, 1) = '1' THEN 'Fiest'
           WHEN substr(dataset_size_x, 1, 1) = '2' THEN 'Second'
           ELSE 'Other'
       END ddd
FROM my_view;
```

SELECT *,
       CASE
           WHEN BEGIN = 1 THEN 'a' ELSE 'b' END AS CLASS
FROM my_view ;


SELECT City
FROM Station
WHERE City REGEXP '^[aeiou]' and City REGEXP '[aeiou]$';

Если мы включим статистику (SET STATISTICS IO ON), то заметим, что SQL Server считывает 46767 страниц из некластеризованного индекса.
SET STATISTICS IO ON
SET STATISTICS TIME ON

SELECT DISTINCT CITY FROM STATION WHERE (ID % 2) = 0;

Оконные функции

SELECT CONCAT(name, "\(", SUBSTR(occupation,1,1) , "\)" ) from occupations

```sql
SELECT ID, 
 Amount, 
 SUM(Amount) OVER(PARTITION BY ID) AS SUM FROM ForWindowFunc
```

```python

# BASE
SHOW TABLES;
SHOW DATABASES;
USE <DB_NAME>
DESC <TABLE_NAME>
EXPLAIN <TABLE_NAME>
DESCRIBE <TABLE_NAME> # KEYS
SHOW CREATE TABLE <TABLE_NAME> # Запрос на создание этой таблицы


import pymysql
import pandas as pd

DB_HOST = '89.223.95.235'
DB_USER = 'student_0'
DB_USER_PASSWORD = 'student_0'
DB_NAME = 'sample_db'

# NULL ~ можно интерпретировать как "неизвестно"/"отсутствует"/"неопределенность", но никак не как 0
# NULL = NULL -> False
# Нельзя сравнивать столбец с NULL. Т.е. нельзя писать такое: phone_number != NULL или credit_limit = NULL.
# Надо так: credit_limit IS NULL/ credit_limit IS NOT NULL.

conn = pymysql.connect(DB_HOST, DB_USER, DB_USER_PASSWORD, DB_NAME)
pd.read_sql_query("select * from customer", conn)

# DISTINCT - уникальные значения
pd.read_sql_query("SELECT DISTINCT location_id FROM department", conn)
# Вывод арифмитических действий
pd.read_sql_query("SELECT employee_id, commission/salary*100 as 'percent' FROM employee", conn)

# SUBSTR - взять подстроку ; CONCAT - объеденить в одну строку
pd.read_sql_query(
    """
    SELECT
      CONCAT(SUBSTR(first_name, 1, 1), '.') as I1,
      CONCAT(middle_initial, '.') as I2,
      last_name
    FROM
      employee
""", conn)

# ROUND() человеческое округление
# CEIL() округление вверх
# FLOOR() округление вниз
pd.read_sql_query("""
  SELECT
    total,
    ROUND(total),
    CEIL(total),
    FLOOR(total)
  FROM
    sales_order
""",conn)

# логическое сравнение
pd.read_sql_query("""
  SELECT last_name, 
       commission, 
       salary 
FROM   employee 
WHERE  commission > salary 
""",conn)

# где подстрока 
pd.read_sql_query("""
    SELECT
      last_name
    FROM
      employee
    WHERE SUBSTR(last_name, 1, 1) = 's'
""",conn)

pd.read_sql_query("""
  SELECT
    CONCAT( first_name , ' ' , last_name),
    FLOOR(DATEDIFF(CURDATE(), hire_date)/365)
  FROM employee
 """, conn) 
 
 pd.read_sql_query("""
  SELECT
    last_name,
    job_id
  FROM 
    employee
  WHERE 
    #job_id=670 or job_id=677
    job_id in (677,670)
 """, conn) 
 
#регулярные выражения LIKE %all% or LIKE _ll ; % ноль или любое количество символов , _ ровно один символ.

pd.read_sql_query("""

SELECT 
employee.employee_id as 'Табельный Номер',
last_name as Фамилия,
regional_group as Город,
function as Должность
FROM employee 
     INNER JOIN 
     job
     INNER JOIN 
     department
     INNER JOIN
     location
     ON employee.job_id = job.job_id
     AND employee.department_id = department.department_id
     AND department.location_id = location.location_id
""",conn)

pd.read_sql_query("""
    SELECT
          customer.customer_id,
          customer.name,
          employee.last_name
    FROM
        customer
        INNER JOIN
        employee
        ON customer.salesperson_id = employee.employee_id
    WHERE
      last_name='turner'

""",conn)


```


