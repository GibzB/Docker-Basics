On the postgres container terminal execute the following command to access

```bash
psql -h localhost -U postgres
```

This should give you access to the public schema

View existing databases

```bash
\l
```

List of databases

| Name      | Owner      | Encoding | Collate    | Ctype                 | Access privileges      |
| --------- | ---------- | -------- | ---------- | --------------------- | ---------------------- |
| postgres  | categories | UTF8     | en_US.utf8 | en_US.utf8            |                        |
| template0 | postgres   | UTF8     | en_US.utf8 | en_US.utf8            | =c/postgres          + |
|           |            |          |            | postgres=CTc/postgres |                        |
| template1 | postgres   | UTF8     | en_US.utf8 | en_US.utf8            | =c/postgres          + |
|           |            |          |            | postgres=CTc/postgres |                        |

(3 rows)

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

To get more information on a specific schema, use the  \dt command. It will list all relations.

```bash
\dt psql_schema.
```

| Schema      | Name                   | Type  | Owner    |
| ----------- | ---------------------- | ----- | -------- |
| psql_schema | categories             | table | postgres |
| psql_schema | customer_customer_demo | table | postgres |
| psql_schema | customer_demographics  | table | postgres |
| psql_schema | customers              | table | postgres |
| psql_schema | employee_territories   | table | postgres |
| psql_schema | employees              | table | postgres |
| psql_schema | order_details          | table | postgres |
| psql_schema | orders                 | table | postgres |
| psql_schema | products               | table | postgres |
| psql_schema | region                 | table | postgres |
| psql_schema | shippers               | table | postgres |
| psql_schema | suppliers              | table | postgres |
| psql_schema | territories            | table | postgres |
| psql_schema | us_states              | table | postgres |

(14 rows)

# Create virtual environment to install DBT

Activate the environment

```
source dbt-env/bin/activate
```

Install dbt

`pip install dbt-postgres`

Initialise dbt


Install Metabase using Docker

* Added metabase service in the `docker-compose` yml
