# Exercicio 1
## Conversao de unidades

```sql
select '2021-10-01'::date - '2021-02-01'::date

select '200'::numeric - '100'::numeric

select cast('2021-10-01' as date) - cast('2021-02-01'as date)

```

## Tratamento geral
```sql
with faixa_de_renda as (
	select
		income,
		case
			when income < 5000 then '0-5000'
			when income >= 5000 and income < 10000 then '5000-10000'
			when income >= 10000 and income < 15000 then '10000-15000'
			else '15000+'
			end as faixa_renda
	from sales.customers
)

select faixa_renda, count(*)
from faixa_de_renda
group by faixa_renda
```
```sql
select
	*,
	case
		when population is not null then population
		else (select avg(population) from temp_tables.regions)
		end as populacao_ajustada

from temp_tables.regions

```

```sql
select
	*,
	coalesce(population, (select avg(population) from temp_tables.regions)) as populacao_ajustada
	
from temp_tables.regions
```

## Tratamento de texto
```sql
select 'São Paulo' = 'SÃO PAULO'
select upper('São Paulo') = 'SÃO PAULO'


select 'São Paulo' = 'são paulo'
select lower('São Paulo') = 'são paulo'


select 'SÃO PAULO     ' = 'SÃO PAULO'
select trim('SÃO PAULO     ') = 'SÃO PAULO'


select 'SAO PAULO' = 'SÃO PAULO'
select replace('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'
```

## Tratamento de data
```sql
select current_date + 10
select (current_date + interval '10 weeks')::date
select (current_date + interval '10 months')::date
select current_date + interval '10 hours'
```

```sql
select visit_page_date, count(*)
from sales.funnel
group by visit_page_date
order by visit_page_date desc
```

```sql
select
	date_trunc('month', visit_page_date)::date as visit_page_month,
	count(*)
from sales.funnel
group by visit_page_month
order by visit_page_month desc
```

```sql
select
	extract('dow' from visit_page_date) as dia_da_semana,
	count(*)
from sales.funnel
group by dia_da_semana
order by dia_da_semana
```

```sql
select (current_date - '2018-06-01')
select (current_date - '2018-06-01')/7
select (current_date - '2018-06-01')/30
select (current_date - '2018-06-01')/365

select datediff('weeks', '2018-06-01', current_date)
```

## Funcoes
```sql
select (current_date - '2018-06-01')
select (current_date - '2018-06-01')/7
select (current_date - '2018-06-01')/30
select (current_date - '2018-06-01')/365

select datediff('weeks', '2018-06-01', current_date)

create function datediff(unidade varchar, data_inicial date, data_final date)
returns integer
language sql

as

$$

	select
		case
			when unidade in ('d', 'day', 'days') then (data_final - data_inicial)
			when unidade in ('w', 'week', 'weeks') then (data_final - data_inicial)/7
			when unidade in ('m', 'month', 'months') then (data_final - data_inicial)/30
			when unidade in ('y', 'year', 'years') then (data_final - data_inicial)/365
			end as diferenca

$$

select datediff('years', '2021-02-04', current_date)
```

```sql
drop function datediff
```