On the postgres container terminal execute the following command to access

```bash
psql -h localhost -U postgres
```

this should give you access to the public schema

view existing databases

```bash
\l
```

List of databases

| Name      | Owner    | Encoding | Collate    | Ctype      | Access privileges |
| --------- | -------- | -------- | ---------- | ---------- | ----------------- |
| Lux       | postgres | UTF8     | en_US.utf8 | en_US.utf8 |                   |
| postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |                   |
| template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres +     |
| template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres +     |

(4 rows)


```bash
CREATE database [database name]
```

IMPORT sql file into the database

```bash
psql -U user_name -d database_name -f file.sql
```

CONNECT to the specific database you imported the sql into

```bash
psql -U username -d database_name
```

```bash
\c [database_name]
```

To get more information on tables, you can use the \dt+ command. It will add the size and description columns

```bash
\dt+
```



List of relations

| Schema | Name                   | Type  |
| ------ | ---------------------- | ----- |
| public | categories             | table |
| public | customer_customer_demo | table |
| public | customer_demographics  | table |
| public | customers              | table |
| public | employee_territories   | table |
| public | employees              | table |
| public | order_details          | table |
| public | orders                 | table |
