# Exercicio1
## Funcoes de agregacao
`select count(*)
from sales.funnel
`

`select count(paid_date)
from sales.funnel`

`select count(product_id)
from sales.funnel
where visit_page_date between '2021-01-01' and '2021-01-31'
`

`select count (distinct product_id)
from sales.funnel
where visit_page_date between '2021-01-01' and '2021-01-31'
`

`select min(price), max(price) , avg(price)
from sales.products
`

`select max(price) from sales.products`

`select * from sales.products
where price = (select max(price) from sales.products)`

# Exercicio2
## Group by
`select state, count(*) as contagem
from sales.customers
group by state
order by contagem desc`

`select state,professional_status, count(*) as contagem
from sales.customers
group by state,professional_status
order by state,contagem desc  
`

`select state from sales.customers
group by state`

# Exercicio3
## Having

`select state,count(*)
from sales.customers
group by state
having count(*) >100
`

`select state,count(*)
from sales.customers
group by state
having count(*) >100
	and state <> 'MG'`

#Desafio
## 1
`select count(*) from sales.customers
where ((current_date - birth_date)/365)<30
`
## 2
`select max((current_date - birth_date)/365),min((current_date - birth_date)/365) from sales.customers`
## 3
`select * from sales.customers
where income = (select max(income) from sales.customers)`
## 4
`select brand,count(brand) from sales.products
group by brand
order by brand`
## 5
`select brand,model_year,count(*) from sales.products
group by brand,model_year
order by brand,model_year`
## 6
`select brand,count(brand) from sales.products
group by brand
having count(brand)>10`