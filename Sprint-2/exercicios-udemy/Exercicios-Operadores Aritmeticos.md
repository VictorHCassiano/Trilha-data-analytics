# Exercicio 1
## Operadores aritmeticos
`
select email,
	birth_date,
	(current_date - birth_date) / 365 as idade_do_cliente
from sales.customers
order by idade_do_cliente
`

`select 
first_name || ' ' || last_name as nome_completo
from sales.customers`

# Exercicio 2
## Operadores de comparacao
`select 
customer_id,
first_name,
professional_status,
(professional_status = 'clt') as profissional_clt
from sales.customers
`
# Exercicio 3
## Operadores Logicos
`select * from sales.products
where price between 100000 and 200000
`

`select * 
from sales.products
where price not between 100000 and 200000
`

`select * from sales.products
where brand in ('HONDA','TOYOTA','RENAULT')
`

`select distinct first_name
from sales.customers
where first_name like '%ANA%'`

`select distinct first_name
from sales.customers
where first_name ilike 'ana%'`

`select * from temp_tables.regions
where population is null`

# Desafio
## 1
`select  income,email,(ROUND(income/1200))as quantidade_salarios_minimos from sales.customers`
## 2
`select  income,email,income/1200 as qnt_salario_minimo,(income/1200>=4) as acima4salarios
from sales.customers`
## 3
`select income,email from sales.customers
where income between 1200*4 and 1200*5`
## 4
`select email,city,state from sales.customers
where state = 'MT' or state = 'MG'`
## 5
`select email,city,state from sales.customers
where not state = 'SP'`
## 6
`select city from temp_tables.regions 
where city like  'Z%'`