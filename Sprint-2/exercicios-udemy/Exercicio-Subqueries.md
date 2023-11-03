# Subqueries
## Where
```sql
select *
from sales.products
where price = (select min(price) from sales.products)
```
## With
```sql
with alguma_tabela as ( 
select
	first_name,professional_status,
	(current_date - birth_date)/365 as idade
from sales.customers
)
select * from alguma_tabela
```
## From
```sql
select 
	professional_status,
	avg(idade) as idade_media
from (
	select
		professional_status,
		(current_date - birth_date)/365 as idade
	from sales.customers
) as alguma_tabela
group by professional_status
```

## Select
```sql
select
	fun.visite_id
	fun.visit_page_date,
	sto.store_name,
	(
		select count(*)
		from sales.funnel as fun2
		where fun2.visit_page_date <= fun.visit_page_date
			and fun2.store_id = fun.store_id
	) as visitas_acumuladas
	from sales.funnel as fun
	left join sale.stores as sto
		on fun.store_id = sto.store_id
	order by sto_store_name , fun.visit_page_date
	`
```
# Desafio
## 1

```sql
WITH numero_visitasdia AS (
    SELECT t1.first_name, COUNT(t2.visit_page_date) AS visit_count
    FROM sales.customers AS t1
    LEFT JOIN sales.funnel AS t2 ON t1.customer_id = t2.customer_id
    GROUP BY t1.first_name
    ORDER BY t1.first_name
)

SELECT first_name, visit_count
FROM numero_visitasdia
ORDER BY visit_count DESC  
``````