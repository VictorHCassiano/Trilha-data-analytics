# Exercicio1
## Left Join
```sql
select t1.cpf, t1.name , t2.state
from temp_tables.tabela_1 as t1 left join temp_tables.tabela_2 as t2
on t1.cpf=t2.cpf
```

## Right join
```sql
select t1.cpf, t1.name , t2.state
from temp_tables.tabela_1 as t1 left join temp_tables.tabela_2 as t2
on t1.cpf=t2.cpf
```

## Full join
```sql
select t1.cpf, t1.name , t2.state
from temp_tables.tabela_1 as t1 full join temp_tables.tabela_2 as t2
on t1.cpf=t2.cpf
```

# Desafio

## 1
```sql
select brand, count(visit_page_date) as quant_visitas
from sales.funnel as t1 left join sales.products as t2
on t1.product_id = t2.product_id
group by brand
order by quant_visitas desc
```
## 2
```sql
select store_name, count(visit_page_date) as quant_visitas
from sales.funnel as t1 left join sales.stores as t2
on t1.store_id = t2.store_id
group by store_name
order by quant_visitas desc
```
## 3
```sql
select
	reg.size,
	count(*) as contagem
from sales.customers as cus
left join temp_tables.regions as reg
	on lower(cus.city) = lower(reg.city)
	and lower(cus.state) = lower(reg.state)
group by reg.size
order by contagem
```