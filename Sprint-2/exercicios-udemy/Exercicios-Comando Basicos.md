# Exercicio1
## Select
```sql
SELECT email,first_name,last_name 
from sales.customers
```
# Exercicio2
## Distinct
```sql
select distinct brand,model_year
from sales.products
```

# Exercicio3
## Where
```sql
select email, state, birth_date
from sales.customers
where (state ='SC' or state = 'MS') and birth_date <'1993-10-31'
```

# Exercicio4
# Order by
```sql
select * from sales.products
order by price --desc(ordem decrescente)`
select distinct state 
from sales.customers
order by state
```

# Exercicio5
# LIMIT
```sql 
select * from sales.products
order by price desc
limit 10
```

# Desafio
### 1 
```sql
select distinct city,state from sales.customers
where state = 'MG'
order by city
```
### 2
```sql
select visit_id,paid_date from sales.funnel
where paid_date is NOT NULL
order by paid_date desc
limit 10
```
### 3
```sql
select * from sales.customers
where birth_date > '2000-01-01'
order by score desc
limit 10
```